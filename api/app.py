from flask_cors import CORS
from flask import Flask
from views.blueprint import blueprint


# dotenv env variables.
def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    CORS(app, resources={r"*": {"origins": "*"}})
    return app
