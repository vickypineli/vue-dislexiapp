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
        id = "1",
        word = "klariona",
        img = 'https://i.ibb.co/KrTZs1M/klariona.png',
        letters = '8',
        syllables = '3'
    )
    word2 = Countletters(
        id = "2",
        word = "platera",
        img ='https://i.ibb.co/6PrS7f6/platera.png',
        letters = '7',
        syllables = '3'
    )

    countletters_repository.save(word1)
    countletters_repository.save(word2)

    # ACT(then)
    response_word1 = client.get("/api/activities/countletters/1")

    # ASSERT(then)
    assert response_word1.json == {
        "id" :"1",
        "word" :"klariona",
        "img" :'https://i.ibb.co/KrTZs1M/klariona.png',
        "letters" :'8',
        "syllables" :'3'
    }
    
def test_should_return_list_of_words_by_random():
    # ARRANGE (given)
    countletters_repository = CountlettersRepository(temp_file())
    app = create_app(repositories={"countletters": countletters_repository})
    client = app.test_client()

    word1 = Countletters (
        id ="1",
        word ="klariona",
        img ='https://i.ibb.co/KrTZs1M/klariona.png',
        letters = '8',
        syllables = '3'
    )
    word2 = Countletters (
        id = "2",
        word = "platera",
        img = 'https://i.ibb.co/6PrS7f6/platera.png',
        letters = '7',
        syllables = '3'
    )
    word3 = Countletters (
        id ="3",
        word ='globoa',
        img ='https://i.ibb.co/HD3vSvV/globoa.png',
        letters = '8',
        syllables = '3'
    )
    word4 = Countletters (
        id = "4",
        word = 'kablea',
        img = 'https://i.ibb.co/L02r9W6/kablea.png',
        letters = '6',
        syllables = '3'
    )
    word5 = Countletters (
        id = "5",
        word = "palmera",
        img = 'https://i.ibb.co/3mkTm0j/palmera.png',
        letters = '7',
        syllables = '3'
    )
    word6 = Countletters (
        id ="6",
        word ="termometroa",
        img ='https://i.ibb.co/DwY3ttw/termometro.png',
        letters = '11',
        syllables = '5'
    )
    word7 = Countletters (
        id = "7",
        word = 'kalkulagailua',
        img = 'https://i.ibb.co/yP79QW7/kalkulagailua.png',
        letters = '7',
        syllables = '3'
    )
    word8 = Countletters (
        id ="8",
        word ='galtzerdiak',
        img ='https://i.ibb.co/Vv2zrCv/galtzerdiak.png',
        letters = '11',
        syllables = '4'
    )
    word9 = Countletters (
        id = "9",
        word = 'prakak',
        img = 'https://i.ibb.co/JHNMkhG/prakak2.png',
        letters = '6',
        syllables = '2'
    )
    word10 = Countletters (
        id = "10",
        word = 'tigrea',
        img = 'https://i.ibb.co/th5yYwc/tigrea.png',
        letters = '6',
        syllables = '3'
    )
    
    countletters_repository.save(word1)
    countletters_repository.save(word2)
    countletters_repository.save(word3)
    countletters_repository.save(word4)
    countletters_repository.save(word5)
    countletters_repository.save(word6)
    countletters_repository.save(word7)
    countletters_repository.save(word8)
    countletters_repository.save(word9)
    countletters_repository.save(word10)

    response = client.get("/api/activities/countlettersrandom")

    # ASSERT (then)
    assert response.json == [
        {
            "id": "10",
            "word": "tigrea",
            "img":'https://i.ibb.co/th5yYwc/tigrea.png',
            "letters": '6',
            "syllables": '3'
        },
        {
            "id": "8",
            "word": "galtzerdiak",
            "img":'https://i.ibb.co/Vv2zrCv/galtzerdiak.png',
            "letters": '11',
            "syllables": '4'
        },
        {
            "id": "2",
            "word": "platera",
            "img":'https://i.ibb.co/6PrS7f6/platera.png',
            "letters": '7',
            "syllables": '3'
        },
        {
            "id": "3",
            "word": "globoa",
            "img":'https://i.ibb.co/HD3vSvV/globoa.png',
            "letters": '6',
            "syllables": '3'
        },
    ]
