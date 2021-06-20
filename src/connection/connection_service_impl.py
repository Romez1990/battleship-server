from random import randint
from tornado.websocket import WebSocketHandler
from pydantic import BaseModel

from src.ioc_container import service
from src.game_session import GameSessionService
from .connection_service import ConnectionService
from .code_counter import CodeCounter
from .models import (
    PlayerConnectionData,
    ConnectionCode,
    ConnectionToGameResult,
    PlayerConnection,
)


@service
class ConnectionServiceImpl(ConnectionService):
    def __init__(self, code_counter: CodeCounter, session: GameSessionService) -> None:
        self.__code_counter = code_counter
        self.__session = session
        self.__connections: dict[str, PlayerConnection] = {}

    def connect(self, socket: WebSocketHandler, player_data: PlayerConnectionData) -> BaseModel:
        if player_data.connection_code is None:
            return self.__create_game(socket, player_data)
        return self.__connect_to_game(socket, player_data)

    def __create_game(self, socket: WebSocketHandler, player_data: PlayerConnectionData) -> ConnectionCode:
        code = self.__get_code()
        self.__connections[code] = PlayerConnection(socket, player_data)
        return ConnectionCode(code=code)

    def __get_code(self) -> str:
        while True:
            code = self.__code_counter.get_code()
            if code not in self.__connections:
                return code

    def __connect_to_game(self, socket: WebSocketHandler, player_data: PlayerConnectionData) -> ConnectionToGameResult:
        if player_data.connection_code not in self.__connections:
            return ConnectionToGameResult(is_connected=False, go=False)
        player_connection = self.__connections.pop(player_data.connection_code)

        self.__session.add_session(player_connection, PlayerConnection(socket, player_data))

        player_goes_first = bool(randint(0, 1))
        result_for_enemy = ConnectionToGameResult(is_connected=True, enemy=player_data.player, go=not player_goes_first)
        player_connection.socket.write_message(result_for_enemy.json())
        return ConnectionToGameResult(is_connected=True, enemy=player_connection.player,
                                      go=player_goes_first)

    def remove_socket_if_exists(self, socket: WebSocketHandler) -> None:
        for code, player_connection in self.__connections.items():
            if player_connection.socket is socket:
                del self.__connections[code]
                break
