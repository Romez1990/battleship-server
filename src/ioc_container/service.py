services: list[type] = []


def service(class_type: type) -> type:
    services.append(class_type)
    return class_type
