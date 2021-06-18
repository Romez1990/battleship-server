from tornado.websocket import WebSocketHandler

from src.ioc_container import service
from src.connection.models import (
    PlayerConnection,
)
from src.battlefield import GameShip
from src.questions import (
    QuestionService,
)
from .game_session_service import GameSessionService
from .models import (
    Session,
    MoveData,
    ShotResult,
    GetShotResult,
    AnswerData,
    AnswerResult,
)


@service
class GameSessionServiceImpl(GameSessionService):
    def __init__(self, questions: QuestionService) -> None:
        self.__questions = questions
        self.__sessions: list[Session] = []

    def add_session(self, player1: PlayerConnection, player2: PlayerConnection) -> None:
        self.__sessions.append(Session(player1, player2))

    def go(self, socket: WebSocketHandler, move_data: MoveData) -> ShotResult:
        player, enemy = self.__find_session(socket)

        shot = move_data.coordinates
        hit_ships = enemy.ships.filter(lambda ship: ship.collides(shot))
        if len(hit_ships) == 0:
            return ShotResult(hit=False)

        player.current_question = self.__questions.get_question()
        player.current_question_model = player.current_question.to_model()

        hit_ship: GameShip = hit_ships[0]
        hit_ship.hit(shot)

        enemy.socket.write_message(GetShotResult(coordinates=shot).json())

        if not hit_ship.destroyed:
            return ShotResult(hit=True, question=player.current_question_model)
        enemy.remove_ship(hit_ship)
        if len(enemy.ships) != 0:
            return ShotResult(hit=True, destroyed=True, destroyed_ship=hit_ship.to_ship(),
                              question=player.current_question_model)
        return ShotResult(hit=True, destroyed=True, destroyed_ship=hit_ship.to_ship(), won=True,
                          question=player.current_question_model)

    def __find_session(self, socket: WebSocketHandler) -> tuple[PlayerConnection, PlayerConnection]:
        for session in self.__sessions:
            if session.player1.socket is socket or session.player2.socket is socket:
                return session.sort(socket)

    def answer(self, socket: WebSocketHandler, answer_data: AnswerData) -> AnswerResult:
        player, enemy = self.__find_session(socket)
        right = player.current_question.answers[0] == player.current_question_model.answers[answer_data.answer_index]
        result = AnswerResult(right=right)
        enemy.socket.write_message(result.json())
        return result
