from src.ioc_container import service
from .game_session_service import GameSessionService


@service
class GameSessionServiceImpl(GameSessionService):
    def open(self) -> None:
        print('WebSocket opened')

    def on_message(self, message) -> None:
        self.write_message(u'You said: ' + message)

    def on_close(self) -> None:
        print('WebSocket closed')
