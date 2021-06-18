from src.connection import ConnectionHandler
from .routes import HttpRoute, WebSocketRoute

http_urls: list[HttpRoute] = [
]

web_socket_urls: list[WebSocketRoute] = [
    WebSocketRoute('connect', ConnectionHandler),
]
