from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.chainedword import ChainedwordRepository, Chainedword

def test_should_return_empty_list_of_phrases():
    chainedword_repository = ChainedwordRepository(temp_file())
    app = create_app(repositories={"chainedword": chainedword_repository})
    client = app.test_client()
    response = client.get("/api/activities/chainedword")

    assert response.json == []
    