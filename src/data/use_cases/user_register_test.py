from src.infra.db.tests.users_repository import UserRepositorySpy
from .user_register import UserRegister


def test_register():
    first_name = "Lucas"
    last_name = "Santos"
    age = 25

    user_repository = UserRepositorySpy()
    user_register = UserRegister(user_repository)

    response = user_register.register(first_name, last_name, age)
    print(user_repository.insert_user_attributes)

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]
