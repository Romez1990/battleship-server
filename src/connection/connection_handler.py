from tornado.websocket import WebSocketHandler

from src.ioc_container import container
from src.game_session import GameSessionService
from .connection_service import ConnectionService
from .models import (
    CreateGameMessage,
)
from src.game_session.models import MoveMessage, AnswerMessage
from src.sockets.message_error import MessageError


class ConnectionHandler(WebSocketHandler):
    def initialize(self) -> None:
        self.__connection = container.get(ConnectionService)
        self.__session = container.get(GameSessionService)

    __connection: ConnectionService
    __session: GameSessionService

    def open(self) -> None:
        pass

    def on_message(self, message: str) -> None:
        try:
            player_data = CreateGameMessage.parse_raw(message)
            result = self.__connection.connect(self, player_data)
        except MessageError:
            try:
                move_data = MoveMessage.parse_raw(message)
                result = self.__session.go(self, move_data)
            except MessageError:
                move_data = AnswerMessage.parse_raw(message)
                result = self.__session.answer(self, move_data)
        self.write_message(result.json())

    def on_close(self) -> None:
        self.__connection.remove_socket_if_exists(self)
