from typing import (
    Type,
    Callable,
)


class BindingContext:
    def __init__(self, class_type: Type, callback: Callable[[Type], None]) -> None:
        self.__class_type = class_type
        self.__callback = callback

    def to(self, base_class: Type) -> None:
        self.__callback(base_class)

    def to_self(self) -> None:
        self.__callback(self.__class_type)
