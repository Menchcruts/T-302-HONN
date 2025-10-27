from contextlib import AbstractContextManager
from typing import Callable

from injector import inject
from sqlalchemy.orm import Session
from models.movie import Movie


class MovieRepository:
    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_all(self) -> list[Movie]:
        with self.__session_factory() as session:
            return session.query(Movie).all()

    def create_movie(self, movie: Movie) -> None:
        with self.__session_factory() as session:
            session.add(movie)
            session.commit()
            session.refresh(movie)
