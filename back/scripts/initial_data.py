

def main():
    
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.wordbyword import Wordbyword, WordbywordRepository
    from src.domain.activities import Activity, ActivityRepository
    from src.domain.users import UserRepository, User
    from src.domain.countletters import CountlettersRepository, Countletters
    from src.domain.chainedword import ChainedwordRepository, Chainedword

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)
    info_repository.save(Info(app_name="irla-kurri"))


    textoriginal_1 = Wordbyword (language ="Gaztelania", text = "En un lugar de la Mancha de cuyo nombre no quiero acordarme, no hace mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. ")
    textoriginal_2 = Wordbyword (language ="Ingelesa", text = "I can't believe the news today Oh, I can't close my eyes and make it go away. How long must we sing this song?")
    textoriginal_3 = Wordbyword (language ="Euskera", text = "Hala bazan ala ez bazan, sar dadila kalabazan eta atera dadila Foruko plazan ")
    
    wordbyword_repository = WordbywordRepository(database_path)
    
    wordbyword_repository.save(textoriginal_1)
    wordbyword_repository.save(textoriginal_2)
    wordbyword_repository.save(textoriginal_3)

   
    Activity_1 = Activity (id="act-1", user_id="user-1", route ="word-by-word", name = "HITZEZ HITZ")
    Activity_2 = Activity (id="act-2", user_id="user-2", route ="play-word-by-word", name = "IRAKUR-LAGUN")
    Activity_3 = Activity (id="act-3", user_id="user-1", route ="count-letters", name = "SILABAK ZENBATU")
    Activity_4 = Activity (id="act-4", user_id="user-2", route ="color-memory", name = "MARGOTU ZURE MEMORIA")
    Activity_5 = Activity (id="act-5", user_id="user-1", route ="cards-game", name = "BIKOTE JOLASA")
    Activity_6 = Activity (id="act-6", user_id="user-2", route ="chained-words", name = "HITZ KATEATUAK")

    activity_repository = ActivityRepository(database_path)
   
    activity_repository.save(Activity_1)
    activity_repository.save(Activity_2)
    activity_repository.save(Activity_3)
    activity_repository.save(Activity_4)
    activity_repository.save(Activity_5)
    activity_repository.save(Activity_6)


    user_repository = UserRepository(database_path)

    user1 = User (id='user-1', name='Ander', password='0000')
    user2 = User (id='user-2', name='Alba', password='0000')

    user_repository.save(user1)
    user_repository.save(user2)

    #countletters
    word1 = Countletters (id ='1', word='klariona', img='https://i.ibb.co/KrTZs1M/klariona.png', letters='8', syllables='3')
    word2 = Countletters (id ='2', word='platera', img='https://i.ibb.co/6PrS7f6/platera.png', letters='7', syllables='3')
    word3 = Countletters (id ='3', word='globoa', img='https://i.ibb.co/HD3vSvV/globoa.png', letters='6', syllables='3')
    word4 = Countletters (id ='4', word='kablea', img='https://i.ibb.co/L02r9W6/kablea.png', letters='6', syllables='3')
    word5 = Countletters (id ='5', word='palmera', img='https://i.ibb.co/3mkTm0j/palmera.png', letters='7', syllables='3')
    word6 = Countletters (id ='6', word='termometroa', img='https://i.ibb.co/DwY3ttw/termometro.png', letters='11', syllables='5')
    word7 = Countletters (id ='7', word='kalkulagailua', img='https://i.ibb.co/yP79QW7/kalkulagailua.png', letters='13', syllables='6')
    word8 = Countletters (id ='8', word='galtzerdiak', img='https://i.ibb.co/Vv2zrCv/galtzerdiak.png', letters='11', syllables='4')
    word9 = Countletters (id ='9', word='prakak', img='https://i.ibb.co/JHNMkhG/prakak2.png', letters='6', syllables='2')
    word10 = Countletters (id ='10', word='tigrea', img='https://i.ibb.co/th5yYwc/tigrea.png', letters='6', syllables='3')
    
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


    phrase1 = Chainedword  (id ='1', level ='easy', question='GaurMartarenurtebetetzeada', answer='Gaur Martaren urtebetetzea da')
    phrase2 = Chainedword  (id ='2', level ='easy', question='Poliziaklapurraatxilotuzuen', answer='Poliziak lapurra atxilotu zuen')
    phrase3 = Chainedword  (id ='3', level ='easy', question='Lucíahaserredago', answer='Lucía haserre dago')
    phrase4 = Chainedword  (id ='4', level ='easy', question='Albertoklasterketairabazidu', answer='Albertok lasterketa irabazi du')
    phrase5 = Chainedword  (id ='5', level ='mediun', question='Printzesaprintzearekingazteluanbizida', answer='Printzesa printzearekin gazteluan bizi da')
    phrase6 = Chainedword  (id ='6', level ='mediun', question='Markoriezzaizkiobarazkiakgustatzen', answer='Markori ez zaizkio barazkiak gustatzen')
    phrase7 = Chainedword  (id ='7', level ='mediun', question='Miguelnegarrezaridaeroridelako', answer='Miguel negarrez ari da erori delako')
    phrase8 = Chainedword  (id ='8', level ='hard', question='Lucasek partidako azken gola sartu zuen', answer='Lucasek partidako azken gola sartu zuen')
    phrase9 = Chainedword  (id ='9', level ='hard', question='Turistekezzekitenherrikoelizanonzegoen', answer='Turistek ez zekiten herriko eliza non zegoen')
    phrase10 = Chainedword (id ='10',level ='hard', question='AmaketaaitakSararilotarakoipuinbatirakurrizioten', answer='Amak eta aitak Sarari lotarako ipuin bat irakurri zioten.')
    
    chainedword_repository = ChainedwordRepository(database_path)

    chainedword_repository.save(phrase1)
    chainedword_repository.save(phrase2)
    chainedword_repository.save(phrase3)
    chainedword_repository.save(phrase4)
    chainedword_repository.save(phrase5)
    chainedword_repository.save(phrase6)
    chainedword_repository.save(phrase7)
    chainedword_repository.save(phrase8)
    chainedword_repository.save(phrase9)
    chainedword_repository.save(phrase10)

    print("Base de datos inicializada en" + database_path)

main()
