from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey
from pricing.pricing import Pricing
from common.database.mapping import Mapping


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
