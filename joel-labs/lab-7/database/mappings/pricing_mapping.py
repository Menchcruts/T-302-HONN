from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey
from models.pricing import Pricing
from database.mappings.mapping import Mapping


class PricingMapping(Mapping):
    def create_table(self, metadata: MetaData) -> Table:
        return Table(
            "pricing",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String),
            Column("price", Float),
        )

    entity = Pricing
