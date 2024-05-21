from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.user import Users as UsersEntity
from src.data.interfaces.users_repository import UserRepositoryInterface
from src.domain.models.users import Users


class UserRepository(UserRepositoryInterface):
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_register = UsersEntity(first_name=first_name, last_name=last_name, age=age)
                database.sessions.add(new_register)
                database.sessions.commit()
            except Exception as exception:
                database.sessions.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str) -> List[Users]:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.sessions.query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all())
                return users
            except Exception as exception:
                database.sessions.rollback()
                raise exception
