from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.chainedword import ChainedwordRepository, Chainedword

def test_should_return_empty_list_of_phrases():
    chainedword_repository = ChainedwordRepository(temp_file())
    app = create_app(repositories={"chainedword": chainedword_repository})
    client = app.test_client()
    response = client.get("/api/activities/chainedword")

    assert response.json == []

def test_should_return_list_of_phrases():
    chainedword_repository = ChainedwordRepository(temp_file())
    app = create_app(repositories={"chainedword": chainedword_repository})
    client = app.test_client()

    phrase2 = Chainedword (
        id ="2",
        level ='easy',
        question = 'Poliziaklapurraatxilotuzuen',
        answer = 'Poliziak lapurra atxilotu zuen'
    )
    phrase1 = Chainedword (
        id = "1",
        level = 'easy',
        question = 'GaurMartarenurtebetetzeada',
        answer = 'Gaur Martaren urtebetetzea da'
    )

    chainedword_repository.save(phrase2)
    chainedword_repository.save(phrase1)

    response = client.get("/api/activities/chainedword")


    assert response.json == [
        {
            "id": "2",
            "level": "easy",
            "question": 'Poliziaklapurraatxilotuzuen',
            "answer": 'Poliziak lapurra atxilotu zuen'
        },
        {
            "id": "1",
            "level": "easy",
            "question": 'GaurMartarenurtebetetzeada',
            "answer": 'Gaur Martaren urtebetetzea da'
        }
    ]
def test_should_return_list_of_phrases_by_level():
    chainedword_repository = ChainedwordRepository(temp_file())
    app = create_app(repositories={"chainedword": chainedword_repository})
    client = app.test_client() 

    phrase6 = Chainedword (
        id ="6",
        level ='mediun',
        question = 'Markoriezzaizkiobarazkiakgustatzen',
        answer = 'Markori ez zaizkio barazkiak gustatzen'
    )
    phrase5 = Chainedword (
        id = "5",
        level = 'mediun',
        question = 'Printzesaprintzearekingazteluanbizida',
        answer = 'Printzesa printzearekin gazteluan bizi da'
    )
    phrase2 = Chainedword (
        id ="2",
        level ='easy',
        question = 'Poliziaklapurraatxilotuzuen',
        answer = 'Poliziak lapurra atxilotu zuen'
    )
    phrase1 = Chainedword (
        id = "1",
        level = 'easy',
        question = 'GaurMartarenurtebetetzeada',
        answer = 'Gaur Martaren urtebetetzea da'
    )
    chainedword_repository.save(phrase6)
    chainedword_repository.save(phrase5)
    chainedword_repository.save(phrase2)
    chainedword_repository.save(phrase1)

    response = client.get("/api/activities/chainedword/easy")
        
    assert response.json == [
        {
            "id": "2",
            "level": "easy",
            "question": 'Poliziaklapurraatxilotuzuen',
            "answer": 'Poliziak lapurra atxilotu zuen'
        },
        {
            "id": "1",
            "level": "easy",
            "question": 'GaurMartarenurtebetetzeada',
            "answer": 'Gaur Martaren urtebetetzea da'
        }]
    # phrases_list = response.json
    # assert len(phrases_list) == 2
    # assert phrases_list[0]["id"] == "1"
    # assert phrases_list[0]["level"] == "easy"
    # assert phrases_list[0]["question"] == "GaurMartarenurtebetetzeada"
    # assert phrases_list[0]["answer"] == "Gaur Martaren urtebetetzea da"





