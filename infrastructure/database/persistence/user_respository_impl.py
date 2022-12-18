import json
from datetime import datetime
from typing import Optional

from pydantic import EmailStr

from domain.user.user import User
from domain.user.user_repository import UserRepository
from infrastructure.database.mongo_connection import db


class MongoUserRepository(UserRepository):

    def __init__(self):

        self.collection = db.user_collection

    def create(self, user: User) -> bool:
        """Create new user

        Args:
            user (User): user model

        Returns:
            bool: True if created successfully
        """

        try:
            user = user.__dict__
            user['created_at'] = datetime.now()
            self.collection.insert_one(user)
            return True
        except Exception as e:
            print("An exception occurred ::", e)
            return False

    def find_by_email(self, email: EmailStr) -> Optional[User]:
        """Find user by e-mail

        Args:
            email (EmailStr): user's email

        Returns:
            Optional[User]: return User if exists
        """

        return self.collection.find_one({"email": email})

    def update(self, email: EmailStr, data: dict) -> bool:

        try:
            self.collection.update_one(
                {"email": email},
                {"$set": data}
            )
            return True
        except Exception as e:
            print("An exception occurred ::", e)
            return False
