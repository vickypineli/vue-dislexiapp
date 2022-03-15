
def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.activity import Activity, ActivityRepository


    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="irla-kurri"))

    Activity1 = Activity (text = "En un lugar la Mancha de cuyo nombre no quiero acordarme ")
                           
    activity_repository = ActivityRepository(database_path)
    activity_repository.save(Activity1)
    
    print("Base de datos inicializada en" + database_path)
    
    main()
