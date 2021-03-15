from tornado.web import Application
from tornado.ioloop import IOLoop

from src.ioc_container import service
from src.game_start import GameStartHandler
from .app import App


@service
class AppImpl(App, Application):
    def __init__(self) -> None:
        super().__init__([
            ('/api/start', GameStartHandler),
        ])

    def run(self) -> None:
        self.listen(8000)
        print('Server has been started')
        IOLoop.current().start()
