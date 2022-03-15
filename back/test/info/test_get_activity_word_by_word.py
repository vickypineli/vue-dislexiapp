from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.activity import ActivityRepository, Activity

def test_should_return_activity_word_by_word():
    activity_repository = ActivityRepository(temp_file())
    app = create_app(repositories={"activities": activity_repository})
    client = app.test_client()

    response = client.get("/api/activities/word-by-word")

    assert response.json == []

