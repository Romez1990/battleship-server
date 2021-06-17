from typing import (
    Optional,
)
from tornado.websocket import WebSocketHandler
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
    is_connected: bool
    enemy: Optional[Player]


class PlayerConnection:
    def __init__(self, socket: WebSocketHandler, player_data: PlayerData) -> None:
        self.socket = socket
        self.player_data = player_data
