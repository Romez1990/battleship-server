from typing import (
    Type,
)
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

from src.ioc_container import service
from src.immutable_collections import List
from .routes import Route
from .app import App
from .urls import http_urls, web_socket_urls


@service
class AppImpl(App, Application):
    def __init__(self) -> None:
        rules = self.__get_rules()
        super().__init__(rules)

    def __get_rules(self) -> list[tuple[str, Type[RequestHandler]]]:
        http_rules = List(http_urls) \
            .map(self.__to_rule)
        web_socket_rules = List(web_socket_urls) \
            .map(self.__to_rule)
        return list(http_rules + web_socket_rules)

    def __to_rule(self, route: Route[RequestHandler]) -> tuple[str, Type[RequestHandler]]:
        return route.to_rule()

    def run(self) -> None:
        self.listen(8001)
        print('Server has been started')
        IOLoop.current().start()
