from .connection import DBConnectionHandler


def test_create_database_engine():
    db_connection_handler = DBConnectionHandler()

    engine = db_connection_handler.get_engine()

    assert engine is not None
    