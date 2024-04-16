from json_manager import JsonManager


class LinkShortener:

    @classmethod
    def get_link_by_id(self,  id: str):
        link_entities = JsonManager.read()
        for link_entity in link_entities:
            if link_entity["id"] == id:
                return link_entity["url"]
        
        raise Exception("Your ID is not found")

    # def short(self, )



























