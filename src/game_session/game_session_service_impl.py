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
    GetEnemyShot,
    AnswerData,
    AnswerResult,
    GetEnemyAnswer,
    PlayerTurn,
)


@service
class GameSessionServiceImpl(GameSessionService):
    def __init__(self, questions: QuestionService) -> None:
        self.__questions = questions
        self.__sessions: list[Session] = []

    def add_session(self, player1: PlayerConnection, player2: PlayerConnection) -> None:
        self.__sessions.append(Session(player1, player2))

    def go(self, socket: WebSocketHandler, move_data: MoveData) -> ShotResult:
        player, enemy = self.__get_players(socket)

        shot = move_data.coordinates
        hit_ships = enemy.ships.filter(lambda ship: ship.collides(shot))
        hit = len(hit_ships) != 0

        enemy.socket.write_message(GetEnemyShot(coordinates=shot, hit=hit).json())

        if not hit:
            return ShotResult(hit=False, destroyed=False, won=False)

        player.current_question = self.__questions.get_question()
        player.current_question_model = player.current_question.to_model()

        hit_ship: GameShip = hit_ships[0]
        hit_ship.hit(shot)

        if not hit_ship.is_destroyed():
            return ShotResult(hit=True, question=player.current_question_model, destroyed=False, won=False)
        enemy.remove_ship(hit_ship)
        if len(enemy.ships) != 0:
            return ShotResult(hit=True, destroyed=True, destroyed_ship=hit_ship.to_ship(),
                              question=player.current_question_model, won=False)
        return ShotResult(hit=True, destroyed=True, destroyed_ship=hit_ship.to_ship(), won=True,
                          question=player.current_question_model)

    def answer(self, socket: WebSocketHandler, answer_data: AnswerData) -> AnswerResult:
        player, enemy = self.__get_players(socket)
        right = player.current_question.answers[0] == player.current_question_model.answers[answer_data.answer_index]
        enemy.socket.write_message(GetEnemyAnswer(right=right).json())
        return AnswerResult(right=right)

    def remove_session_if_exists(self, socket: WebSocketHandler) -> None:
        session = self.__find_session(socket)
        if session is not None:
            self.__sessions.remove(session)

    def enemy_go(self, socket: WebSocketHandler) -> None:
        _, enemy = self.__get_players(socket)
        enemy.socket.write_message(PlayerTurn().json())

    def __get_players(self, socket: WebSocketHandler) -> tuple[PlayerConnection, PlayerConnection]:
        return self.__find_session(socket).sort(socket)

    def __find_session(self, socket: WebSocketHandler) -> Session:
        for session in self.__sessions:
            if session.player1.socket is socket or session.player2.socket is socket:
                return session
