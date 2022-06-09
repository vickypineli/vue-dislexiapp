from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.users import UserRepository, User

# def setup():
#     user_repository = UserRepository(temp_file())
#     app = create_app(repositories={"users": user_repository})
#     client = app.test_client()

#     tomas = User(id='user-tomas', name='Tomás', password='el mejor')
#     user_repository.save(tomas)

#     return client

# def test_should_validate_login():
#     client = setup()

#     body = {
#         "user": 'user-tomas',
#         'password': 'el mejor'
#     }
#     response = client.post(
#         "/auth/login", json=body
#     )

#     assert response.status_code == 200
#     assert response.json == {
#         'id': 'user-tomas',
#         'name': 'Tomás'
#     }

# def test_should_fail_if_invalid_password():
#     client = setup()

#     body = {
#         "user": 'user-tomas',
#         'password': 'el peor'
#     }
#     response = client.post(
#         "/auth/login", json=body
#     )

#     assert response.status_code == 401

# def test_should_fail_if_user_not_exists():
#     client = setup()

#     body = {
#         "user": 'user-not-exists',
#         'password': 'el mediano'
#     }
#     response = client.post(
#         "/auth/login", json=body
#     )

#     assert response.status_code == 401
