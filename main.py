from link_shortener import LinkShortener
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/health_check")
def health_check(r: Request):
    return "healthy"

@app.get("/all")
def get_all_links():
    results = LinkShortener.get_all()
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

