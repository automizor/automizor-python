from automizor.utils import OS_RELEASE, OS_SYSTEM, get_headers, version


def test_get_headers():
    token = "foo"
    assert {
        "Authorization": f"Token {token}",
        "User-Agent": f"Automizor/{version} {OS_SYSTEM}/{OS_RELEASE}",
    } == get_headers(token)
