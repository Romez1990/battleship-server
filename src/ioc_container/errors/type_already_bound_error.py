from typing import (
    Type,
)


class TypeAlreadyBoundError(Exception):
    def __init__(self, base_class: Type, type: Type) -> None:
        super().__init__(f'type "{base_class.__name__}" is already bound to "{type.__name__}"')
