from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.activity import Activity
from src.domain.wordbyword import Wordbyword


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

    @app.route("/api/activities", methods=["GET"])
    def get_all_activities():
        all_activities = repositories["Activities"].get_all()
        return object_to_json(all_activities)   
    
    @app.route("/api/activities/word-by-word/", methods=["GET"])
    def wordByWord_text_get():
        text_all = repositories["Wordbyword"].get_texts()
        return object_to_json(text_all)

    # @app.route("/api/activities/<name>", methods=["GET"])
    # def activity_by_name(name):
    #     Wordbyword = repositories["Activity"].get_by_name(name)
    #     return object_to_json(Wordbyword)

    return app
