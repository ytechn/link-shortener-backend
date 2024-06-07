import logging
import os

from link_shortener import LinkShortener
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from logging.handlers import SocketHandler
from logstash_formatter import LogstashFormatterV1

LOGSTASH_HOST = os.getenv("LOGSTASH_HOST")
LOGSTASH_PORT = int(os.getenv("LOGSTASH_PORT"))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logstash_handler = SocketHandler(LOGSTASH_HOST, LOGSTASH_PORT)
logstash_handler.setFormatter(LogstashFormatterV1)
logger.addHandler(logstash_handler)

app = FastAPI()

@app.get("/health_check")
def health_check(r: Request):
    return "healthy"

@app.get("/all")
def get_all_links():
    results = LinkShortener.get_all()
    logging.error("FETCHED ALL LINKS")
    return results

@app.post("/shorten")
def create_url(params: dict):
    url = params["url"]
    id = LinkShortener.shorten(url)
    return {"id": id}

@app.get("/{id}")
def get_link_by_id(id: str):
    url = LinkShortener.get_link_by_id(id)
    return RedirectResponse(url)

