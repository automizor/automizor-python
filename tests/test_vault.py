import pytest

from automizor import exceptions, vault


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
    with pytest.raises(exceptions.NotFound):
        vault.get_secret("nonexistent")


def test_vault_singleton():
    vault1 = vault.Vault()
    vault2 = vault.Vault()
    assert vault1 is vault2
