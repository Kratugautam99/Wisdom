"""
5_Reliability_Operations.py

Demos:
- Transactions (ACID) with retries
- Inspect replication / cluster role (Causal Clustering)
- Backup & recovery examples (neo4j-admin and APOC)
- Security: create users and assign roles

Prereqs:
pip install neo4j requests
Neo4j server running and accessible. For backup commands, neo4j-admin must be available on the server host.

Edit NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD to match your instance.
"""

import subprocess
import time
from neo4j import GraphDatabase, basic_auth
from neo4j.exceptions import ServiceUnavailable, Neo4jError

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))

# -----------------------
# Transactions (ACID)
# -----------------------
def create_person_with_transaction(tx, person_id, name):
    # Example of a transactional unit of work
    tx.run(
        """
        MERGE (p:Person {personId: $person_id})
        ON CREATE SET p.name = $name, p.created = timestamp()
        ON MATCH SET p.lastSeen = timestamp()
        """,
        person_id=person_id, name=name
    )

def run_transaction_example():
    # Retry pattern for transient errors (updated to use v5 API)
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            # execute_write replaces write_transaction in neo4j driver v5+
            with driver.session() as session:
                session.execute_write(create_person_with_transaction, "person-123", "Dana")
            print("Transaction committed.")
            break
        except (ServiceUnavailable, Neo4jError) as e:
            print(f"Transaction failed on attempt {attempt}: {e}")
            if attempt == max_retries:
                raise
            time.sleep(1 * attempt)

# -----------------------
# Replication & HA
# -----------------------
def inspect_cluster():
    with driver.session() as session:
        try:
            # Returns role info for this database instance (core/replica/leader/follower)
            role_rec = session.run("CALL dbms.cluster.role() YIELD role RETURN role").single()
            print("Cluster role:", role_rec["role"] if role_rec else "unknown")

            # Cluster overview (may require appropriate privileges)
            try:
                overview = session.run(
                    "CALL dbms.cluster.overview() YIELD id, addresses, role RETURN id, addresses, role"
                ).values()
                print("Cluster overview (id, addresses, role):")
                for row in overview:
                    print(row)
            except Exception:
                print("dbms.cluster.overview() not available or insufficient privileges.")
        except Exception as e:
            print("Could not inspect cluster:", e)

# -----------------------
# Backup & Recovery
# -----------------------
def run_offline_backup(neo4j_admin_path="/usr/bin/neo4j-admin", backup_dir="/tmp/neo4j-backup"):
    """
    Example: run on the server host where neo4j-admin is installed.
    This is an illustrative subprocess call; in many deployments you run this on the DB host.
    """
    cmd = [neo4j_admin_path, "backup", "--backup-dir", backup_dir, "--name", "manual-backup"]
    try:
        print("Running neo4j-admin backup:", " ".join(cmd))
        subprocess.run(cmd, check=True)
        print("Backup completed to", backup_dir)
    except FileNotFoundError:
        print("neo4j-admin not found at", neo4j_admin_path)
    except subprocess.CalledProcessError as e:
        print("Backup command failed:", e)

def apoc_export_example():
    # Use APOC to export data to JSON/CSV (server must have APOC installed and allowed)
    with driver.session() as session:
        try:
            # Export whole DB to JSON (server-side file path)
            res = session.run(
                "CALL apoc.export.json.all($file, {}) YIELD file, nodes, relationships",
                file="/tmp/neo4j_export.json"
            )
            single = res.single()
            print("APOC export result:", single if single else "No result returned")
        except Exception as e:
            print("APOC export failed (is APOC installed and allowed?):", e)

# -----------------------
# Security: Users & Roles
# -----------------------
def create_user_and_assign_role(username, password, role="reader"):
    with driver.session() as session:
        try:
            # Create user (requires admin privileges)
            session.run("CREATE USER $username SET PASSWORD $password CHANGE NOT REQUIRED", username=username, password=password)
            print(f"User {username} created.")
        except Exception as e:
            print("Create user failed (may already exist or insufficient privileges):", e)

        try:
            # Grant role (built-in roles: admin, architect, publisher, reader, editor)
            session.run("GRANT ROLE $role TO $username", role=role, username=username)
            print(f"Granted role {role} to {username}.")
        except Exception as e:
            print("Grant role failed:", e)

def revoke_role(username, role):
    with driver.session() as session:
        try:
            session.run("REVOKE ROLE $role FROM $username", role=role, username=username)
            print(f"Revoked role {role} from {username}.")
        except Exception as e:
            print("Revoke role failed:", e)

# -----------------------
# Main demo runner
# -----------------------
if __name__ == "__main__":
    try:
        print("=== Transactions demo ===")
        run_transaction_example()

        print("\n=== Replication & HA inspection ===")
        inspect_cluster()

        print("\n=== Backup examples (illustrative) ===")
        # run_offline_backup()  # Uncomment to run on DB host with neo4j-admin available
        apoc_export_example()

        print("\n=== Security demo (create user & assign role) ===")
        # create_user_and_assign_role("demo_user", "demo_password", role="reader")
        print("Security commands shown; uncomment create_user_and_assign_role to execute.")

    finally:
        driver.close()
