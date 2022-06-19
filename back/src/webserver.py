from flask import Flask, request, jsonify
from flask_cors import CORS


from src.lib.utils import object_to_json
from src.domain.activities import Activity
from src.domain.wordbyword import Wordbyword
from src.domain.countletters import Countletters
from src.domain.users import UserRepository
from flask_jwt_extended import ( 
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)



def create_app(repositories):
    app = Flask(__name__)
    CORS(app)
       
    # app.config["JWT_SECRET_KEY"] = "5465436758585"  
    # jwt = JWTManager(app)

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        user = repositories["users"].get_user_by_id(body["user"])

        if user is None or (body["password"]) != user.password:
            return "", 401
        return user.to_dict(), 200

        # jwt_token = create_access_token(identity=user.id)
        # return jsonify(access_token=jwt_token), 200

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/users", methods=["GET"])
    def get_users():
        all_users = repositories["users"].get_all_users()
        return object_to_json(all_users)

    # @app.route("/api/activities", methods=["GET"])
    # def get_all_activities():
    #     all_activities = repositories["activities"].get_all()
    #     return object_to_json(all_activities)

    @app.route("/api/activities", methods=["GET"])
    # @jwt_required()
    def get_all_activities_by_user():
        user_id = request.headers.get("Authorization")
        # user_id = get_jwt_identity()
        print("****", user_id)

        all_activities = repositories["activities"].search_activities_by_user_id(user_id)
        return object_to_json(all_activities)

    @app.route("/api/activities/wordbyword", methods=["GET"])
    def get_texts_to_wordbyword():
        texts = repositories["wordbyword"].get_all_texts()
        return object_to_json(texts)

    @app.route("/api/activities/wordbyword/<language>", methods=["GET"])
    def get_text_of_wordbyword_by_language(language):
        text = repositories["wordbyword"].get_text_by_language(language)
        return object_to_json(text)

    @app.route("/api/activities/countletters", methods=["GET"])
    def get_all_words():
        all_words = repositories["countletters"].get_all_words()
        return object_to_json(all_words)

    @app.route("/api/activities/countletters/<id>", methods=["GET"])
    def get_word_by_id(id):
        words = repositories["countletters"].get_word_by_id(id)
        return object_to_json(words)

    @app.route("/api/activities/countlettersrandom", methods=["GET"])
    def get_words_by_random():
        words_by_random = repositories["countletters"].get_word_by_random()
        return object_to_json(words_by_random)

    @app.route("/api/activities/chainedword", methods=["GET"])
    def get_all_phrases():
        all_phrases = repositories["chainedword"].get_all_phrases()
        return object_to_json(all_phrases)

    @app.route("/api/activities/countletters/<level>", methods=["GET"])
    def get_phrases_by_level(level):
        phrases = repositories["countletters"].get_phrases_by_level(level)
        return object_to_json(phrases)
    return app