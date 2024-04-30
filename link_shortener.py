import uuid 
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

        ids = [ entity["id"] for entity in url_entities ]
        unique_ids = list(set(ids))
        unique_id = str(uuid.uuid4())[:8]
        
        while unique_id in unique_ids:
            unique_id = str(uuid.uuid4())[:8]

        new_url_entity = {"id": unique_id, "url": url}
        url_entities.append(new_url_entity)
        JsonManager.write(url_entities)
        return unique_id




























