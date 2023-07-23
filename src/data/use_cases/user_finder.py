from typing import Dict
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    def find(self, user_id: int) -> Dict:
        ...