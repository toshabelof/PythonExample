from datetime import datetime

from testData import userList

g_id = 1


class UserModel:
    def __init__(self,
                 fio: str,
                 birthday: str,
                 phone_number: str,
                 login: str,
                 password: str,
                 id: int = None):
        self.id = ++g_id if id is None else id
        self.fio = fio
        self.birthday = birthday
        self.phone_number = phone_number
        self.login = login
        self.password = password

    def add(self):
        userList.append({
            'id': self.id,
            'fio': self.fio,
            'birthday': self.birthday,
            'phone_number': self.phone_number,
            'login': self.login,
            'password': self.password
        })
