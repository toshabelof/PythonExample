import decimal
from datetime import datetime

import testData
from models.BaseModel import BaseModel


class Consumable(BaseModel):
    def __init__(
        self,
        isn: int,
        name: str,
        count: float,
        unit: str,
        purchase_price: decimal,
        user_modify: int,
        create_date: datetime = datetime.now(),
        update_date: datetime = datetime.now(),
    ):
        super().__init__(isn, create_date, update_date, user_modify)
        self.name = name
        self.count = count
        self.unit = unit
        self.purchase_price = purchase_price

    def add(self):
        testData.productsList.append(
            {
                "isn": self.isn,
                "name": self.name,
                "count": self.count,
                "unit": self.unit,
                "purchase_price": self.purchase_price,
                "user_modify": self.user_modify,
                "create_date": self.create_date,
                "update_date": self.update_date,
            }
        )

    def upd(self):
        idx = next(
            (
                index
                for (index, d) in enumerate(testData.productsList)
                if d["isn"] == self.isn
            )
        )
        testData.productsList[idx] = {
            "isn": self.isn,
            "name": self.name,
            "count": self.count,
            "unit": self.unit,
            "purchase_price": self.purchase_price,
            "user_modify": self.user_modify,
            "create_date": self.create_date,
            "update_date": self.update_date,
        }


def get_products() -> list[Consumable]:
    consumables = []
    for data in testData.productsList:
        consumables.append(
            Consumable(
                data["isn"],
                data["name"],
                data["count"],
                data["unit"],
                data["purchase_price"],
                data["user_modify"],
                data["create_date"],
                data["update_date"],
            )
        )
    return consumables


def get_product_by_id(isn: int) -> Consumable:
    consumable = next(
        (
            consumable
            for consumable in testData.productsList
            if int(consumable["isn"]) == isn
        )
    )
    return Consumable(
        consumable["isn"],
        consumable["name"],
        consumable["count"],
        consumable["unit"],
        consumable["purchase_price"],
        consumable["user_modify"],
        consumable["create_date"],
        consumable["update_date"],
    )
