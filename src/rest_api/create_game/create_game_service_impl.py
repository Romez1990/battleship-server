import json
from typing import Union

from pydantic import BaseModel

from src.ioc_container import service
from .create_game_service import CreateGameService


class GameStartJson(BaseModel):
    code = int


@service
class CreateGameServiceImpl(CreateGameService):
    def get_game_code(self) -> Union[str, bytes, dict]:
        return {'code': 222}  # TODO: Create logic

    def post_game_code(self, json_data):
        print(json_data)
        json_ = json.loads(json_data)
        data = GameStartJson.parse_raw(json_data)
        code = data.code
        print(f'Your code is: {code}')
