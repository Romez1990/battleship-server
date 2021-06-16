from tornado.websocket import WebSocketHandler
from pydantic import BaseModel

from src.ioc_container import service
from .connection_service import ConnectionService
from .code_counter import CodeCounter
from .models import (
    PlayerData,
    ConnectionCode,
    ConnectionToGameResult,
    PlayerConnection,
)


@service
class ConnectionServiceImpl(ConnectionService):
    def __init__(self, code_counter: CodeCounter) -> None:
        self.__code_counter = code_counter
        self.__connections: dict[str, PlayerConnection] = {}

    def connect(self, socket: WebSocketHandler, player_data: PlayerData) -> BaseModel:
        if player_data.connection_code is None:
            return self.__create_game(socket, player_data)
        return self.__connect_to_game(player_data)

    def __create_game(self, socket: WebSocketHandler, player_data: PlayerData) -> ConnectionCode:
        code = self.__get_code()
        self.__connections[code] = PlayerConnection(socket, player_data)
        return ConnectionCode(code=code)

    def __get_code(self) -> str:
        while True:
            code = self.__code_counter.get_code()
            if code not in self.__connections:
                return code

    def __connect_to_game(self, player_data: PlayerData) -> ConnectionToGameResult:
        if player_data.connection_code not in self.__connections:
            return ConnectionToGameResult(result=False)
        player_connection = self.__connections.pop(player_data.connection_code)
        result = ConnectionToGameResult(result=True)
        player_connection.socket.write_message(result.json())
        return result

    def remove_socket_if_exists(self, socket: WebSocketHandler) -> None:
        for code, player_connection in self.__connections.items():
            if player_connection.socket is socket:
                del self.__connections[code]
                break
