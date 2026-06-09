"""
4_Performance_Scaling.py

Demonstrates:
- Query tuning with EXPLAIN and PROFILE
- Index creation (native, composite)
- Simple caching and memory-awareness tips (illustrative)
- Notes and commands for clustering/sharding (server-side actions)

Prereqs:
pip install neo4j

Configure connection by editing NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD.
"""

from neo4j import GraphDatabase, basic_auth

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))


def create_sample_data(tx):
    # Create sample users and posts for profiling
    tx.run(
        """
    UNWIND $users AS u
    MERGE (user:User {userId: u.userId})
    SET user.name = u.name
    """,
        users=[{"userId": "u1", "name": "Alice"}, {"userId": "u2", "name": "Bob"}],
    )

    tx.run(
        """
    UNWIND $posts AS p
    MERGE (post:Post {postId: p.postId})
    SET post.title = p.title, post.likes = p.likes
    """,
        posts=[
            {"postId": "post1", "title": "Intro", "likes": 10},
            {"postId": "post2", "title": "Advanced", "likes": 50},
        ],
    )

    tx.run(
        """
    MATCH (u:User {userId:'u1'}), (p:Post {postId:'post2'})
    MERGE (u)-[:AUTHORED]->(p)
    """
    )


def create_indexes(tx):
    # Native single-property index
    tx.run("CREATE INDEX IF NOT EXISTS FOR (u:User) ON (u.userId)")
    # Composite index example
    tx.run("CREATE INDEX IF NOT EXISTS FOR (p:Post) ON (p.postId, p.title)")
    print("Indexes created (if not existing).")


def explain_and_profile(tx):
    # EXPLAIN: shows the plan without executing
    explain_result = tx.run(
        "EXPLAIN MATCH (u:User)-[:AUTHORED]->(p:Post) WHERE p.likes > $min RETURN u.userId, p.postId LIMIT 5",
        min=5,
    )
    print("EXPLAIN plan records:")
    for record in explain_result:
        print(record)

    # PROFILE: executes and returns runtime stats
    profile_result = tx.run(
        "PROFILE MATCH (u:User)-[:AUTHORED]->(p:Post) WHERE p.likes > $min RETURN u.userId, p.postId LIMIT 5",
        min=5,
    )
    print("PROFILE results (rows):")
    for row in profile_result:
        print(row)


def memory_and_caching_tips(tx):
    # MEMORY USAGE is server-side; query memory-related config where available
    try:
        res = tx.run(
            "CALL dbms.listConfig() YIELD name, value WHERE name CONTAINS 'dbms.memory' RETURN name, value"
        )
        print("Memory-related config (sample):")
        for r in res:
            print(r["name"], "=", r["value"])
    except Exception as e:
        print("Could not fetch memory config (permissions or version):", e)

    print("Caching tips:")
    print("- Ensure frequently queried properties are indexed.")
    print("- Use query patterns that allow index seeks (avoid leading wildcards).")
    print("- Warm the page cache by running representative queries after startup.")


def clustering_and_sharding_notes():
    # Clustering and sharding are configured server-side. Provide commands and notes.
    print("Clustering & sharding notes:")
    print("- Use Causal Clustering for HA and read scaling (enterprise).")
    print("- Use Fabric for cross-database sharding in larger deployments.")
    print("- Server-side tools: neo4j-admin, neo4j.conf, and orchestration (K8s).")
    print("- Example: check cluster status via: CALL dbms.cluster.role() or via neo4j-admin cluster commands on the server.")


def cleanup(tx):
    tx.run("MATCH (u:User) WHERE u.userId IN ['u1','u2'] DETACH DELETE u")
    tx.run("MATCH (p:Post) WHERE p.postId IN ['post1','post2'] DETACH DELETE p")


if __name__ == "__main__":
    try:
        with driver.session() as session:
            # Create sample data and indexes (write operations)
            session.execute_write(create_sample_data)
            session.execute_write(create_indexes)

            # Run explain/profile and memory checks (read operations)
            session.execute_read(explain_and_profile)
            session.execute_read(memory_and_caching_tips)

            # Print clustering/sharding notes (local helper)
            clustering_and_sharding_notes()

            # Optional cleanup (uncomment to remove demo data)
            # session.execute_write(cleanup)
    finally:
        driver.close()
