import uuid 
from elastic_manager import get_url_by_id
from utils.generate_id import generate_id
from utils.is_unique import is_unique

from json_manager import JsonManager

class LinkShortener:
    @classmethod
    def get_all_links(self):
        return JsonManager.read()

    @classmethod
    def get_link_by_id(self,  id: str):
        try: 
            return get_url_by_id(id)
        except Exception as e:
            raise e
        

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




























