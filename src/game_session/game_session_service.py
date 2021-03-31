from abc import ABCMeta, abstractmethod


class GameSessionService(metaclass=ABCMeta):
    @abstractmethod
    def open(self) -> None:
        ...

    @abstractmethod
    def on_message(self, message) -> None:
        ...

    @abstractmethod
    def on_close(self) -> None:
        ...
