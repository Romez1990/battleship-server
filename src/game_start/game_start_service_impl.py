from src.ioc_container import service
from .game_start_service import GameStartService


@service
class GameStartServiceImpl(GameStartService):
    def get_text(self) -> str:
        return 'Hello world'
