from .ioc_container import container
from .app import App


def main() -> None:
    app = container.get(App)

    app.run()
