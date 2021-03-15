from tornado.web import Application
from tornado.ioloop import IOLoop

from src.ioc_container import service
from .app import App


@service
class AppImpl(App, Application):
    def __init__(self) -> None:
        super().__init__([
        ])

    def run(self) -> None:
        self.listen(8000)
        print('Server has been started')
        IOLoop.current().start()
