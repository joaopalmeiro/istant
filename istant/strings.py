from typing import Any


def is_string(obj: Any) -> bool:
    """Check whether an object is a string."""
    return isinstance(obj, str)


def is_mixed_case(string: str) -> bool:
    """Check whether a string contains uppercase and lowercase characters."""
    return not string.islower() and not string.isupper()
