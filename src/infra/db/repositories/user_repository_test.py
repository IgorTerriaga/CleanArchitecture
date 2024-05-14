from .user_repository import UserRepository

# from src.infra.db.settings.connection import DBConnectionHandlers

def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 23
    users_repository = UserRepository()
    users_repository.insert_user(mocked_first_name, last_name=mocked_last_name, age=mocked_age)
