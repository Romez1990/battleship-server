from typing import (
    Type,
)
from tornado.websocket import WebSocketHandler

from .route import Route


class WebSocketRoute(Route[WebSocketHandler]):
    def to_rule(self) -> tuple[str, Type[WebSocketHandler]]:
        return f'/{self.path}', self.handler
