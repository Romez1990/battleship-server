from src.ioc_container import service
from .code_counter import CodeCounter


@service
class CodeCounterImpl(CodeCounter):
    def __init__(self) -> None:
        self.__code_length = 3
        self.__limit = 10 ** self.__code_length - 1
        self.__code_counter = 0

    def get_code(self) -> str:
        code = '%03d' % self.__code_counter
        self.__code_counter += 1
        if self.__code_counter > self.__limit:
            self.__code_counter = 0
        return code
