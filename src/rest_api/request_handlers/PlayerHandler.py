import tornado.web
import json

from ..generics import Base


class PlayerHandler(Base, tornado.web.RequestHandler):
    def post(self) -> None:
        data = json.loads(self.request.body)
        player = {
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'year_of_birth': data.get('year_of_birth'),
            'grade': data.get('grade'),
        }
        self.write({'status_code': self.set_status(201)})
