from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.wordbyword import WordbywordRepository, Wordbyword

def test_should_return_empty_list_of_texts():
    wordbyword_repository = WordbywordRepository(temp_file())
    app = create_app(repositories={"wordbyword": wordbyword_repository})
    client = app.test_client()
    response = client.get("/api/activities/wordbyword")

    assert response.json == []

def test_should_return_list_of_texts():
    # ARRANGE (given)
    wordbyword_repository = WordbywordRepository(temp_file())
    app = create_app(repositories={"wordbyword": wordbyword_repository})
    client = app.test_client()

    textoriginal1 = Wordbyword()
    textoriginal2 = Wordbyword()

    wordbyword_repository.save(textoriginal1)
    wordbyword_repository.save(textoriginal2)

    # ACT (when)
    response = client.get("/api/activities/wordbyword")

    # ASSERT (then)
    assert response.json == [
        {"id": 1, "test": "En un lugar la Mancha de cuyo nombre no quiero acordarme"},
        {"id": 2, "test": "I can't believe the news today, y close my eyes it make it away"},
    ]
