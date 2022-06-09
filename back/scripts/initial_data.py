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
    textoriginal_1 = Wordbyword (language ="Gaztelania", text = "En un lugar de la Mancha de cuyo nombre no quiero acordarme, no hace mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. ")
    textoriginal_2 = Wordbyword (language ="Ingelesa", text = "I can't believe the news today Oh, I can't close my eyes and make it go away. How long must we sing this song?")
    textoriginal_3 = Wordbyword (language ="Euskera", text = "Hala bazan ala ez bazan, sar dadila kalabazan eta atera dadila Foruko plazan ")
    
    wordbyword_repository = WordbywordRepository(database_path)
    
    wordbyword_repository.save(textoriginal_1)
    wordbyword_repository.save(textoriginal_2)
    wordbyword_repository.save(textoriginal_3)

    # Activities
    Activity_1 = Activity (id="act-1", name = "HITZEZ HITZ")
    Activity_2 = Activity (id="act-2", name = "IRAKUR-LAGUN")
    Activity_3 = Activity (id="act-3", name = "SILABAK ZENBATU")
    Activity_4 = Activity (id="act-4", name = "MARGOTU ZURE MEMORIA")
    Activity_5 = Activity (id="act-5", name = "BIKOTE JOLASA")
    Activity_6 = Activity (id="act-5", name = "HITZ KATEATUAK")

    activity_repository = ActivityRepository(database_path)
   
    activity_repository.save(Activity_1)
    activity_repository.save(Activity_2)
    activity_repository.save(Activity_3)
    activity_repository.save(Activity_4)

    #users
    user_repository = UserRepository(database_path)

    user1 = User (user_id='user_1', name='Ander', password='0000')
    user2 = User (user_id='user_2', name='Alba', password='0000')

    user_repository.save(user1)
    user_repository.save(user2)

    #countletters
    word1 = Countletters (user_id ='1', word='klariona', img='https://i.ibb.co/KrTZs1M/klariona.png', letters='8', syllables='3')
    word2 = Countletters (user_id ='2', word='platera', img='https://i.ibb.co/6PrS7f6/platera.png', letters='7', syllables='3')
    word3 = Countletters (user_id ='3', word='globoa', img='https://i.ibb.co/HD3vSvV/globoa.png', letters='6', syllables='3')
    word4 = Countletters (user_id ='4', word='kablea', img='https://i.ibb.co/L02r9W6/kablea.png', letters='6', syllables='3')
    word5 = Countletters (user_id ='5', word='palmera', img='https://i.ibb.co/3mkTm0j/palmera.png', letters='7', syllables='3')
    word6 = Countletters (user_id ='6', word='termometroa', img='https://i.ibb.co/DwY3ttw/termometro.png', letters='11', syllables='5')
    word7 = Countletters (user_id ='7', word='kalkulagailua', img='https://i.ibb.co/yP79QW7/kalkulagailua.png', letters='13', syllables='6')
    word8 = Countletters (user_id ='8', word='galtzerdiak', img='https://i.ibb.co/Vv2zrCv/galtzerdiak.png', letters='11', syllables='4')
    word9 = Countletters (user_id ='9', word='prakak', img='https://i.ibb.co/JHNMkhG/prakak2.png', letters='6', syllables='2')
    word10 = Countletters (user_id ='10', word='tigrea', img='https://i.ibb.co/th5yYwc/tigrea.png', letters='6', syllables='3')
    
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
