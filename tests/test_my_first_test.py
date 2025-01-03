import pytest


def test_my_first_test(word="Hello World!"):
    assert word == "Hello World!", "Word is incorrect!"


if __name__ == "__main__":
    pytest.main()
