import json 
from elasticsearch import Elasticsearch, helpers
from typing import Dict, List

LINKS_INDEX = "links"
es_client = Elasticsearch(["http://localhost:9200"])

def insert_link(url: str) -> str:
    response = es_client.index(
        index=LINKS_INDEX,
        body={"url": url}
    )

    return response.body["_id"]

def get_all_links() -> List:
    response = es_client.search(index=LINKS_INDEX)
    raw_results = response.body["hits"]["hits"]

    return [
        { "_id": r["_id"], "url": r["_source"]["url"] }
        for r in raw_results
    ]

def get_url_by_id(id: str) -> str:
    response = es_client.get(index=LINKS_INDEX, id=id)
    return response.body["_source"]["url"]