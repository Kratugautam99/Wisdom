"""
1_Core_Concepts.py

Demonstrates Neo4j core graph concepts:
- Nodes, relationships, properties
- Labels and relationship types
- Property graph model (attributes on nodes and relationships)

Prereqs:
pip install neo4j

Configure connection by editing NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD.
"""

from neo4j import GraphDatabase, basic_auth

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))

def create_sample_graph(tx):
    # Create nodes with labels and properties
    tx.run(
        """
        CREATE (a:Person {id: $idA, name: $nameA, age: $ageA})
        CREATE (b:Person {id: $idB, name: $nameB, age: $ageB})
        CREATE (c:Company {id: $idC, name: $companyName})
        """,
        idA="p1", nameA="Alice", ageA=30,
        idB="p2", nameB="Bob", ageB=35,
        idC="c1", companyName="Acme Corp"
    )

    # Create relationships with types and properties
    tx.run(
        """
        MATCH (a:Person {id: $idA}), (b:Person {id: $idB}), (c:Company {id: $idC})
        CREATE (a)-[:KNOWS {since: $sinceAB, closeness: $closeness}]->(b)
        CREATE (b)-[:WORKS_AT {role: $roleB, since: $sinceB}]->(c)
        """,
        idA="p1", idB="p2", idC="c1",
        sinceAB=2015, closeness=0.8,
        roleB="Engineer", sinceB=2018
    )

def read_graph(tx):
    # Return nodes and relationships with properties
    result = tx.run(
        """
        MATCH (p:Person)-[r]->(o)
        RETURN p.name AS person, type(r) AS rel_type, properties(r) AS rel_props, labels(o) AS object_labels, o
        LIMIT 25
        """
    )
    for record in result:
        print("Person:", record["person"])
        print("Relationship type:", record["rel_type"])
        print("Relationship properties:", record["rel_props"])
        print("Object labels:", record["object_labels"])
        # record["o"] is a Node; convert to dict for readable output
        try:
            node_dict = dict(record["o"])
        except Exception:
            # Fallback if direct conversion isn't supported
            node_dict = {k: record["o"].get(k) for k in record["o"].keys()}
        print("Object node:", node_dict)
        print("---")

def cleanup(tx):
    # Remove sample data (safe cleanup for demo)
    tx.run("MATCH (n) WHERE n.id IN ['p1','p2','c1'] DETACH DELETE n")

if __name__ == "__main__":
    with driver.session() as session:
        # Clean any previous demo data, then create and read
        session.execute_write(cleanup)
        session.execute_write(create_sample_graph)
        session.execute_read(read_graph)
        # Optional cleanup after demo
        # session.execute_write(cleanup)

    driver.close()
