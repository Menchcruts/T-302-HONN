from abc import ABC, abstractmethod
from core.entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[User]: ...

    @abstractmethod
    def create_user(self, user: User) -> None: ...