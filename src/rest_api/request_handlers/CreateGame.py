import tornado.web

from ..generics import BaseApi


class CreateGameHandler(BaseApi, tornado.web.RequestHandler):
    GET_JSON = {'result': '001'}
