from abc import ABCMeta, abstractmethod


class CodeCounter(metaclass=ABCMeta):
    @abstractmethod
    def get_code(self) -> str: ...
