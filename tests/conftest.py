import pytest


@pytest.fixture
def test_secret():
    return {
        "name": "testSecret",
        "value": {"hush": "top secret"},
        "description": "such a secret",
    }


@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    monkeypatch.setenv(
        "AUTOMIZOR_API_HOST",
        "foo.automizor.localhost:8443",
    )
    monkeypatch.setenv(
        "AUTOMIZOR_API_TOKEN",
        "c257ccdbda0c5e04ce26b67ba78438b1848ef4fe",
    )
    monkeypatch.setenv(
        "REQUESTS_CA_BUNDLE",
        "/Users/elmcrest/projects/automizor/automizor-platform/certs/ca.pem",
    )
