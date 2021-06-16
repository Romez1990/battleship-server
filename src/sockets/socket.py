from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class Socket(metaclass=ABCMeta):
    @abstractmethod
    def send(self, model: BaseModel) -> None: ...
