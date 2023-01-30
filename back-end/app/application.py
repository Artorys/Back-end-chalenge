from flask import Flask
from app.routes import init_route
from flask_migrate import Migrate
from flask_cors import CORS
from app.server import start_server
from app.models import Cnab,Tipo
from app.utils.populate_type import populate_type
from app.config import URL,UPLOAD_FOLDER


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = URL
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    CORS(app,origin=["http://localhost:3000/"])

    db = start_server(app)

    Migrate(app,db)

    init_route(app)

    with app.app_context():
        populate_type(db,Tipo)

    return app