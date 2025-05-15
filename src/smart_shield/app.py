from flask import Flask


def create_app(test: bool = False):
    """Created application on Flask"""

    if test:
        _db = "sqlite://"
    else:
        _db = ""

    app = Flask(__name__, instance_relative_config=True)
    app.config["SEKRET_KEY"] = ""
    app.config["SQLALCHEMY_DATABASE_URI"] = _db

    @app.route("/", methods=["GET"])
    def index():
        return "OK", 200

    return app
