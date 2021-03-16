from .container import Container
from .service import services


def scan_services() -> Container:
    container = Container()
    for service in services:
        base_class = service.__bases__[0]
        container.bind(service).to(base_class)
    return container
