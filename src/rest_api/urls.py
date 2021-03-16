from .request_handlers import (
    FooHandler,
    PlayerHandler,
)

REST_API_URLS = [
    (r'/api/v1/foo/', FooHandler),
    (r'/api/v1/player/', PlayerHandler),
]
