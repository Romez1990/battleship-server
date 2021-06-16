from typing import (
    Optional,
)
from pydantic import BaseModel

from src.sockets import Message


class Player(BaseModel):
    first_name: str
    last_name: str


class ConnectionCode(BaseModel):
    code: str


class PlayerData(BaseModel):
    player: Player
    connection_code: Optional[str]


class CreateGameMessage(Message[PlayerData]):
    message_type = 'create_game'
    data_type = PlayerData


class ConnectionToGameResult(BaseModel):
    result: bool
