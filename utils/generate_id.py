import uuid

def generate_id(len: int = 8):
    return str(uuid.uuid4())[:len]