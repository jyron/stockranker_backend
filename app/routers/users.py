from fastapi import APIRouter

from app.auth.usermanager import auth_backend, fastapi_users
from app.models.users import User
from app.schemas.users import UserCreate, UserRead, UserUpdate

users_router = fastapi_users.get_users_router(UserRead, UserUpdate)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)
reset_password_router = fastapi_users.get_reset_password_router()
verify_router = fastapi_users.get_verify_router(UserRead)
auth_router = fastapi_users.get_auth_router(auth_backend)

user_router = APIRouter()

user_router.include_router(users_router, prefix="/users", tags=["users"])
user_router.include_router(register_router, prefix="/auth", tags=["auth"])
user_router.include_router(reset_password_router, prefix="/auth", tags=["auth"])
user_router.include_router(verify_router, prefix="/auth", tags=["auth"])
user_router.include_router(auth_router, prefix="/auth/jwt", tags=["auth"])
