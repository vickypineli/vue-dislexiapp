def main():
    
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.activities import Activity, ActivityRepository
    from src.domain.wordbyword import Wordbyword, WordbywordRepository

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)
    info_repository.save(Info(app_name="irla-kurri"))

    #Wordbyword
    textoriginal_1 = Wordbyword (language ="spanish_text", text = "En un lugar la Mancha de cuyo nombre no quiero acordarme ")
    textoriginal_2 = Wordbyword (language ="english_text", text = "I can't believe the news today, y close my eyes it make it away ")
    textoriginal_3 = Wordbyword (language ="basque_text", text = "Hala bazan ala ez bazan, sar dadila kalabazan eta atera dadila Foruko plazan ")
    
    wordbyword_repository = WordbywordRepository(database_path)
    
    wordbyword_repository.save(textoriginal_1)
    wordbyword_repository.save(textoriginal_2)
    wordbyword_repository.save(textoriginal_3)

    # Activities
    Activity_1 = Activity (id="act-1", name = "Wordbyword")
    Activity_2 = Activity (id="act-2", name = "C.semantica")
    Activity_3 = Activity (id="act-3", name = "C.fonologica")
    Activity_4 = Activity (id="act-4", name = "memoria secuencial")

    activity_repository = ActivityRepository(database_path)
   
    activity_repository.save(Activity_1)
    activity_repository.save(Activity_2)
    activity_repository.save(Activity_3)
    activity_repository.save(Activity_4)

    print("Base de datos inicializada en" + database_path)

main()
