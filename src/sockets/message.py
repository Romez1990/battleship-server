from typing import (
    Optional,
    Type,
    TypeVar,
    Generic,
)
from pydantic import BaseModel

from .message_error import MessageError

T = TypeVar('T', bound=BaseModel)


class MessageModel(BaseModel):
    message_type: str
    data: Optional[dict]


class Message(Generic[T]):
    message_type: str
    data_type: Type[T]

    @classmethod
    def parse_raw(cls, text: str) -> T:
        message = MessageModel.parse_raw(text)
        if message.message_type != cls.message_type:
            raise MessageError('message.message_type != cls.message_type')
        if cls.data_type is None:
            return None
        return cls.data_type(**message.data)
