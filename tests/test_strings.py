import pytest

from istant.strings import is_mixed_case, is_string


# is_string
@pytest.mark.parametrize("obj", ["", " ", "Hello, World!", "H"])
def test_is_string(obj):
    assert is_string(obj)


@pytest.mark.parametrize("obj", [1, 1.1, ["Hello", "World"], b"Hello, World!"])
def test_is_string_not_string(obj):
    assert not is_string(obj)


# is_mixed_case
@pytest.mark.parametrize(
    "string", ["Hello, World!", "hello, World!", "Hello World", "Hello world"]
)
def test_is_mixed_case(string):
    assert is_mixed_case(string)


@pytest.mark.parametrize(
    "string", ["HELLO, WORLD!", "hello, world!", "HELLO WORLD", "hello world"]
)
def test_is_mixed_case_not_mixed_case(string):
    assert not is_mixed_case(string)
