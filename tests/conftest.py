import pytest
import requests


@pytest.fixture
def test_secret():
    return {
        "name": "testSecret",
        "value": {"hush": "top secret"},
        "description": "such a secret",
    }


@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("AUTOMIZOR_API_HOST", "http://localhost:8000")
    monkeypatch.setenv("AUTOMIZOR_API_TOKEN", "foo")


@pytest.fixture
def mock_session(mocker, test_secret):
    mock_session = mocker.Mock(spec=requests.Session)
    mock_session.headers = mocker.MagicMock()
    mock_response = mocker.Mock()
    mock_response.json.return_value = test_secret

    mock_session.put.return_value = mock_response  # mock put request
    mock_session.get.return_value = mock_response  # mock get request

    mocker.patch("requests.Session", return_value=mock_session)
    yield


@pytest.fixture
def mock_session_secret_not_found(mocker):
    mock_session = mocker.Mock(spec=requests.Session)
    mock_session.headers = mocker.MagicMock()
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"detail": "No Secret matches the given query."}
    mock_session.get.side_effect = requests.HTTPError(
        response=mocker.Mock(status_code=404)
    )
    mock_session.get.return_value = mock_response  # mock get request

    mocker.patch("requests.Session", return_value=mock_session)
    yield


@pytest.fixture
def mock_session_vault_error(mocker):
    mock_session = mocker.Mock(spec=requests.Session)
    mock_session.headers = mocker.MagicMock()
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"detail": "Internal Server Error"}
    mock_session.get.side_effect = requests.HTTPError(
        response=mocker.Mock(status_code=500)
    )
    mock_session.get.return_value = mock_response  # mock get request

    mocker.patch("requests.Session", return_value=mock_session)
    yield
