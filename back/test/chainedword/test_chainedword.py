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
        img = 'img',
        question = 'Poliziaklapurraatxilotuzuen',
        answer = 'Poliziak lapurra atxilotu zuen'
    )
    phrase1 = Chainedword (
        id = "1",
        level = 'easy',
        img = 'img',
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
            "img" : 'img',
            "question": 'Poliziaklapurraatxilotuzuen',
            "answer": 'Poliziak lapurra atxilotu zuen'
        },
        {
            "id": "1",
            "level": "easy",
            "img" : 'img',
            "question": 'GaurMartarenurtebetetzeada',
            "answer": 'Gaur Martaren urtebetetzea da'
        }
    ]

# def test_should_return_list_of_phrases_by_level():
#     chainedword_repository = ChainedwordRepository(temp_file())
#     app = create_app(repositories={"chainedword": chainedword_repository})
#     client = app.test_client() 
#     phrase1 = Chainedword (
#         id = "1",
#         level = 'easy',
#         img = 'img1',
#         question = 'GaurMartarenurtebetetzeada',
#         answer = 'Gaur Martaren urtebetetzea da'
#     )
#     phrase2 = Chainedword (
#         id ="2",
#         level ='easy',
#         img = 'img2',
#         question = 'Poliziaklapurraatxilotuzuen',
#         answer = 'Poliziak lapurra atxilotu zuen'
#     )
#     phrase5 = Chainedword (
#         id = "5",
#         level = 'mediun',
#         img = 'img5',
#         question = 'Printzesaprintzearekingazteluanbizida',
#         answer = 'Printzesa printzearekin gazteluan bizi da'
#     )
#     phrase6 = Chainedword (
#         id ="6",
#         level ='mediun',
#         img = 'img6',
#         question = 'Markoriezzaizkiobarazkiakgustatzen',
#         answer = 'Markori ez zaizkio barazkiak gustatzen'
#     )
#     chainedword_repository.save(phrase1)
#     chainedword_repository.save(phrase2)
#     chainedword_repository.save(phrase5)
#     chainedword_repository.save(phrase6)

#     response = client.get("/api/activities/chainedword/easy")
        
#     assert response.json == [
#         {
#             "id": "1",
#             "level": "easy",
#             "img": 'img1',
#             "question": 'GaurMartarenurtebetetzeada',
#             "answer": 'Gaur Martaren urtebetetzea da'
#         },
#       ]

# def test_should_return_list_of_phrases_by_level_one_by_one():
#     chainedword_repository = ChainedwordRepository(temp_file())
#     app = create_app(repositories={"chainedword": chainedword_repository})
#     client = app.test_client()
#     phrase1 = Chainedword (
#         id = "1",
#         level = 'easy',
#         img = 'img1',
#         question = 'GaurMartarenurtebetetzeada',
#         answer = 'Gaur Martaren urtebetetzea da'
#     ) 
#     phrase2 = Chainedword (
#         id ="2",
#         level ='easy',
#         img = 'img2',
#         question = 'Poliziaklapurraatxilotuzuen',
#         answer = 'Poliziak lapurra atxilotu zuen'
#     )
#     phrase5 = Chainedword (
#         id = "5",
#         level = 'mediun',
#         img = 'img5',
#         question = 'Printzesaprintzearekingazteluanbizida',
#         answer = 'Printzesa printzearekin gazteluan bizi da'
#     )
#     phrase6 = Chainedword (
#         id ="6",
#         level ='mediun',
#         img = 'img6',
#         question = 'Markoriezzaizkiobarazkiakgustatzen',
#         answer = 'Markori ez zaizkio barazkiak gustatzen'
#     )
#     chainedword_repository.save(phrase1)
#     chainedword_repository.save(phrase2)
#     chainedword_repository.save(phrase5)
#     chainedword_repository.save(phrase6)

#     response = client.get("/api/activities/chainedword/easy")

#     assert response.json == [
#         {
#             "id": "1",
#             "level": "easy",
#             "img" : 'img1',
#             "question": 'GaurMartarenurtebetetzeada',
#             "answer": 'Gaur Martaren urtebetetzea da'
#         }
#     ]





