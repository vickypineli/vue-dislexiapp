from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.users import UserRepository, User

def test_should_return_empty_list_of_users():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    response = client.get("/api/users")

    assert response.json == []


def test_should_return_all_users_of_database():
    # ARRANGE (given)
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    user1 = User(
        id = "user-1",
        name = "Ander",
        password='0000',
    )
    user2 = User(
        id = "user-2",
        name = "Alba",
        password='0000',
    )

    user_repository.save(user1)
    user_repository.save(user2)

    # ACT (when)
    response = client.get("/api/users")
    # ASSERT (then)
    assert response.json == [
        {
            "id": "user-1",
            "name": "Ander",
            "password":'0000',
        },
        {
            "id": "user-2",
            "name": "Alba",
            "password":'0000',
        },
    ]
