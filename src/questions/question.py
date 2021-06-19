from random import shuffle

from pydantic import BaseModel


class QuestionModel(BaseModel):
    text: str
    answers: list[str]


class Question:
    def __init__(self, text: str, answers: list[str]):
        self.__text = text
        self.__answers = answers

    @property
    def text(self) -> str:
        return self.__text

    @property
    def answers(self) -> list[str]:
        return self.__answers

    def to_model(self) -> QuestionModel:
        shuffled_answers = self.answers.copy()
        shuffle(shuffled_answers)
        return QuestionModel(text=self.text, answers=shuffled_answers)
