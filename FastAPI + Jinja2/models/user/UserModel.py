from datetime import date, datetime

import testData
from models.BaseModel import BaseModel


class User(BaseModel):
    def __init__(
        self,
        isn: int,
        login: str,
        password: str,
        fio: str,
        birthday: date,
        phone_number: str,
        email: str,
        user_modify: int,
        last_date: datetime = datetime.now(),
        reg_date: datetime = datetime.now(),
        create_date: datetime = datetime.now(),
        update_date: datetime = datetime.now(),
    ):
        super().__init__(isn, create_date, update_date, user_modify)
        self.fio = fio
        self.login = login
        self.password = password
        self.birthday = birthday
        self.phone_number = phone_number
        self.email = email
        self.reg_date = reg_date
        self.last_date = last_date

    def add(self):
        testData.userList.append(
            {
                "isn": self.isn,
                "login": self.login,
                "password": self.password,
                "fio": self.fio,
                "birthday": self.birthday,
                "phone_number": self.phone_number,
                "email": self.email,
                "reg_date": self.reg_date,
                "last_date": self.last_date,
            }
        )

    def upd(self, fio: str):
        idx = next(
            (
                index
                for (index, d) in enumerate(testData.userList)
                if d["isn"] == self.isn
            )
        )
        testData.userList[idx] = {
            "fio": fio,
            "login": self.login,
            "password": self.password,
            "birthday": self.birthday,
            "phone_number": self.phone_number,
            "email": self.email,
            "reg_date": self.reg_date,
            "last_date": self.last_date,
        }


def get_users() -> list[User]:
    users = []
    for data in testData.userList:
        users.append(
            User(
                data["isn"],
                data["login"],
                data["password"],
                data["fio"],
                data["birthday"],
                data["phone_number"],
                data["email"],
                data["reg_date"],
                data["last_date"],
            )
        )
    return users


def get_user_by_id(isn: int) -> User:
    user = next((users for users in testData.userList if int(users["isn"]) == isn))
    return User(
        isn=user["isn"],
        login=user["login"],
        password=user["password"],
        fio=user["fio"],
        birthday=datetime.strptime(user["birthday"], "%d-%m-%Y").date(),
        phone_number=user["phone_number"],
        email=user["email"],
        user_modify=user["user_modify"],
        reg_date=datetime.strptime(user["reg_date"], "%d-%m-%Y %H:%M:%S"),
        last_date=datetime.strptime(user["last_date"], "%d-%m-%Y %H:%M:%S"),
    )


def delete_user_by_id(isn: int):
    user = next((users for users in testData.userList if int(users["isn"]) == isn))
    testData.userList.remove(user)
