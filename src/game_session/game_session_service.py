from abc import ABCMeta, abstractmethod
from tornado.websocket import WebSocketHandler

from src.connection.models import (
    PlayerConnection,
)
from .models import (
    ShotResult,
    MoveData,
    AnswerData,
    AnswerResult,
)


class GameSessionService(metaclass=ABCMeta):
    @abstractmethod
    def add_session(self, player1: PlayerConnection, player2: PlayerConnection) -> None: ...

    @abstractmethod
    def go(self, socket: WebSocketHandler, move_data: MoveData) -> ShotResult: ...

    @abstractmethod
    def answer(self, socket: WebSocketHandler, answer_data: AnswerData) -> AnswerResult: ...

    @abstractmethod
    def enemy_go(self, socket: WebSocketHandler) -> None: ...

    @abstractmethod
    def remove_session_if_exists(self, socket: WebSocketHandler) -> None: ...
