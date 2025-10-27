from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey
from core.entities.movie import Movie
from database.mappings.mapping import Mapping


class MovieMapping(Mapping):
    def create_table(self, metadata: MetaData) -> Table:
        return Table(
            "movie",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String),
            Column("description", String),
            Column("imdb_url", String),
        )

    entity = Movie
