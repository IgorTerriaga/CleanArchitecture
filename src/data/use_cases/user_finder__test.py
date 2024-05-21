from src.infra.db.tests.user_repository import UserRepositorySpy
from .user_finder import UserFinder


def test_user_finder():
    first_name = 'ss'
    repo: UserRepositorySpy = UserRepositorySpy()
    user_finder = UserFinder(repo)
    response = user_finder.find(first_name)
    assert response["count"] == 2
