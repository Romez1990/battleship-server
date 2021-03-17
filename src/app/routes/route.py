from abc import ABCMeta, abstractmethod
from typing import (
    Type,
    TypeVar,
    Generic,
)

from tornado.web import RequestHandler

T = TypeVar('T', bound=RequestHandler)


class Route(Generic[T], metaclass=ABCMeta):
    def __init__(self, path: str, handler: Type[T]) -> None:
        if path.startswith('/') or path.endswith('/'):
            raise Exception
        self.__path = path
        self.__handler = handler

    @property
    def path(self) -> str:
        return self.__path

    @property
    def handler(self) -> Type[T]:
        return self.__handler

    @abstractmethod
    def to_rule(self) -> tuple[str, Type[T]]: ...
