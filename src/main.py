from .ioc_container import scan_services
from .app import App


def main() -> None:
    container = scan_services()
    app = container.get(App)

    app.run()
