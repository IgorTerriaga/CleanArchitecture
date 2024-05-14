import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .user_repository import UserRepository


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensitive test")
def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 23
    users_repository = UserRepository()
    users_repository.insert_user(mocked_first_name, last_name=mocked_last_name, age=mocked_age)

    sql  = f'SELECT * FROM users where age = {mocked_age}'
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]
    assert registry.age == mocked_age

    connection.execute(text(f'DELETE FROM users WHERE id= {registry.id}'))
    connection.commit()


@pytest.mark.skip(reason="Sensitive test")
def test_select_user():
    mocked_first_name = "first_2"
    mocked_last_name = "last_2"
    mocked_age = 13
    sql = '''INSERT INTO users (first_name, last_name, age) VALUES 
    ('{}', '{}', {})'''.format(mocked_first_name, mocked_last_name, mocked_age)
    connection.execute(text(sql))
    connection.commit()
    users_repository = UserRepository()
    response = users_repository.select_user(mocked_first_name)
    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age
    connection.execute(text(f'DELETE FROM users WHERE id= {response[0].id}'))
    connection.commit()
