def is_mixed_case(string: str) -> bool:
    """Check whether a string contains uppercase and lowercase characters."""
    return not string.islower() and not string.isupper()
