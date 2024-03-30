import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def test_secret():
    return {
        "name": "testSecret",
        "value": {"hush": "top secret"},
        "description": "such a secret",
    }
