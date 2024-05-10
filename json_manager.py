import json

FILE_NAME = "./data/links.json"

class JsonManager:
    @classmethod
    def read(self, file_name: str = FILE_NAME):
        with open(file_name) as f:
            data = json.load(f)
        return data

    @classmethod
    def write(self, data, file_name: str = FILE_NAME):
        try:
            with open(file_name, "w") as f:
                json.dump(data, f)
            return True
        except Exception as e:
            return False

