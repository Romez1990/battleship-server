from tornado.websocket import WebSocketHandler

from src.ioc_container import container
from src.game_session import GameSessionService
from .connection_service import ConnectionService
from .models import (
    CreateGameMessage,
)
from src.game_session.models import MoveMessage, AnswerMessage, EnemyGoMessage
from src.sockets.message_error import MessageError

counter = 0


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
            self.write_message(result.json())
        except MessageError:
            try:
                move_data = MoveMessage.parse_raw(message)
                result = self.__session.go(self, move_data)
                self.write_message(result.json())
            except MessageError:
                try:
                    answer_data = AnswerMessage.parse_raw(message)
                    result = self.__session.answer(self, answer_data)
                    self.write_message(result.json())
                except MessageError:
                    EnemyGoMessage.parse_raw(message)
                    self.__session.enemy_go(self)

    def on_close(self) -> None:
        global counter
        print(f'closed {counter}')
        counter += 1
        # self.__connection.remove_socket_if_exists(self)
        # self.__session.remove_session_if_exists(self)
