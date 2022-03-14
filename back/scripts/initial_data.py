
def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
    from src.domain.activity import Activity, ActivityRepository


    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="irla-kurri"))

    text1 = ("En un lugar de la Mancha de cuyo nombre no quiero acordarme ")
    text2 = ("A cien cañones por banda, viento en popa a toda vela ")
    text3 = ("Cuando ante tí se abran muchos caminos y no sepas cual recorrer")

    activity_repository = ActivityRepository(database_path)
    activity_repository.save(text1)
    activity_repository.save(text2)
    activity_repository.save(text3)
    

if __name__ == '__main__':
    main()
