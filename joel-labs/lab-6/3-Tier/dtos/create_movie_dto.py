from pydantic import BaseModel


class CreateMovieDto(BaseModel):
    name: str
    description: str
    imdb_url: str
