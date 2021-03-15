from abc import ABCMeta, abstractmethod


class GameStartService(metaclass=ABCMeta):
    @abstractmethod
    def get_text(self) -> str: ...
