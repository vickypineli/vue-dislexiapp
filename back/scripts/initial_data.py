
def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.activity import Activity, ActivityRepository
    from src.domain.wordbyword import Wordbyword, WordbywordRepository

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)
    info_repository.save(Info(app_name="irla-kurri"))

    textoriginal = Wordbyword (text = "En un lugar la Mancha de cuyo nombre no quiero acordarme ")
    
    wordbyword_repository = WordbywordRepository(database_path)
    wordbyword_repository.save(textoriginal)
    
    
    Activity1 = Activity (id = "activity-1", name = "wordbyword" )
                           
    activity_repository = ActivityRepository(database_path)
    activity_repository.save(Activity1)
    
    print("Base de datos inicializada en" + database_path)
    
    main()
