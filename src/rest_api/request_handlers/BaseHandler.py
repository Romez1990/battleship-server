import tornado.web

from tornado import escape, httputil

from typing import Optional, Union


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self) -> None:
        self.set_header("Content-Type", 'application/json')

    #  TODO: read about `set_status` method
    def set_status(self, status_code: int, reason: Optional[str] = None) -> Union[str, int]:
        self._status_code = status_code
        if reason is not None:
            self._reason = escape.native_str(reason)
            return "Unknown"
        else:
            self._reason = httputil.responses.get(status_code, "Unknown")
            return self._status_code
