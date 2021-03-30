import json
from typing import Union

from pydantic import BaseModel

from src.ioc_container import service
from .create_game_service import CreateGameService


class GameStartJson(BaseModel):
    code = int


@service
class CreateGameServiceImpl(CreateGameService):
    code_game = []

    def get_game_code(self) -> Union[str, bytes, dict]:
        if len(self.code_game) == 0:
            self.code_game.append(1)
            return {'code_game': self.code_game[0]}
        else:
            code = self.code_game[-1] + 1
            self.code_game.append(code)
            return {'code_game': code}


    def post_game_code(self, json_data):
        print(json_data)
        json_ = json.loads(json_data)
        data = GameStartJson.parse_raw(json_data)
        code = data.code
        print(f'Your code is: {code}')
