# Reading into cassandra db documentation

### Terminology
[Terminology]([url](https://docs.datastax.com/en/astra/astra-db-vector/get-started/terminology.html)) 


### Quick start
[Quick Start]([url](https://docs.datastax.com/en/astra/astra-db-vector/get-started/quickstart.html)https://docs.datastax.com/en/astra/astra-db-vector/get-started/quickstart.html)


#### Objective

  Learn how to create a new database, connect to your database, load a set of vector embeddings, and perform a similarity search to find vectors that are close to the one in your query.

  The first handful of steps discuss setting up your serverless db, selecting a region, getting you app token and end point, and finally creating some environmental variable using the export key word in terminal.

  e.g. 
  export ASTRA_DB_API_ENDPOINT=API_ENDPOINT # Your database API endpoint
  export ASTRA_DB_APPLICATION_TOKEN=TOKEN # Your database application token

#### Questions:
  - Can we set environmental variables that are specific to to a virtual environment? How? please link source.
  
  - I don't understand the difference between creating a collection and loading vector embeddings...
    [Terminology]([url](https://docs.datastax.com/en/astra/astra-db-vector/get-started/terminology.html)) 


  #### Tip : Don't name astra init file astrapy.py as this will cause a namespace collision.


  #### Creating a collection:
  [Read this](https://docs.datastax.com/en/astra/astra-db-vector/get-started/quickstart.html#create-a-collection)

  
  
```python

import os

from astrapy.db import AstraDB

# Initialize the client. The namespace parameter is optional if you use
# "default_keyspace".
db = AstraDB(
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
    api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
    namespace="default_keyspace",
)
print(db)

# ⬇️ NEW CODE

# Create a collection. The default similarity metric is "cosine".
collection = db.create_collection("vector_test", dimension=5, metric="cosine")
print(collection)

# ⬆️ NEW CODE

# Delete the collection
res = db.delete_collection(collection_name="vector_test")
print(res)

```
  
