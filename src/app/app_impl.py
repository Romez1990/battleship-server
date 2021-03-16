from tornado.web import Application
from tornado.ioloop import IOLoop

from src.ioc_container import service

from .app import App

from .urls import URLS


@service
class AppImpl(App, Application):
    def __init__(self) -> None:
        super().__init__(
            URLS
        )

    def run(self) -> None:
        self.listen(8001)
        print('Server has been started')
        IOLoop.current().start()
