import pytest

from automizor import vault


def test_crud_secret(mock_session, test_secret):
    secret = vault.create_secret(**test_secret)
    assert secret.name == test_secret.get("name")
    assert secret.value == test_secret.get("value")
    assert secret.description == test_secret.get("description")

    secret = vault.get_secret(test_secret.get("name"))
    assert secret.name == test_secret.get("name")

    secret = vault.set_secret(secret)
    assert secret.name == test_secret.get("name")


def test_vault_secret_not_found(mock_session_secret_not_found):
    with pytest.raises(vault.SecretNotFoundError):
        vault.get_secret("nonexistent")


def test_vault_error(mock_session_vault_error):
    with pytest.raises(vault.AutomizorVaultError):
        vault.get_secret("nonexistent")
