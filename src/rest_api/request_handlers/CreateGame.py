import tornado.web

from ..generics import BaseHandlerApi


class CreateGameHandler(BaseHandlerApi, tornado.web.RequestHandler):
    GET_JSON = {'result': '001'}
