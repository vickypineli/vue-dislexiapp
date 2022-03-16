from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.activity import Activity

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
    
    @app.route("/api/activities/word-by-word/", methods=["GET"])
    def wordByWord_text_get():
        text_all = repositories["Activities"].get_text()
        return object_to_json(text_all)

    # @app.route("/api/activities/word-by-word/<id>", methods=["GET"])
    # def wordByWord_text_by_id(id):
    #     text = repositories["Activity"].get_by_id(id)
    #     return object_to_json(text)

        return app
