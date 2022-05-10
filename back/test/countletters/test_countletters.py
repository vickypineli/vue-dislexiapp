from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.countletters import CountlettersRepository, Countletters

def test_should_return_empty_list_of_words():
    countletters_repository = CountlettersRepository(temp_file())
    app = create_app(repositories={"countletters": countletters_repository})
    client = app.test_client()
    response = client.get("/api/activities/countletters")

    assert response.json == []

def test_should_return_list_of_words():
    # ARRANGE (given)
    countletters_repository = CountlettersRepository(temp_file())
    app = create_app(repositories={"countletters": countletters_repository})
    client = app.test_client()

    word1 = Countletters (
        id ="word_1",
        word ="klariona",
        img ='https://ibb.co/6vDRmyb',
        letters = '8',
        syllables = '3'
    )
    word2 = Countletters (
        id = "word_2",
        word = "platera",
        img = 'https://ibb.co/0jrhGvz',
        letters = '7',
        syllables = '3'
    )

    countletters_repository.save(word1)
    countletters_repository.save(word2)
    response = client.get("/api/activities/countletters")

    # ASSERT (then)
    assert response.json == [
        {
            "id": "word_1",
            "word": "klariona",
            "img":'https://ibb.co/6vDRmyb',
            "letters": '8',
            "syllables": '3'
        },
        {
            "id": "word_2",
            "word": "platera",
            "img":'https://ibb.co/0jrhGvz',
            "letters": '7',
            "syllables": '3'
        },
    ]
def test_should_return_word_by_id():
# ARRANGE (given)
    countletters_repository = CountlettersRepository(temp_file())
    app = create_app(repositories={"countletters": countletters_repository})
    client = app.test_client()

    word1 = Countletters(
        id = "word_1",
        word = "klariona",
        img = 'https://ibb.co/6vDRmyb',
        letters = '8',
        syllables = '3'
    )
    word2 = Countletters(
        id = "word_2",
        word = "platera",
        img ='https://ibb.co/0jrhGvz',
        letters = '7',
        syllables = '3'

    )

    countletters_repository.save(word1)
    countletters_repository.save(word2)

    # ACT(then)
    response_word1 = client.get("/api/activities/countletters/word_1")
    

    # ASSERT(then)
    assert response_word1.json == {
        "id" :"word_1",
        "word" :"klariona",
        "img" :'https://ibb.co/6vDRmyb',
        "letters" :'8',
        "syllables" :'3'
    }
    