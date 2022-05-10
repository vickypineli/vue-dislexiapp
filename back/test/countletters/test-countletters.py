from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.countletters import CountlettersRepository, Countletters

def test_should_return_empty_list_of_words():
    countletters_repository = CountlettersRepository(temp_file())
    app = create_app(repositories={"countletters": countletters_repository})
    client = app.test_client()
    response = client.get("/api/activities/countletters")

    assert response.json == []
