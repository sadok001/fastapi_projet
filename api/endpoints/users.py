from datetime import datetime

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import EmailStr

from api.data import users
from domain.user import user_exception
from domain.user.user import User
from infrastructure.database.persistence.user_respository_impl import \
    MongoUserRepository
from infrastructure.notification.email_notification import \
    send_new_account_email

router = APIRouter()
user_repository = MongoUserRepository()


@router.post("/", response_model=users.CreatedUser)
def create_user(new_user: users.CreateUser):
    """Create new User

    Args:
        new_user (users.CreateUser): payload schema

    Raises:
        user_exception.UserEmailAlreadyExistsError
    """
    user = user_repository.find_by_email(email=new_user.email)
    if user:
        raise user_exception.UserEmailAlreadyExistsError()

    user = User(
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        email=new_user.email
    )

    user.set_password(new_user.password)
    user.set_code()

    user_repository.create(user=user)

    send_new_account_email(
        email=user.email, username=user.full_name, code=user.get_code())

    return users.CreatedUser(
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        email=new_user.email
    )


@router.put("/{user_email}", response_model=users.ActivatedUser)
def activate_user(user_email: EmailStr, inactive_user: users.InactiveUser):
    """Activate user

    Args:
        user_email (EmailStr): user email
        inactive_user (users.InactiveUser): payload schema

    Raises:
        user_exception.UserNotFoundError
        user_exception.InvalideUserCodeError
    """
    user = user_repository.find_by_email(email=user_email)

    if not user:
        raise user_exception.UserNotFoundError()

    if user['_code'] != inactive_user.token:
        raise user_exception.InvalideUserCodeError()

    # get difference
    delta = datetime.now() - user['_code_timestamp']
    diff_min = delta.total_seconds()/60

    if diff_min > 1:
        raise user_exception.InvalideUserCodeError()

    user['active'] = True

    user_repository.update(email=user_email, data=user)

    return users.ActivatedUser(
        first_name=user['first_name'],
        last_name=user['last_name'],
    )
