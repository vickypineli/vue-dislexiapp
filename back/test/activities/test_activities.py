from src.lib.utils import temp_file

from src.webserver import create_app
<<<<<<< HEAD:back/test/info/test_get_activity_word_by_word.py
from src.domain.wordbyword import WordbywordRepository, Wordbyword


def test_should_return_texts_in_wordbyword():
    wordbyword_repository = WordbywordRepository(temp_file())
    app = create_app(repositories={"wordbyword": wordbyword_repository})
=======
from src.domain.activities import ActivityRepository, Activity

def test_should_return_all_activities():
    activity_repository = ActivityRepository(temp_file())
    app = create_app(repositories={"activities": activity_repository})
    client = app.test_client()

    response = client.get("/api/activities")
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735:back/test/activities/test_activities.py

    client = app.test_client()

    response = client.get("/api/activities/wordbyword")
    print(response)
    assert response.json == []
