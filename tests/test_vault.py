import pytest

from automizor import vault


@pytest.mark.vcr()
def test_vault_secret_create_get_set(test_secret):
    secret = vault.create_secret(**test_secret)
    assert secret.name == test_secret.get("name")
    assert secret.value == test_secret.get("value")
    assert secret.description == test_secret.get("description")

    secret = vault.get_secret(test_secret.get("name"))
    assert secret.name == test_secret.get("name")

    secret = vault.set_secret(secret)
    assert secret.name == test_secret.get("name")


@pytest.mark.vcr()
def test_vault_secret_not_found():
    with pytest.raises(vault.SecretNotFoundError):
        vault.get_secret("nonexistent")
