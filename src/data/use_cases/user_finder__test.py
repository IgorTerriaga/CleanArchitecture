from src.infra.db.tests.user_repository import UserRepositorySpy
from .user_finder import UserFinder


def test_user_finder():
    first_name = 'ss'
    repo: UserRepositorySpy = UserRepositorySpy()
    user_finder = UserFinder(repo)
    response = user_finder.find(first_name)
    assert response["count"] == 2


def test_find_error_in_valid_name():
    first_name = 's12s'
    repo: UserRepositorySpy = UserRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
    except Exception as exception:
        assert  str(exception) == 'Nome inválido para a busca'


def test_find_error_in_long_name():
    first_name = 'sfdsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'
    repo: UserRepositorySpy = UserRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
    except Exception as exception:
        assert  str(exception) == 'Nome muito grande para a busca'
