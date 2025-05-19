from flask import Flask
from sqlalchemy import inspect

from configs import DEBUG, SECRET_KEY, database


def create_app(test: bool = False):
    """Created application on Flask"""

    if test:
        _db = "sqlite://"
    else:
        _db = database

    app = Flask(__name__, instance_relative_config=True)
    app.config["SEKRET_KEY"] = SECRET_KEY
    app.config["DEBUG"] = DEBUG
    app.config["SQLALCHEMY_DATABASE_URI"] = _db

    from .models import db

    db.init_app(app)

    @app.before_request
    def before_request():
        """
        Проверка существуют ли таблицы в базе данных и создаются таблицы,
        если они отсутствуют.
        """
        tables = inspect(db.engine).get_table_names()
        if not tables:
            db.create_all()

    @app.route("/", methods=["GET"])
    def index():
        return "OK", 200

    return app
