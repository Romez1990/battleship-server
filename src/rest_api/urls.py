from .request_handlers import (
    PlayerHandler,
)

REST_API_URLS = [
    (r'/api/v1/player/', PlayerHandler),
]
