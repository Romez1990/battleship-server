from __future__ import annotations
from typing import (
    get_type_hints,
    Type,
    Callable,
    TypeVar,
    TYPE_CHECKING,
)

from .errors import (
    SubclassError,
    TypeAlreadyBoundError,
    TypeMatchingError,
    TypeNotFoundError,
    MissingTypeHintError,
)
from .binding_context import BindingContext
from .type_hints import TypeHints

if TYPE_CHECKING:
    from .module import Module

T = TypeVar('T')

wrapper_descriptor = type(object.__init__)


class Container:
    def __init__(self) -> None:
        self.__types: dict[Type, Type] = {}
        self.__instances: dict[Type, object] = {}

    def register_module(self, module: Type[Module]) -> None:
        module_object = module(self)
        module_object.bind()

    def bind(self, class_type: Type) -> BindingContext:
        return BindingContext(class_type, lambda base_class: self.__bind_type(class_type, base_class))

    def __bind_type(self, class_type: Type, base_class: Type) -> None:
        if not issubclass(class_type, base_class):
            raise SubclassError(class_type, base_class)
        if base_class in self.__types:
            class_type = self.__types[base_class]
            raise TypeAlreadyBoundError(base_class, class_type)
        elif base_class in self.__instances:
            instance = self.__instances[base_class]
            raise TypeAlreadyBoundError(base_class, class_type(instance))
        self.__types[base_class] = class_type

    def get(self, base_class: Type[T]) -> T:
        if base_class in self.__instances:
            instance = self.__instances[base_class]
            return self.__as_type(instance, base_class)
        if base_class not in self.__types:
            raise TypeNotFoundError(base_class)
        type = self.__types[base_class]
        instance = self.__instantiate_type(type)
        del self.__types[base_class]
        self.__instances[base_class] = instance
        return self.__as_type(instance, base_class)

    def __as_type(self, instance: object, class_type: Type[T]) -> T:
        if not isinstance(instance, class_type):
            raise TypeMatchingError(instance, class_type)
        return instance

    def __instantiate_type(self, class_type: Type) -> object:
        type_hints = self.__get_constructor_type_hints(class_type)
        parameter_type: Type[object]
        return class_type(**{parameter_name: self.get(parameter_type)
                             for parameter_name, parameter_type in type_hints.items()})

    def __get_constructor_type_hints(self, class_type: Type) -> TypeHints:
        constructor = class_type.__init__
        if self.__is_constructor_empty(constructor):
            return TypeHints({})
        type_hints = get_type_hints(constructor)
        if 'return' in type_hints:
            del type_hints['return']
        parameter_names = self.__get_function_parameters(constructor)
        if len(type_hints) != len(parameter_names):
            parameters_with_no_type_hint = [parameter_name for parameter_name in parameter_names
                                            if parameter_name not in type_hints]
            raise MissingTypeHintError(class_type, parameters_with_no_type_hint)
        return TypeHints(type_hints)

    def __is_constructor_empty(self, constructor: Callable) -> bool:
        return isinstance(constructor, wrapper_descriptor)

    def __get_function_parameters(self, func: Callable) -> list[str]:
        number_of_parameters = func.__code__.co_argcount
        self_parameter = 1
        return list(func.__code__.co_varnames[self_parameter:number_of_parameters])
