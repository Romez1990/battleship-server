from abc import ABCMeta, abstractmethod

from .question import Question


class QuestionService(metaclass=ABCMeta):
    @abstractmethod
    def get_question(self) -> Question: ...
