"""
6_Integrations_with_Extensions.py

Combined GraphQL server (Ariadne) + Neo4j integration demos for local testing.

Run:
  uv sync
  uv run "6_Integration_with_Extensions.py"
"""

import os
import tempfile
import threading
import time
import requests
import pandas as pd
from neo4j import GraphDatabase, basic_auth

# Ariadne imports (GraphQL server)
from ariadne import gql, make_executable_schema, QueryType
from ariadne.asgi import GraphQL
import uvicorn

# ---------- Configuration ----------
NEO4J_URI = "bolt://127.0.0.1:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"
GRAPHQL_HOST = "127.0.0.1"
GRAPHQL_PORT = 8081
GRAPHQL_ENDPOINT = f"http://{GRAPHQL_HOST}:{GRAPHQL_PORT}/graphql"

# Shared driver used by both GraphQL resolvers and demos
driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))


# -----------------------
# GraphQL server (Ariadne)
# -----------------------
type_defs = gql("""
type User { userId: ID! name: String }
type Post { postId: ID! title: String }
type Query { users: [User] }
""")

query = QueryType()

@query.field("users")
def resolve_users(*_):
    with driver.session() as s:
        res = s.run("MATCH (u:User) RETURN u.userId AS userId, u.name AS name LIMIT 50")
        return [{"userId": r["userId"], "name": r["name"]} for r in res]

schema = make_executable_schema(type_defs, query)
graphql_app = GraphQL(schema, debug=True)

def run_graphql_server():
    # Run uvicorn programmatically; this blocks so we run it in a thread.
    uvicorn.run(graphql_app, host=GRAPHQL_HOST, port=GRAPHQL_PORT, log_level="info")


# -----------------------
# Helpers and checks
# -----------------------
def procedure_exists(prefix: str) -> bool:
    try:
        with driver.session() as s:
            res = s.run("CALL dbms.procedures() YIELD name RETURN name")
            for r in res:
                if r["name"].startswith(prefix):
                    return True
    except Exception:
        return False
    return False

def is_http_up(url: str, timeout: float = 1.0) -> bool:
    try:
        r = requests.options(url, timeout=timeout)
        return r.status_code < 500
    except Exception:
        return False


# -----------------------
# Integration demos
# -----------------------
def python_driver_example(tx):
    res = tx.run("RETURN 'hello from neo4j' AS msg")
    rec = res.single()
    print("Driver test:", rec["msg"] if rec else "no result")

def run_pagerank(graph_name="myGraph"):
    if not procedure_exists("gds"):
        print("Skipping GDS demo: gds procedures not available.")
        return

    def project_graph(tx, graphName):
        tx.run(
            """
            CALL gds.graph.project(
              $graphName,
              ['Person','Post'],
              { KNOWS: {orientation: 'UNDIRECTED'}, AUTHORED: {orientation: 'NATURAL'} }
            )
            """,
            graphName=graphName,
        )

    def pagerank_stream(tx, graphName):
        return tx.run(
            """
            CALL gds.pageRank.stream($graphName)
            YIELD nodeId, score
            RETURN gds.util.asNode(nodeId).name AS name, score
            ORDER BY score DESC
            LIMIT 10
            """,
            graphName=graphName,
        )

    def drop_graph(tx, graphName):
        tx.run("CALL gds.graph.drop($graphName)", graphName=graphName)

    try:
        with driver.session() as session:
            session.execute_write(project_graph, graph_name)
            print("Graph projected:", graph_name)
            records = session.execute_read(pagerank_stream, graph_name)
            print("Top PageRank results:")
            for r in records:
                print(r["name"], r["score"])
            session.execute_write(drop_graph, graph_name)
    except Exception as e:
        print("GDS call failed (is GDS installed and licensed?):", e)

def bloom_integration_note():
    print("Neo4j Bloom: prepare data by adding descriptive labels and properties.")
    print(f"Open Bloom and connect to bolt://{GRAPHQL_HOST}:7687 with credentials to visualize.")

def create_csv_and_load():
    df = pd.DataFrame([{"userId": "u10", "name": "Eve"}, {"userId": "u11", "name": "Frank"}])
    tmpdir = "."
    csv_name = "users_import.csv"
    csv_path = os.path.join(tmpdir, csv_name)
    df.to_csv(csv_path, index=False)
    print("CSV written to", csv_path)

    # For Docker: ensure the container can access this path (mount host tmp into container)
    file_uri = "file:///" + csv_path.replace("\\", "/")

    def load_csv(tx, url):
        tx.run(
            """
            LOAD CSV WITH HEADERS FROM $url AS row
            MERGE (u:User {userId: row.userId})
            SET u.name = row.name
            """,
            url=url,
        )

    try:
        with driver.session() as session:
            session.execute_write(load_csv, file_uri)
            print("LOAD CSV executed (check server file access permissions).")
    except Exception as e:
        print("LOAD CSV failed (server file access or permissions):", e)

def graphql_query_example():
    if not is_http_up(GRAPHQL_ENDPOINT):
        print("Skipping GraphQL demo: no server listening at", GRAPHQL_ENDPOINT)
        return

    query = {"query": "{ users { userId name } }"}
    try:
        resp = requests.post(GRAPHQL_ENDPOINT, json=query, timeout=5)
        print("GraphQL status:", resp.status_code)
        try:
            print("GraphQL response:", resp.json())
        except Exception:
            print("GraphQL response (non-JSON):", resp.text)
    except Exception as e:
        print("GraphQL request failed:", e)


# -----------------------
# Main runner
# -----------------------
def main():
    # 1) Start GraphQL server in background thread
    server_thread = threading.Thread(target=run_graphql_server, daemon=True)
    server_thread.start()
    print(f"Starting GraphQL server on http://{GRAPHQL_HOST}:{GRAPHQL_PORT} ...")
    # wait briefly for server to come up
    time.sleep(1.0)

    # 2) Run integration demos
    try:
        print("\n=== Drivers demo ===")
        with driver.session() as session:
            try:
                session.execute_read(python_driver_example)
            except Exception as e:
                print("Driver demo failed:", e)

        print("\n=== Graph Data Science (PageRank) ===")
        run_pagerank()

        print("\n=== Neo4j Bloom note ===")
        bloom_integration_note()

        print("\n=== GraphQL example ===")
        graphql_query_example()

        print("\n=== ETL & Import demo ===")
        create_csv_and_load()

    finally:
        try:
            driver.close()
        except Exception:
            pass
        print("Done. GraphQL server thread is daemonized and will exit when process ends.")

if __name__ == "__main__":
    main()
