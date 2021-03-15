from tornado.web import RequestHandler

from src.ioc_container import container
from .game_start_service import GameStartService


class GameStartHandler(RequestHandler):
    def initialize(self) -> None:
        self.__game_start = container.get(GameStartService)

    __game_start: GameStartService

    def get(self) -> None:
        text = self.__game_start.get_text()
        self.write(text)
