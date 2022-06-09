from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.activities import ActivityRepository, Activity


def test_should_return_empty_list_of_activities():
    activity_repository = ActivityRepository(temp_file())
    app = create_app(repositories={"activities": activity_repository})
    client = app.test_client()
    response = client.get("/api/activities")

    assert response.json == []

def test_should_return_list_of_activities():
    # ARRANGE (given)
    activity_repository = ActivityRepository(temp_file())
    app = create_app(repositories={"activities": activity_repository})
    client = app.test_client()
   
    Activity_1 = Activity (id="act-1", user_id = "user-Alba", name = "IRAKUR-LAGUN")
    Activity_2 = Activity (id="act-2", user_id = "user-Ander", name = "HITZEZ HITZ")
    
    activity_repository.save(Activity_1)
    activity_repository.save(Activity_2)
    # ACT (when)
    response = client.get("/api/activities")

    # ASSERT (then)
    assert response.json == [
        {   
            "id":"act-1", 
            "user_id": "user-Alba",
            "name": "IRAKUR-LAGUN",
        },
        {
            "id":"act-2",
            "user_id": "user-Ander", 
            "name": "HITZEZ HITZ",
        },

        ]

def test_should_return_list_of_activities_by_user():
        # ARRANGE (given)
        activity_repository = ActivityRepository(temp_file())
        app = create_app(repositories={"activities": activity_repository})
        client = app.test_client()

        Activity_1 = Activity(
            id= "act-1",
            user_id = "user-Alba",
            name = "IRAKUR-LAGUN",
        )
        Activity_2 = Activity(
            id= "act-2",
            user_id= "user-Ander",
            name= "HITZEZ HITZ",
        )

        activity_repository.save(Activity_1)
        activity_repository.save(Activity_2)

        # ACT (when)
        response = client.get("/api/activities", headers={"Authorization": "user-Alba"})

        # ASSERT (then)
        activity_list = response.json
        assert len(activity_list) == 1
        assert activity_list[0]["id"] == "act-1"
        assert activity_list[0]["name"] == "IRAKUR-LAGUN"
       
