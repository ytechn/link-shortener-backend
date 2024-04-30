import uuid 
from utils.generate_id import generate_id
from utils.is_unique import is_unique

from json_manager import JsonManager

class LinkShortener:
    @classmethod
    def get_link_by_id(self,  id: str):
        url_entities = JsonManager.read()
        for url_entity in url_entities:
            if url_entity["id"] == id:
                return url_entity["url"]
        
        raise Exception("Your ID is not found")

    @classmethod
    def shorten(self, url: str):
        url_entities = JsonManager.read()

        for entity in url_entities:
            iter_url = entity["url"]
            if iter_url == url:
                return entity["id"]

        ids = [ entity["id"] for entity in url_entities ]
        unique_ids = list(set(ids))
        unique_id = generate_id()
        
        while not is_unique(unique_id, unique_ids):
            unique_id = generate_id()

        new_url_entity = {"id": unique_id, "url": url}
        url_entities.append(new_url_entity)
        JsonManager.write(url_entities)
        return unique_id




























