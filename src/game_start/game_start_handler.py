from tornado.web import RequestHandler


class GameStartHandler(RequestHandler):
    def get(self) -> None:
        self.write('Hello world')
