"""
3_Advanced_Cypher_Features.py

Demonstrates:
- Indexes & constraints (creation, usage)
- Full-text search (create and query)
- APOC procedures (utility examples)
- Subqueries and CALL (modular queries)

Prereqs:
pip install neo4j
Ensure APOC is installed on the server for APOC examples.

Configure connection by editing NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD.
"""

import uuid
from neo4j import GraphDatabase, basic_auth

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"   

driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))


def create_indexes_and_constraints(tx):
    tx.run("CREATE CONSTRAINT user_id_unique IF NOT EXISTS FOR (u:User) REQUIRE u.userId IS UNIQUE")
    tx.run("CREATE INDEX post_title_idx IF NOT EXISTS FOR (p:Post) ON (p.title)")
    print("Indexes and constraints created (if not existing).")


def create_fulltext_index(tx):
    tx.run("CREATE FULLTEXT INDEX postsFullText IF NOT EXISTS FOR (p:Post) ON EACH [p.title, p.body]")
    print("Full-text index created (if not existing).")


def insert_sample_posts(tx):
    tx.run("CREATE (p:Post {postId: $id, title: $title, body: $body})",
           id="p1", title="Graph Databases", body="Intro to graph databases and Cypher.")
    tx.run("CREATE (p:Post {postId: $id, title: $title, body: $body})",
           id="p2", title="Full Text Search", body="Using full-text indexes in Neo4j.")
    print("Sample posts inserted.")


def query_fulltext_index(tx):
    result = tx.run("""
        CALL db.index.fulltext.queryNodes('postsFullText', $q)
        YIELD node, score
        RETURN node.postId AS id, score
        ORDER BY score DESC
    """, {"q": "graph OR full"})   # <-- parameters dict

    print("Full-text search results:")
    for r in result:
        print(r["id"], "score:", r["score"])




def apoc_examples(tx):
    generated_uuid = str(uuid.uuid4())
    tx.run("CREATE (n:Thing {name:$name, uuid:$uuid})", name="demo", uuid=generated_uuid)
    print("Python generated node uuid:", generated_uuid)

    print("APOC batch pattern (example, requires APOC):")
    print("CALL apoc.periodic.iterate('MATCH (n:Old) RETURN n', 'SET n.processed = true', {batchSize:1000})")



def subqueries_and_call(tx):
    tx.run("""
    MATCH (u:User)
    CALL {
      WITH u
      MATCH (u)-[:AUTHORED]->(p:Post)
      RETURN p ORDER BY p.likes DESC LIMIT 3
    }
    WITH u, collect(p.title) AS topTitles
    SET u.topPosts = topTitles
    RETURN u.userId AS user, topTitles
    """)
    print("Subquery and CALL examples executed.")


def cleanup(tx):
    tx.run("MATCH (n) WHERE n.postId IN ['p1','p2'] DETACH DELETE n")
    tx.run("MATCH (n:Thing {name:'demo'}) DETACH DELETE n")
    # tx.run("DROP INDEX postsFullText")  # optional cleanup
    print("Cleanup done.")


if __name__ == "__main__":
    try:
        with driver.session() as session:
            # Schema ops
            session.execute_write(create_indexes_and_constraints)
            session.execute_write(create_fulltext_index)

            # Data ops
            session.execute_write(insert_sample_posts)

            # Query ops
            session.execute_read(query_fulltext_index)

            # APOC + subqueries
            session.execute_write(apoc_examples)
            session.execute_write(subqueries_and_call)

            # Optional cleanup
            # session.execute_write(cleanup)
    finally:
        driver.close()
