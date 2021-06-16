from tornado.websocket import WebSocketHandler
from pydantic import BaseModel

from .socket import Socket


class TornadoSocket(Socket):
    def __init__(self, handler: WebSocketHandler) -> None:
        self.__handler = handler

    def send(self, model: BaseModel) -> None:
        text = model.json()
        self.__handler.write(text)

