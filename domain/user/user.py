from datetime import datetime
from random import randint

from pydantic import EmailStr

from infrastructure.utils.hasher import Hasher


class User:
    """User represents the collection of users as an entity."""

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: EmailStr,
    ):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email

    @property
    def full_name(self):
        return self.first_name+" "+self.last_name

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, User):
            return False

        return self.id == o.id

    def get_password(self) -> str:
        return self._password

    def set_password(self, password: str) -> None:
        self._password = Hasher.get_password_hash(password)

    def get_code(self):
        return self._code

    def set_code(self) -> None:
        self._code = randint(1000, 9999)
        self._code_timestamp = datetime.now()

    def get_code_timestamp(self):
        return self._code_timestamp
