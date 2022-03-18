from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.wordbyword import WordbywordRepository, Wordbyword


def test_should_return_texts_in_wordbyword():
    wordbyword_repository = WordbywordRepository(temp_file())
    app = create_app(repositories={"wordbyword": wordbyword_repository})

    client = app.test_client()

    response = client.get("/api/activities/wordbyword")
    print(response)
    assert response.json == []
