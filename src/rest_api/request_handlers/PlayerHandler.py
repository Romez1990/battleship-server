import tornado.web
import json

from tornado import escape, httputil

from typing import Optional


from .BaseHandler import BaseHandler


class PlayerHandler(BaseHandler, tornado.web.RequestHandler):
    def post(self) -> None:
        data = json.loads(self.request.body)
        player = {
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'year_of_birth': data.get('year_of_birth'),
            'grade': data.get('grade'),
        }
        self.write({'player': player})  # TODO: Set the HTTP status code

    def set_status(self, status_code: int, reason: Optional[str] = None) -> None:
        self._status_code = status_code
        if reason is not None:
            self._reason = escape.native_str(reason)
        else:
            self._reason = httputil.responses.get(status_code, "Unknown")
