from tornado.websocket import WebSocketHandler
from src.ioc_container import container
from .game_session_service import GameSessionService


class GameSessionHandler(WebSocketHandler):
    def initialize(self) -> None:
        self.__game_create_websocket = container.get(GameSessionService)

    __game_create_websocket: GameSessionService

    def open(self) -> None:
        self.__game_create_websocket.open()

    def on_message(self, message) -> None:
        self.__game_create_websocket.on_message(message)

    def on_close(self) -> None:
        self.__game_create_websocket.on_close()
