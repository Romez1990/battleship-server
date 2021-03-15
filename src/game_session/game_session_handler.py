from tornado.websocket import WebSocketHandler


class GameSessionHandler(WebSocketHandler):
    def initialize(self) -> None:
        # inject here
        ...

    def open(self) -> None:
        print('open')
        self.write_message('open message')

    def on_message(self, message):
        print(f'message: {message}')

    def on_close(self):
        print('close')
