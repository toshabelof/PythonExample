from datetime import datetime

import testData
from models.BaseModel import BaseModel
from models.consumable.ConsumableModel import Consumable


class Product(BaseModel):
    def __init__(
        self,
        isn: int,
        name: str,
        unit: str,
        weight: str,
        width: str,
        height: int,
        length: int,
        cost_price: int,
        selling_price: int,
        consumables: list[Consumable],
        user_modify: int,
        create_date: datetime = datetime.now(),
        update_date: datetime = datetime.now(),
    ):
        super().__init__(isn, create_date, update_date, user_modify)
        self.name = name
        self.unit = unit
        self.weight = weight
        self.width = width
        self.height = height
        self.length = length
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.consumables = consumables

    def add(self):
        testData.productsList.append(
            {
                "isn": self.isn,
                "name": self.name,
                "unit": self.unit,
                "weight": self.weight,
                "width": self.width,
                "height": self.height,
                "length": self.length,
                "cost_price": self.cost_price,
                "selling_price": self.selling_price,
                "consumables": self.consumables,
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
            "unit": self.unit,
            "weight": self.weight,
            "width": self.width,
            "height": self.height,
            "length": self.length,
            "cost_price": self.cost_price,
            "selling_price": self.selling_price,
            "consumables": self.consumables,
            "user_modify": self.user_modify,
            "create_date": self.create_date,
            "update_date": self.update_date,
        }


def get_products() -> list[Product]:
    products = []
    for data in testData.productsList:
        products.append(
            Product(
                data["isn"],
                data["name"],
                data["unit"],
                data["weight"],
                data["width"],
                data["height"],
                data["length"],
                data["cost_price"],
                data["selling_price"],
                data["consumables"],
                data["user_modify"],
                data["create_date"],
                data["update_date"],
            )
        )
    return products


def get_product_by_id(isn: int) -> Product:
    product = next(
        (product for product in testData.productsList if int(product["isn"]) == isn)
    )
    consumables = []
    for consumable in product["consumables"]:
        consumables.append(
            Consumable(
                consumable["isn"],
                consumable["name"],
                consumable["count"],
                consumable["unit"],
                consumable["purchase_price"],
                consumable["user_modify"],
                consumable["create_date"],
                consumable["update_date"],
            )
        )

    return Product(
        product["isn"],
        product["name"],
        product["unit"],
        product["weight"],
        product["width"],
        product["height"],
        product["length"],
        product["cost_price"],
        product["selling_price"],
        consumables,
        product["user_modify"],
        product["create_date"],
        product["update_date"],
    )


# if __name__ == "__main__":
#     print(get_product_by_id(1).consumables[1].name)
