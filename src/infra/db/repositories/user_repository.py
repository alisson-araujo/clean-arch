from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UserEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users


class UsersRepository(UsersRepositoryInterface):
    """User Repository"""

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_user = UserEntity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                )
                database.session.add(new_user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str) -> List[Users]:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session.query(UserEntity)
                    .filter(UserEntity.first_name == first_name)
                    .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception
