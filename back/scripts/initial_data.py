def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.activities import Activity, ActivityRepository
    from src.domain.wordbyword import Wordbyword, WordbywordRepository


    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)
    info_repository.save(Info(app_name="irla-kurri"))

    # Activities
    Activity1 = Activity(id="1", name="wordbyword")
    Activity2 = Activity(id="2", name="2 Actividad")
    Activity3 = Activity(id="3", name="3 Actividad")
    Activity4 = Activity(id="4", name="4 Actividad")

    activity_repository = ActivityRepository(database_path)
    activity_repository.save(Activity1)
    activity_repository.save(Activity2)
    activity_repository.save(Activity3)
    activity_repository.save(Activity4)

    #Wordbyword
    textoriginal1 = Wordbyword (text = "En un lugar la Mancha de cuyo nombre no quiero acordarme ")
    textoriginal2 = Wordbyword (text = "I can't believe the news today, y close my eyes it make it away ")
    textoriginal3 = Wordbyword (text = "Hala bazan ala ez bazan, sar dadila kalabazan eta atera dadila Foruko plazan ")
    
    wordbyword_repository = WordbywordRepository(database_path)
    
    wordbyword_repository.save(textoriginal1)
    wordbyword_repository.save(textoriginal2)
    wordbyword_repository.save(textoriginal3)
    
    print("Base de datos inicializada en" + database_path)

main()
