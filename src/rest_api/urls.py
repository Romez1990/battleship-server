from .request_handlers import (
    PlayerHandler,
    CreateGameHandler,
)

# TODO:  Delete `/api/v1/` and move it to GLOBAL urls.py which in the `app` directory
REST_API_URLS = [
    (r'/api/v1/player/', PlayerHandler),
    (r'/api/v1/create-game/', CreateGameHandler),
]
