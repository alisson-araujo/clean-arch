from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)

        users = self.__search_user(first_name)

        return {"type": "users", "count": len(users), "attributes": users}

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception("Invalid name")

        if len(first_name) > 18:
            raise Exception("Name is too long")

    def __search_user(self, first_name: str) -> List[Users]:
        users = self.__users_repository.select_user(first_name)
        if users == []:
            raise Exception("User not found")
        return users
