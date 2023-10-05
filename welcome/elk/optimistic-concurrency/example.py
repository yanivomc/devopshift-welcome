from elasticsearch import Elasticsearch, NotFoundError

es = Elasticsearch()

# Create a test document
doc = {
    "name": "John",
    "age": 30
}
res = es.index(index="test-index", id=1, body=doc)

# Fetch the document twice simulating two clients
doc1 = es.get(index="test-index", id=1)
doc2 = es.get(index="test-index", id=1)

# Update the age by both "clients"
doc1['_source']['age'] += 1
doc2['_source']['age'] += 2

# Try to update using version control
try:
    es.index(index="test-index", id=1, body=doc1['_source'], if_seq_no=doc1['_seq_no'], if_primary_term=doc1['_primary_term'])
    print("Doc1 updated successfully")
except NotFoundError:
    print("Conflict with Doc1 update!")

try:
    es.index(index="test-index", id=1, body=doc2['_source'], if_seq_no=doc2['_seq_no'], if_primary_term=doc2['_primary_term'])
    print("Doc2 updated successfully")
except NotFoundError:
    print("Conflict with Doc2 update!")
