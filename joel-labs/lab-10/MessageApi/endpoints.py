from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from models.message_model import MessageModel
from container import Container
from message_repository import MessageRepository
from message_sender import MessageSender

router = APIRouter()


@router.get('/messages/{id}', status_code=200)
@inject
async def get_message(id: int, message_repository: MessageRepository = Depends(Provide[Container.message_repository_provider])):
    msg = message_repository.get_message(id=id)
    return msg


@router.post('/messages', status_code=201)
@inject
async def save_messages(message: MessageModel,
                        message_sender: MessageSender = Depends(
                            Provide[Container.message_sender_provider]),
                        message_repository: MessageRepository = Depends(
                            Provide[Container.message_repository_provider])):
    data = message.json()
    msg = data["message"]
    
    _id = message_repository.save_message(message=msg)
    message_sender.send_message(message=msg)
    
    return _id