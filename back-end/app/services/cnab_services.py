from app.server import connect_db

db = connect_db()

def cnab_post_service():
    cnab = db["cnab"]
    ...
def cnab_get_service():
    cnab = db["cnab"]
    ...