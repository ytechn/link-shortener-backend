from link_shortener import LinkShortener
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/api/health_check")
def health_check(r: Request):
    return "healthy"

@app.get("/api/{id}")
def health_check(id: str):
    url = LinkShortener.get_link_by_id(id)
    return RedirectResponse(url)

@app.post("/api/shorten")
def create_url(params: dict):
    url = params["url"]
    id = LinkShortener.shorten(url)
    return {"id": id}
