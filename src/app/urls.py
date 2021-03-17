from src.game_start import GameStartHandler
from src.game_session import GameSessionHandler
from src.rest_api.request_handlers import PlayerHandler, CreateGameHandler
from .routes import HttpRoute, WebSocketRoute

http_urls: list[HttpRoute] = [
    HttpRoute('start', GameStartHandler),
    HttpRoute('player', PlayerHandler),
    HttpRoute('create-game', CreateGameHandler),
]

web_socket_urls: list[WebSocketRoute] = [
    WebSocketRoute('game-session', GameSessionHandler),
]
