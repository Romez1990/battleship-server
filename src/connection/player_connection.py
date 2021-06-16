from tornado.websocket import WebSocketHandler

from .models import PlayerData


class PlayerConnection:
    def __init__(self, socket: WebSocketHandler, player_data: PlayerData) -> None:
        self.socket = socket
        self.player_data = player_data
