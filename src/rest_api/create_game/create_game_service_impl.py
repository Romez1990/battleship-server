from typing import Union

from src.ioc_container import service
from .create_game_service import CreateGameService


class CreateGameServiceImpl(CreateGameService):
    def get_game_code(self) -> Union[str, bytes, dict]:
        return {'code': 222}  # TODO: Create logic
