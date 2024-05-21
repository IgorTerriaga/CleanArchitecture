from src.infra.db.repositories.user_repository import UserRepository
from .user_finder import UserFinder


def test_user_finder():
    repo = UserRepository()
    user_finder = UserFinder(repo)
