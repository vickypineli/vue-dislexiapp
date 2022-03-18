from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json
<<<<<<< HEAD
from src.domain.activity import Activity
=======
from src.domain.activities import Activity
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735
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
<<<<<<< HEAD
    def activities_get_all():
        get_activities = repositories["activities"].get_all()
        return object_to_json(get_activities)

    @app.route("/api/activities/wordbyword", methods=["GET"])
    def get_text_to_wordbyword():
        texts = repositories["wordbyword"].get_texts
        return object_to_json(texts)
=======
    def get_all_activities():
        all_activities = repositories["activities"].get_all()
        return object_to_json(all_activities)   
    
    @app.route("/api/activities/word-by-word/", methods=["GET"])
    def wordByWord_text_get():
        text_all = repositories["wordbyword"].get_texts()
        return object_to_json(text_all)

    # @app.route("/api/activities/<name>", methods=["GET"])
    # def activity_by_name(name):
    #     Wordbyword = repositories["Activity"].get_by_name(name)
    #     return object_to_json(Wordbyword)
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735

    return app
