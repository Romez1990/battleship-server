from importlib import import_module
from pathlib import Path

from .container import Container
from .service import services

root_dir = 'src'


def scan_services() -> Container:
    container = Container()
    import_all_modules()
    bind_services(container)
    return container


def import_all_modules() -> None:
    source_directory = get_source_directory()
    import_modules_in_directory(source_directory, root_dir)


def get_source_directory() -> Path:
    current_path = Path(__file__)
    while current_path.is_file() or current_path.name != root_dir:
        current_path = current_path.parent
    return current_path


def import_modules_in_directory(directory: Path, package_name: str) -> None:
    for fs_node in directory.iterdir():
        if fs_node.is_dir():
            import_modules_in_directory(fs_node, f'{package_name}.{fs_node.name}')
        else:
            if fs_node.suffix == '.py':
                import_module(f'{package_name}.{fs_node.stem}')


def bind_services(container: Container) -> None:
    for service in services:
        base_class = service.__bases__[0]
        container.bind(service).to(base_class)
