from tornado.websocket import WebSocketHandler

from src.ioc_container import container
from .connection_service import ConnectionService
from .models import (
    CreateGameMessage,
    PlayerData,
)


class ConnectionHandler(WebSocketHandler):
    def initialize(self) -> None:
        self.__connection = container.get(ConnectionService)

    __connection: ConnectionService

    def open(self) -> None:
        pass

    def on_message(self, message: str) -> None:
        player_data = CreateGameMessage.parse_raw(message)
        result = self.__connection.connect(self, player_data)
        self.write_message(result.json())

    def on_close(self) -> None:
        self.__connection.remove_socket_if_exists(self)
