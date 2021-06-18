from typing import Optional

from tornado.websocket import WebSocketHandler
from pydantic import BaseModel

from src.battlefield import (
    Vector,
    Ship,
)
from src.connection.models import (
    PlayerConnection,
)
from src.questions import (
    QuestionModel,
)
from src.sockets import Message


class Session:
    def __init__(self, player1: PlayerConnection, player2: PlayerConnection) -> None:
        self.__player1 = player1
        self.__player2 = player2

    @property
    def player1(self) -> PlayerConnection:
        return self.__player1

    @property
    def player2(self) -> PlayerConnection:
        return self.__player2

    def sort(self, socket: WebSocketHandler) -> tuple[PlayerConnection, PlayerConnection]:
        if self.player1.socket is socket:
            return self.player1, self.player2
        return self.player2, self.player1


class MoveData(BaseModel):
    coordinates: Vector


class MoveMessage(Message[MoveData]):
    message_type = 'move'
    data_type = MoveData


class ShotResult(BaseModel):
    message_type = 'move_result'
    hit: bool
    destroyed: bool
    destroyed_ship: Optional[Ship]
    won: bool
    question: Optional[QuestionModel]


class GetShotResult(BaseModel):
    message_type = 'get_move_result'
    coordinates: Vector


class AnswerData(BaseModel):
    answer_index: int


class AnswerMessage(Message[AnswerData]):
    message_type = 'answer'
    data_type = AnswerData


class AnswerResult(BaseModel):
    message_type = 'answer_result'
    right: bool
