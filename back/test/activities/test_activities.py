from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.activities import ActivityRepository, Activity


def test_should_return_empty_list_of_activities():
    activity_repository = ActivityRepository(temp_file())
    app = create_app(repositories={"activities": activity_repository})
    client = app.test_client()
    # "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyLUFsYmEiLCJpYXQiOjE1MTYyMzkwMjJ9.vfg2H8LlQgB9gKZM4iqggw-ZNZRT8HoxXHgDQCmfwMY"

    response = client.get("/api/activities",headers={"Authorization": "user-Alba"})

    assert response.json == []

# def test_should_return_list_of_activities():
#     # ARRANGE (given)
#     activity_repository = ActivityRepository(temp_file())
#     app = create_app(repositories={"activities": activity_repository})
#     client = app.test_client()
   
#     Activity_1 = Activity (id="act-1", user_id="user-1", name = "IRAKUR-LAGUN")
#     Activity_2 = Activity (id="act-2", user_id="user-2", name = "HITZEZ HITZ")
    
#     activity_repository.save(Activity_1)
#     activity_repository.save(Activity_2)
#     # ACT (when)
#     response = client.get("/api/activities")

#     # ASSERT (then)
#     assert response.json == [
#         {   
#             "id":"act-1", 
#             "user_id": "user-Alba",
#             "name": "IRAKUR-LAGUN",
#         },
#         {
#             "id":"act-2",
#             "user_id": "user-Ander", 
#             "name": "HITZEZ HITZ",
#         },
#         ]

def test_should_return_list_of_activities_by_user():
        # ARRANGE (given)
        activity_repository = ActivityRepository(temp_file())
        app = create_app(repositories={"activities": activity_repository})
        client = app.test_client()

        Activity_1 = Activity(
            id= "act-1",
            user_id = "user-Alba",
            route ="play-word-by-word",
            name = "IRAKUR-LAGUN",
        )
        Activity_2 = Activity(
            id= "act-2",
            user_id= "user-Ander",
            route ="word-by-word",
            name= "HITZEZ HITZ",
        )

        activity_repository.save(Activity_1)
        activity_repository.save(Activity_2)

        # ACT (when)
        response = client.get("/api/activities", headers={"Authorization": "user-Alba"},)


        # ASSERT (then)
        # assert response.json == [
        #     {
        #         "id":"act-1",
        #         "user_id": "user-Alba",
        #         "name": "IRAKUR-LAGUN",
        #     }]
        activity_list = response.json
        assert len(activity_list) == 1
        assert activity_list[0]["id"] == "act-1"
        assert activity_list[0]["user_id"] == "user-Alba"
        assert activity_list[0]["name"] == "IRAKUR-LAGUN"
       
