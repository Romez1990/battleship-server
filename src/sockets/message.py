from pydantic import BaseModel
from typing import (
    Type,
    TypeVar,
    Generic,
)

T = TypeVar('T', bound=BaseModel)


class MessageModel(BaseModel):
    message_type: str
    data: dict


class Message(Generic[T]):
    message_type: str
    data_type: Type[T]

    @classmethod
    def parse_raw(cls, text: str) -> T:
        message = MessageModel.parse_raw(text)
        if message.message_type != cls.message_type:
            raise Exception('message.message_type != cls.message_type')
        return cls.data_type(**message.data)
