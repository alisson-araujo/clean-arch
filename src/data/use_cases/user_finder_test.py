from src.infra.db.tests.users_repository import UserRepositorySpy
from .user_finder import UserFinder

def test_find():
    first_name = "paul"

    repository = UserRepositorySpy()
    user_finder = UserFinder(users_repository=repository)

    response = user_finder.find(first_name)
    print(response)
    print(repository.select_user_attributes)

    assert response['type'] == 'users'