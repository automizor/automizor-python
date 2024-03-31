from automizor import exceptions, storage


def test_storage_singleton():
    storage1 = storage.Storage()
    storage2 = storage.Storage()
    assert storage1 is storage2
