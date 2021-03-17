from src.game_start import GameStartHandler
from src.game_session import GameSessionHandler
from .routes import HttpRoute, WebSocketRoute

http_urls: list[HttpRoute] = [
    HttpRoute('start', GameStartHandler),
]

web_socket_urls: list[WebSocketRoute] = [
    WebSocketRoute('game-session', GameSessionHandler),
]
