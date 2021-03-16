services: list[type] = []


def service(class_type: type) -> None:
    services.append(class_type)
