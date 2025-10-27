from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey, Date
from models.pricing import Pricing
from models.subscription import Subscription
from models.user import User
from database.mappings.mapping import Mapping
from sqlalchemy.orm import relationship


class SubscriptionMapping(Mapping):
    def create_table(self, metadata: MetaData) -> Table:
        return Table(
            "subscription",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("start_date", Date),
            Column("end_date", Date),
            Column("pricing_id", Integer, ForeignKey(
                "pricing.id"), nullable=False),
            Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
        )

    def properties(self) -> dict:
        return {
            "pricing": relationship(Pricing),
            "user": relationship(User),
        }

    entity = Subscription
