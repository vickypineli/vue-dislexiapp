import sqlite3

from src.webserver import create_app
from src.domain.info import InfoRepository
<<<<<<< HEAD
from src.domain.activity import ActivityRepository
from src.domain.wordbyword import WordbywordRepository

=======
from src.domain.activities import ActivityRepository
from src.domain.wordbyword import WordbywordRepository
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735

database_path = "data/database.db"

repositories = {
    "info": InfoRepository(database_path),
<<<<<<< HEAD
    "activities":ActivityRepository(database_path),
    "wordbyword":WordbywordRepository(database_path)
=======
    "activities": ActivityRepository(database_path),
    "wordbyword": WordbywordRepository(database_path),
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
