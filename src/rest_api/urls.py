from .request_handlers import FooHandler

REST_API_URLS = [
    (r'/api/v1/foo/', FooHandler),
]
