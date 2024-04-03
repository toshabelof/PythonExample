from abc import ABC
from datetime import datetime


class BaseModel(ABC):
    def __init__(
        self, isn: int, create_date: datetime, update_date: datetime, user_modify: int
    ):
        self.isn = isn
        self.create_date = create_date
        self.update_date = update_date
        self.user_modify = user_modify
