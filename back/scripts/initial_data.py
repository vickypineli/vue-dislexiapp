def main():
    
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.activities import Activity, ActivityRepository
    from src.domain.wordbyword import Wordbyword, WordbywordRepository
    from src.domain.users import UserRepository, User
    from src.domain.countletters import CountlettersRepository, Countletters

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)
    info_repository.save(Info(app_name="irla-kurri"))

    #Wordbyword
    textoriginal_1 = Wordbyword (language ="Gaztelania", text = "En un lugar de la Mancha de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. ")
    textoriginal_2 = Wordbyword (language ="Ingelesa", text = "I can't believe the news today Oh, I can't close my eyes and make it go away. How long must we sing this song?")
    textoriginal_3 = Wordbyword (language ="Euskera", text = "Hala bazan ala ez bazan, sar dadila kalabazan eta atera dadila Foruko plazan ")
    
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

    #users
    user_repository = UserRepository(database_path)

    user1 = User (id='user_1', name='Ander')
    user2 = User (id='user_2', name='Alba')

    user_repository.save(user1)
    user_repository.save(user2)

    #countletters
    word1 = Countletters (id ='word_1', word='klariona', img='https://ibb.co/6vDRmyb', letters='8', syllables='3')
    word2 = Countletters (id ='word_2', word='platera', img='https://ibb.co/0jrhGvz', letters='7', syllables='3')
    word3 = Countletters (id ='word_3', word='globoa', img='https://ibb.co/N931KLs', letters='6', syllables='3')
    word4 = Countletters (id ='word_4', word='kablea', img='https://ibb.co/ryPhn2q', letters='6', syllables='3')
    word5 = Countletters (id ='word_5', word='palmera', img='https://ibb.co/y8Dyb8R', letters='7', syllables='3')
    word6 = Countletters (id ='word_6', word='termometroa', img='https://ibb.co/QkrFnrV', letters='11', syllables='5')
    word7 = Countletters (id ='word_7', word='kalkulagailua', img='https://ibb.co/jLwq99T', letters='13', syllables='6')
    word8 = Countletters (id ='word_8', word='galtzerdiak', img='https://ibb.co/Y22SDn4', letters='11', syllables='4')
    word9 = Countletters (id ='word_9', word='prakak', img='https://ibb.co/K0L0c2g', letters='6', syllables='2')
    word10 = Countletters (id ='word_10', word='tigrea', img='https://ibb.co/BzD6qBQ', letters='6', syllables='3')
    
    countletters_repository = CountlettersRepository(database_path)

    countletters_repository.save(word1)
    countletters_repository.save(word2)
    countletters_repository.save(word3)
    countletters_repository.save(word4)
    countletters_repository.save(word5)
    countletters_repository.save(word6)
    countletters_repository.save(word7)
    countletters_repository.save(word8)
    countletters_repository.save(word9)
    countletters_repository.save(word10)

    
    
    print("Base de datos inicializada en" + database_path)

main()
