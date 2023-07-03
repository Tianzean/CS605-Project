from neo4j import GraphDatabase

# Establish a connection to the Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j URI
username = "neo4j"  # Replace with your Neo4j username
password = "abc123"  # Replace with your Neo4j password

driver = GraphDatabase.driver(uri, auth=(username, password))

# Import data
def import_data():
    with driver.session() as session:
        session.run(
            "MATCH (c:Category {fetched: false}) "
            "CALL apoc.load.json('https://en.wikipedia.org/w/api.php?format=json&action=query&list=categorymembers&cmtype=subcat&cmtitle=Category:' + replace(c.catName,' ', '%20 ') + '&cmprop=ids|title&cmlimit=500') "
            "YIELD value AS results "
            "UNWIND results.query.categorymembers AS subcat "
            "MERGE (sc:Category:Level9Category {catId: subcat.pageid}) "
            "ON CREATE SET sc.catName = substring(subcat.title, 9), sc.fetched = false "
            "MERGE (c)-[:has_subclass]->(sc) "
            "WITH DISTINCT c "
            "SET c.fetched = true"
        )
        print("Data imported successfully.")

# Usage example
import_data()

# Close the database connection
driver.close()
