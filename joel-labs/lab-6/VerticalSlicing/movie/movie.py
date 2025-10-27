from dataclasses import dataclass


@dataclass
class Movie:
    name: str
    description: str
    imdb_url: str
    id: int = None
