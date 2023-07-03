from neo4j import GraphDatabase

# Establish a connection to the Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j URI
username = "neo4j"  # Replace with your Neo4j username
password = "abc123"  # Replace with your Neo4j password

driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a node
def create_node():
    with driver.session() as session:
        session.run(
            "CREATE (c:Category:RootCategory {catId: '0000000', catName: 'Main_topic_classifications', fetched: false})"
        )
        print("Node created successfully.")

# Usage example
create_node()

# Close the database connection
driver.close()
