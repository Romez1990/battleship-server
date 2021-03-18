from tornado.web import RequestHandler

from src.ioc_container import container
from .create_game_service import CreateGameService


class CreateGameHandler(RequestHandler):
    def initialize(self) -> None:
        self.__create_game = container.get(CreateGameService)

    __create_game: CreateGameService

    def get(self) -> None:
        code = self.__create_game.get_game_code()
        self.write(code)
