import json

class JsonManager:
    @classmethod
    def read(self, file_name: str = "./data/links.json"):
        with open(file_name) as f:
            data = json.load(f)
        return data

    @classmethod
    def write(self, data, file_name: str = "./data/links.json"):
        try:
            with open(file_name, "w") as f:
                json.dump(data, f)
            return True
        except Exception as e:
            return False

