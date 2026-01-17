import uuid

def generate_reservation_code():
    return str(uuid.uuid4()).split('-')[0].upper()