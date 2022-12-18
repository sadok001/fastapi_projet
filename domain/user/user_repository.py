from abc import ABC, abstractmethod
from typing import List, Optional

from pydantic import EmailStr

from domain.user.user import User


class UserRepository(ABC):
    """UserRepository defines a repository interface for User entity."""

    @abstractmethod
    def create(self, user: User) -> bool:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: EmailStr) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def update(self, email: EmailStr, data: dict) -> bool:
        raise NotImplementedError
