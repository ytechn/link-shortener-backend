from elastic_manager import get_all_links, get_url_by_id, insert_link

class LinkShortener:
    @classmethod
    def get_all(self):
        return get_all_links()

    @classmethod
    def get_link_by_id(self,  id: str):
        try: 
            return get_url_by_id(id)
        except Exception as e:
            raise e
        
    @classmethod
    def shorten(self, url: str):
        return insert_link(url)























