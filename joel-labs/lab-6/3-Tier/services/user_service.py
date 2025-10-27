from injector import inject

from models.user import User
from database.repositories.user_repository import UserRepository


class UserService:
    @inject
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def get_all(self) -> list[User]:
        return self.__repository.get_all()

    def create_user(self, user: User):
        self.__repository.create_user(user)
