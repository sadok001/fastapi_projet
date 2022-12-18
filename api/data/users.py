from dataclasses import dataclass

from pydantic import EmailStr

from infrastructure.utils.validations import Validations


@dataclass
class CreateUser(Validations):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    confirm_password: str

    def validate_password(self, value, **_):
        if value != self.confirm_password:
            raise ValueError("invalid password")

        return value

@dataclass
class CreatedUser:
    first_name: str
    last_name: str
    email: EmailStr

@dataclass
class InactiveUser(Validations):
    token: int

    def validate_token(self, value, **_):
        if value < 1000 or value > 9999:
            raise ValueError("invalid token")

        return value
