import json

import tornado.web


class PlayerHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        player = {
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'year_of_birth': data.get('year_of_birth'),
            'grade': data.get('grade'),
        }
