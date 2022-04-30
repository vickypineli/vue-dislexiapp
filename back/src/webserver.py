from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.activities import Activity
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
        all_activities = repositories["activities"].get_all()
        return object_to_json(all_activities)

    @app.route("/api/activities/wordbyword", methods=["GET"])
    def get_texts_to_wordbyword():
        texts = repositories["wordbyword"].get_all_texts()
        return object_to_json(texts)

    @app.route("/api/activities/wordbyword/<language>", methods=["GET"])
    def get_text_of_wordbyword_by_language(language):
        text = repositories["wordbyword"].get_text_by_language(language)
        return object_to_json(text)

    @app.route("/api/users", methods=["GET"])
    def get_users():
        all_users = repositories["users"].get_users()
        return object_to_json(all_users)

    return app
