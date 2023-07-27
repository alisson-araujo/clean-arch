from src.infra.db.tests.users_repository import UserRepositorySpy
from .user_finder import UserFinder


def test_find():
    first_name = "paul"

    repository = UserRepositorySpy()
    user_finder = UserFinder(users_repository=repository)

    response = user_finder.find(first_name)

    assert response["type"] == "Users"


def test_find_error_valid_name():
    first_name = "paul1"

    repository = UserRepositorySpy()
    user_finder = UserFinder(users_repository=repository)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exc:
        assert str(exc) == "Invalid name"


def test_user_not_found():
    class UserRepositoryError(UserRepositorySpy):
        def select_user(self, first_name: str):
            return []

    first_name = "paul"

    repository = UserRepositoryError()
    user_finder = UserFinder(users_repository=repository)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exc:
        assert str(exc) == "User not found"
