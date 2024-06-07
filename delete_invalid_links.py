import requests
from link_shortener import LinkShortener
from json_manager import JsonManager

url_entities = LinkShortener.get_all()
new_url_entities = []

def is_valid_link(link: str) -> bool:
    try:
        response = requests.get(link, )
        status_code = response.status_code
        if status_code in [200, 201]:
            return True
        return False
    except:
        return False

for entity in url_entities:
    entity_url = entity["url"]
    if is_valid_link(entity_url):
        new_url_entities.append(entity)

JsonManager.write(new_url_entities)