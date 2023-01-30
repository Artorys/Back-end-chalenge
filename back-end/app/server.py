from app.database import db

def start_server(app):
    db.init_app(app)
    return db
    
