from elasticsearch import Elasticsearch, helpers
import json

# Connect to the Elasticsearch instance
es = Elasticsearch(['http://localhost:9200'])

# Load your JSON data
with open('./datasets/ecommerce.json', 'r') as f:
    json_data = json.load(f)

# Create the bulk data format
def generate_data(json_data):
    for item in json_data:
        yield {
            "_index": "ecommerce_data",
            "_source": item
        }

# Perform the bulk upload
helpers.bulk(es, generate_data(json_data))

print("Data uploaded successfully.")
