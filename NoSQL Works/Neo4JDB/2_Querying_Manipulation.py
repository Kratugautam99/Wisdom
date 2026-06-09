"""
2_Querying_Manipulation.py

Demonstrates Cypher querying and data manipulation:
- MATCH, RETURN, WHERE
- CREATE, MERGE
- SET, REMOVE, DELETE
- Pattern matching and traversals
- Aggregation functions

Prereqs:
pip install neo4j

Configure connection by editing NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD.
"""

from neo4j import GraphDatabase, basic_auth

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))

def create_or_merge_nodes(tx):
    # MERGE ensures idempotent creation (create if not exists)
    tx.run(
        """
        MERGE (u:User {userId: $uid})
        ON CREATE SET u.name = $name, u.created = timestamp()
        ON MATCH SET u.lastSeen = timestamp()
        """,
        uid="u100", name="Charlie"
    )

    # CREATE multiple nodes and relationships
    tx.run(
        """
        CREATE (p:Post {postId: $postId, title: $title, likes: $likes})
        WITH p
        MATCH (u:User {userId: $uid})
        CREATE (u)-[:AUTHORED {since: $since}]->(p)
        """,
        postId="post1", title="Graph Databases 101", likes=10, uid="u100", since=2026
    )

def update_and_remove(tx):
    # SET to update properties; REMOVE to drop a property
    tx.run(
        """
        MATCH (p:Post {postId: $postId})
        SET p.likes = p.likes + $inc, p.updated = timestamp()
        REMOVE p.tempFlag
        """,
        postId="post1", inc=5
    )

def delete_example(tx):
    # Delete a relationship or node safely
    tx.run(
        """
        MATCH (u:User {userId: $uid})-[r:AUTHORED]->(p:Post {postId: $postId})
        DELETE r
        """,
        uid="u100", postId="post1"
    )
    # If you want to delete the node as well (and detach relationships)
    tx.run("MATCH (p:Post {postId: $postId}) DETACH DELETE p", postId="post1")

def pattern_matching_and_traversal(tx):
    # Find friends-of-friends (two-hop traversal) excluding direct friends
    result = tx.run(
        """
        MATCH (a:User {userId: $uid})-[:KNOWS]->(friend)-[:KNOWS]->(fof)
        WHERE NOT (a)-[:KNOWS]->(fof) AND a <> fof
        RETURN DISTINCT fof.userId AS fofId, fof.name AS fofName, COUNT(*) AS paths
        ORDER BY paths DESC
        LIMIT 10
        """,
        uid="u100"
    )
    print("Friends of friends suggestions:")
    for rec in result:
        print(rec["fofId"], rec["fofName"], "paths:", rec["paths"])

def aggregation_examples(tx):
    # Aggregations: counts, averages, collect
    result = tx.run(
        """
        MATCH (p:Post)<-[:AUTHORED]-(u:User)
        RETURN u.userId AS user, COUNT(p) AS postCount, AVG(p.likes) AS avgLikes, COLLECT(p.title)[0..5] AS sampleTitles
        ORDER BY postCount DESC
        LIMIT 10
        """
    )
    print("User post stats:")
    for rec in result:
        print(rec["user"], "posts:", rec["postCount"], "avgLikes:", rec["avgLikes"], "sample:", rec["sampleTitles"])

def explain_profile_example(tx):
    # Show how to get a query plan (EXPLAIN or PROFILE)
    # EXPLAIN returns the plan without executing; PROFILE executes and returns runtime stats.
    plan_cursor = tx.run("EXPLAIN MATCH (u:User)-[:AUTHORED]->(p:Post) RETURN u, p LIMIT 5")
    # Print raw records for inspection (driver returns plan metadata as records)
    print("EXPLAIN plan records:")
    for rec in plan_cursor:
        print(rec)

if __name__ == "__main__":
    try:
        with driver.session() as session:
            # Create or merge sample data
            session.execute_write(create_or_merge_nodes)

            # Demonstrate updates and removals
            session.execute_write(update_and_remove)

            # Demonstrate pattern matching/traversal
            session.execute_read(pattern_matching_and_traversal)

            # Demonstrate aggregations
            session.execute_read(aggregation_examples)

            # Show EXPLAIN usage (note: output object is driver-specific)
            session.execute_read(explain_profile_example)

            # Cleanup demo artifacts if desired (not shown here)
    finally:
        driver.close()
