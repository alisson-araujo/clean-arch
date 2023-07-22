# pylint: disable=missing-class-docstring
from abc import ABC, abstractmethod
from typing import Dict

class UserFinder(ABC):

    @abstractmethod
    def find_user(self, first_name: str) -> Dict:
        pass
