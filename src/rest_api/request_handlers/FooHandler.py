from tornado.web import RequestHandler


class FooHandler(RequestHandler):
    def get(self):
        self.write(
            {
                'message': 'Foo get handler'
            }
        )  # TODO: implement in separate file/services_logic

    def post(self):
        self.write(
            {
                'message': 'Foo post handler'
            }
        )
