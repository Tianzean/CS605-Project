from neo4j import GraphDatabase

# Establish a connection to the Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j URI
username = "neo4j"  # Replace with your Neo4j username
password = "abc123"  # Replace with your Neo4j password

driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a index
def create_index():
    with driver.session() as session:
        session.run(
            "CREATE INDEX FOR (c:Category) ON (c.catId)"
        )
        print("Index created successfully.")

# Usage example
create_index()

# Close the database connection
driver.close()
