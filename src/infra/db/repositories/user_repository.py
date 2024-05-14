from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.user import Users as UsersEntity

class UserRepository:
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int ) -> None:
        with DBConnectionHandler() as database:
            try:
                new_register = UsersEntity(first_name=first_name, last_name=last_name, age=age)
                database.sessions.add(new_register)
                database.sessions.commit()
            except Exception as exception:
                database.sessions.rollback()
                raise exception
