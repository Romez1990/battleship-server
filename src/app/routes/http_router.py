from typing import (
    Type,
)
from tornado.web import RequestHandler

from .route import Route


class HttpRoute(Route[RequestHandler]):
    def to_rule(self) -> tuple[str, Type[RequestHandler]]:
        return f'/api/{self.path}', self.handler
