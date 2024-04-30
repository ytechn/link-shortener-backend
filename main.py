from link_shortener import LinkShortener


urls = [
    "https://walla.co.il",
    "https://nana.co.il",
    "https://ynet.co.il"
]

for url in urls:
    id = LinkShortener.shorten(url)
    print(id)