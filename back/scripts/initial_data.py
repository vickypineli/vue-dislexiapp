def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.activity import Activity, ActivityRepository
    from src.domain.wordbyword import WordbywordRepository, Wordbyword

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)
    info_repository.save(Info(app_name="irla-kurri"))

    ## Activities

    # Activity1 = Activity(id="1", name="wordbyword")

    # activity_repository = ActivityRepository(database_path)
    # activity_repository.save(Activity1)

    # wordbyword

    Textoriginal = Wordbyword(
        text = "A cien cañones por banda, viento en popa a toda vela"
    )

    wordbyword_repository = WordbywordRepository(database_path)
    wordbyword_repository.save(Textoriginal)

    print("Base de datos inicializada en" + database_path)


main()
