from src.ioc_container import container


def service(type_: type) -> None:
    base_type = type_.__bases__[0]
    container.bind(type_).to(base_type)
