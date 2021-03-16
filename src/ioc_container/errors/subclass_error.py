from typing import (
    Type,
)


class SubclassError(Exception):
    def __init__(self, type: Type, base_class: Type) -> None:
        super().__init__(f'type "{type.__name__}" is not subclass of "{base_class.__name__}"')
