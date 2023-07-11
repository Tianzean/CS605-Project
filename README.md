# CS605-Project
Extracting hierarchical topic taxonomy from knowledge graph

# Link to Repository
[Repository Link] https://github.com/Tianzean/CS605-Project.git

# Set-up
1. Neo4j 5.9.0
2. start neo4j environment
```
$ Neo4j console
```
4. install neo4j-driver
5. Neo4j database contact with neo4j-driver in Python
```
$ uri = "bolt://localhost:7687"  # Replace with your Neo4j URI
$ username = "neo4j"  # Replace with your Neo4j username
$ password = "abc123"  # Replace with your Neo4j password
```
7. Run CreateNode.py, CreateCatid.py and ImportData.py in sequence

# Execution
1. Firstly, running CreateNode.py
2. Secondly, running CreateCatid.py to create the index.
3. After that, running importData.py and pay attention to "sc:Category:Level1Category" in the line 18
4. After Level1Category, modifying "sc:Category:Level1Category" into "sc:Category:Level2Category" and running importData.py
5. And so on, getting the diagram in the Neo4j database

# Languages & tools
1. Python
2. Neo4j
3. PyCharm

# Authors
- Tianze An (22250240)
