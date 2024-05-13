import pytest
from .connection import DBConnectionHandler
# from sqlalchemy import text

# def test_create_database_engine():
#     db_connection_handle = DBConnectionHandler()
#     engine = db_connection_handle.get_engine()

#     conn = engine.connect()
#     conn.execute(text(
#         "INSERT INTO users (first_name, last_name, age) VALUES ('ola','mundo','22')"))
#     conn.commit()


@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handle = DBConnectionHandler()
    engine = db_connection_handle.get_engine()
    assert engine is not None
