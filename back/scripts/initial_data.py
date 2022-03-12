def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="irla-kurri"))


if __name__ == '__main__':
    main()
