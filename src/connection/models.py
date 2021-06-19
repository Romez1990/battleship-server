from typing import (
    Optional,
)
from tornado.websocket import WebSocketHandler
from pydantic import BaseModel

from src.battlefield import (
    Vector,
    Ship,
    GameShip,
)
from src.questions import (
    Question,
    QuestionModel,
)
from src.sockets import Message
from src.immutable_collections import List


class Player(BaseModel):
    first_name: str
    last_name: str


class ConnectionCode(BaseModel):
    message_type = 'connection_code'
    code: str


class PlayerConnectionData(BaseModel):
    player: Player
    ships: list[Ship]
    connection_code: Optional[str]


class CreateGameMessage(Message[PlayerConnectionData]):
    message_type = 'create_game'
    data_type = PlayerConnectionData


class ConnectionToGameResult(BaseModel):
    message_type = 'game_connected'
    is_connected: bool
    enemy: Optional[Player]
    go: bool


class PlayerConnection:
    def __init__(self, socket: WebSocketHandler, player_data: PlayerConnectionData) -> None:
        self.socket = socket
        self.__player = player_data.player
        self.__ships: List[GameShip] = List(player_data.ships).map(lambda ship: GameShip(ship))
        self.current_question: Optional[Question] = None
        self.current_question_model: Optional[QuestionModel] = None

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def ships(self) -> List[GameShip]:
        return self.__ships

    def remove_ship(self, ship: GameShip) -> None:
        self.__ships = self.__ships.remove(ship)
