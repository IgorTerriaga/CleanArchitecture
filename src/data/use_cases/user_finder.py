# pylint: disable=broad-exception-raised
from typing import Dict

from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UserRepositoryInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self._users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        if not first_name.isalpha():
            raise Exception('Nome inválido para a busca')
        if len(first_name) > 18:
            raise Exception('Nome muito grande para a busca')

        users = self._users_repository.select_user(first_name=first_name)
        if not users:
            raise Exception('Usuário não encontrado')
        response = {
            "type": "Users",
            "count": len(users),
            "users": users
        }
        return response
