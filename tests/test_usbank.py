import pytest
from bankr.usbank import USBank


@pytest.fixture(scope="module")
def initialize_api():
    return USBank()


def test_generate_oauth_token(initialize_api: object) -> None:
    assert initialize_api._generate_oauth_token() is not None


def test_generate_oauth_token_type(initialize_api: object) -> None:
    assert type(initialize_api._generate_oauth_token()) == str


def test_validate_oauth_token_not_undefined(initialize_api: object) -> None:
    assert initialize_api._generate_oauth_token() != "undefined"
