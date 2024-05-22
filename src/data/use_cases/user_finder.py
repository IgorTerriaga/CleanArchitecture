# pylint: disable=broad-exception-raised
from typing import Dict, List

from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UserRepositoryInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self._users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)
        users = self.__search_users(first_name)
        response = self.__format_response(users)
        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception('Nome inválido para a busca')
        if len(first_name) > 18:
            raise Exception('Nome muito grande para a busca')

    def __search_users(self, first_name: str) -> List:
        users = self._users_repository.select_user(first_name=first_name)
        if not users:
            raise Exception('Usuário não encontrado')
        return users

    @classmethod
    def __format_response(cls, users: List) -> Dict:
        attributes = []
        for user in users:
            attributes.append(
                {"first_name": user.first_name, "last_name": user.last_name, "age": user.age}
            )
        response = {
            "type": "Users",
            "count": len(users),
            "users": attributes
        }
        return response
