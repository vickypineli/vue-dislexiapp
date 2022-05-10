import sqlite3

from src.webserver import create_app

from src.domain.info import InfoRepository
from src.domain.activities import ActivityRepository
from src.domain.wordbyword import WordbywordRepository
from src.domain.users import UserRepository
from src.domain.countletters import CountlettersRepository

database_path = "data/database.db"

repositories = {
    "info": InfoRepository(database_path),
    "activities":ActivityRepository(database_path),
    "wordbyword":WordbywordRepository(database_path),
    "users": UserRepository(database_path),
    "countletters": CountlettersRepository(database_path)
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
