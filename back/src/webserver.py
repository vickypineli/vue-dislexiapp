from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    # @app.route("/api/activities", methods=["GET"])
    # def activities_get_all():
    #     all_activities = repositories["activities"].get_all_activities()
    #     return object_to_json(all_activities)   
    
    @app.route("/api/activities/word-by-word", methods=["GET"])
    def text_get():
        text_selected = repositories["texts"].get_text()
        return object_to_json(text_selected)

    return app
