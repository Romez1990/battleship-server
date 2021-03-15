from .ioc_container import container, scan_services
from .app import App


def main() -> None:
    scan_services()

    app = container.get(App)

    app.run()
