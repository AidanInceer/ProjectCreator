def is_dict(object: str | list | dict) -> bool:
    return isinstance(object, dict)


def is_list(object: str | list | dict) -> bool:
    return isinstance(object, list)


def is_str(object: str | list | dict) -> bool:
    return isinstance(object, str)
