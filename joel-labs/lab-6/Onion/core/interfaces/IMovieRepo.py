from abc import ABC, abstractmethod
from core.entities.movie import Movie

class IMovieRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Movie]: ...

    @abstractmethod
    def create_movie(self, movie: Movie) -> None: ...

