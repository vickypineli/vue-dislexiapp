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

    textoriginal_1 = Wordbyword(id="1", text="En un lugar la Mancha de cuyo nombre no quiero acordarme")
    textoriginal_2 = Wordbyword(id="2", text="I can't believe the news today, y close my eyes it make it away")

    wordbyword_repository.save(textoriginal_1)
    wordbyword_repository.save(textoriginal_2)

    # ACT (when)
    response = client.get("/api/activities/wordbyword")

    # ASSERT (then)
    assert response.json == [
        {"id":"1", "text":"En un lugar la Mancha de cuyo nombre no quiero acordarme"},
        {"id":"2", "text":"I can't believe the news today, y close my eyes it make it away"},
    ]
