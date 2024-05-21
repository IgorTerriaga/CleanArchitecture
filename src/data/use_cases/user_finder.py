from typing import Dict

from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UserRepositoryInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self._users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        pass
