from src.game_start import GameStartHandler
from src.game_session import GameSessionHandler
from .routes import HttpRoute, WebSocketRoute
from ..rest_api.create_game import CreateGameHandler
from ..rest_api.player import PlayerHandler

http_urls: list[HttpRoute] = [
    HttpRoute('start', GameStartHandler),
    HttpRoute('player', PlayerHandler),
    HttpRoute('create-game', CreateGameHandler),
]

web_socket_urls: list[WebSocketRoute] = [
    WebSocketRoute('game-session', GameSessionHandler),
]
