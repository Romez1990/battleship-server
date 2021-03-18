import tornado.web

from ..generics import BaseHandler


class BaseHandlerApi(BaseHandler):
    GET_JSON: dict = None
    POST_JSON: dict = None

    def get(self) -> None:
        self.write(self.GET_JSON)

    def post(self):
        self.write(self.POST_JSON)
