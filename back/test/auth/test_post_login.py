from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.users import UserRepository, User

def setup():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    alba = User(user_id='user-2', name='Alba', password='0000')
    user_repository.save(alba)

    return client

def test_should_validate_login():
    client = setup()

    body = {
        "user": 'Alba',
        'password': '0000'
    }
    response = client.post(
        "/auth/login", json=body
    )

    assert response.status_code == 200

def test_should_fail_if_invalid_password():
    client = setup()

    body = {
        "user": 'pepe',
        'password': '45879'
    }
    response = client.post(
        "/auth/login", json=body
    )

    assert response.status_code == 401

def test_should_fail_if_user_not_exists():
    client = setup()

    body = {
        "user": 'user-not-exists',
        'password': '9999999'
    }
    response = client.post(
        "/auth/login", json=body
    )

    assert response.status_code == 401
