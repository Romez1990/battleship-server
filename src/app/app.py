from abc import ABCMeta, abstractmethod


class App(metaclass=ABCMeta):
    @abstractmethod
    def run(self) -> None: ...
