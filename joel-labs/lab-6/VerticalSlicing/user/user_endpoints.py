from fastapi import APIRouter, Depends, status

from common.infrastructure.get_service import get_service
from user.user_service import UserService
from user.create_user_dto import CreateUserDto

from user.user import User

router = APIRouter(
    prefix='/users',
)


@router.get('/')
def get_users(user_service: UserService = Depends(get_service(UserService))):
    return user_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: CreateUserDto, user_service: UserService = Depends(get_service(UserService))):
    user = User(
        name=request.name,
        email=request.email,
        phone_number=request.phone_number
    )

    user_service.create_user(
        user
    )

    return user
