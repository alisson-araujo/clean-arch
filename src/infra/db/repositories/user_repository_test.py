import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .user_repository import UserRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensitive test")
def test_insert_user():
    mocked_first_name = "Homer"
    mocked_last_name = "Simpson"
    mocked_age = 34

    user_repository = UserRepository()
    user_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    query = """
        SELECT * FROM users 
        WHERE first_name='{}'
        AND last_name='{}'
        AND age='{}';""".format(
        mocked_first_name,
        mocked_last_name,
        mocked_age,
    )
    response = connection.execute(text(query))
    registry = response.fetchall()[0]

    print(registry)

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f"""DELETE FROM users WHERE id = {registry.id}"""))
    connection.commit()


def test_select_user():
    mocked_first_name = "Tite"
    mocked_last_name = "Kubo"
    mocked_age = 56

    query = """
        INSERT INTO users (first_name, last_name, age) VALUES ('{}', '{}', '{}')
    """.format(
        mocked_first_name, mocked_last_name, mocked_age
    )

    connection.execute(text(query))
    connection.commit()

    user_repository = UserRepository()
    response = user_repository.select_user(mocked_first_name)

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age
