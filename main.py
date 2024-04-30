from link_shortener import LinkShortener
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/health_check")
def health_check():
    return "healthy"

@app.get("/{id}")
def health_check(id: str):
    url = LinkShortener.get_link_by_id(id)
    return RedirectResponse(url)
















# urls = [
#     "https://walla.co.il",
#     "https://nana.co.il",
#     "https://ynet.co.il"
# ]

# for url in urls:
#     id = LinkShortener.shorten(url)
#     print(id)