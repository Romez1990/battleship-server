from .request_handlers import (
    PlayerHandler,
    CreateGame,
)

REST_API_URLS = [
    (r'/api/v1/player/', PlayerHandler),
    (r'/api/v1/create-game/', CreateGame),
]
