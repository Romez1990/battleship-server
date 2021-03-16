from src.game_start import GameStartHandler
from src.game_session import GameSessionHandler

from ..rest_api import REST_API_URLS


URLS = [
    (r'/api/start', GameStartHandler),
    (r'/game_session', GameSessionHandler),
]

URLS += REST_API_URLS
