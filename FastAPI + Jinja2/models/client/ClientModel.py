from datetime import datetime

import testData
from models.BaseModel import BaseModel


class Client(BaseModel):
    def __init__(
            self,
            isn: int,
            name: str,
            phone_number: str,
            email: str,
            birthday: str,
            country: str,
            zip: int,
            address: str,
            card: str,
            discount: int,
            user_modify: int,
            create_date: datetime = datetime.now(),
            update_date: datetime = datetime.now(),
    ):
        super().__init__(isn, create_date, update_date, user_modify)
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.birthday = birthday
        self.country = country
        self.zip = zip
        self.address = address
        self.card = card
        self.discount = discount

    def add(self):
        testData.clientsList.append(
            {
                "isn": self.isn,
                "last_name": self.last_name,
                "first_name": self.first_name,
                "birthday": self.birthday,
                "phone_number": self.phone_number,
                "discount": self.discount,
            }
        )

    def upd(self):
        idx = next(
            (
                index
                for (index, d) in enumerate(testData.clientsList)
                if d["isn"] == self.isn
            )
        )
        testData.clientsList[idx] = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "phone_number": self.phone_number,
            "discount": self.discount,
        }


def get_clients() -> list[Client]:
    clients = []
    for data in testData.clientsList:
        clients.append(
            Client(
                data["isn"],
                data["last_name"],
                data["first_name"],
                data["birthday"],
                data["phone_number"],
                data["discount"],
                data["user_modify"],
            )
        )
    return clients


def get_client_by_id(isn: int) -> Client:
    client = next(
        (client for client in testData.clientsList if int(client["isn"]) == isn)
    )
    return Client(
        client["isn"],
        client["last_name"],
        client["first_name"],
        client["birthday"],
        client["phone_number"],
        client["discount"],
    )
