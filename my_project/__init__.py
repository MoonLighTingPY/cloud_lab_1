import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flasgger import Swagger

from .auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"


db = SQLAlchemy()

todos = {}


def create_app(app_config: Dict[str, Any]) -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'rest',
                "route": '/rest_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
        "dom_id": "#swagger-ui",
        "deepLinking": True,
        "docExpansion": "list",
        "filter": True,
        "layout": "BaseLayout"
    }
    
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "REST-endpoints",
            "version": "1.0.0"
        },
        "schemes": ["http"]
    }
    
    Swagger(app, config=swagger_config, template=swagger_template)

    _init_db(app)
    register_routes(app)

    return app


def _init_db(app: Flask) -> None:
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()
