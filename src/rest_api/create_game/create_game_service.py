from abc import ABCMeta, abstractmethod
from typing import Union


class CreateGameService(metaclass=ABCMeta):
    @abstractmethod
    def get_game_code(self) -> Union[str, bytes, dict]: ...

    def post_game_code(self, json_data): ...
