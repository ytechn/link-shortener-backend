from link_shortener import LinkShortener


urls = [
    "https://walla.co.il",
    "https://nana.co.il"
]

for url in urls:
    id = LinkShortener.shorten(url)
    print(id)