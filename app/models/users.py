"""User model."""

from fastapi_users_db_beanie import BeanieBaseUser
from beanie import Document


class User(BeanieBaseUser, Document):
    pass
