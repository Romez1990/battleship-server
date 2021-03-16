from tornado.web import Application
from tornado.ioloop import IOLoop

from src.ioc_container import service
from src.game_start import GameStartHandler
from src.game_session import GameSessionHandler
from .app import App


from ..rest_api import REST_API_URLS

URLS = [
    (r'/api/start', GameStartHandler),
    (r'/game_session', GameSessionHandler),
]  # TODO: Try to make it more beautiful

URLS += REST_API_URLS


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
