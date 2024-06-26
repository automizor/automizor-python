import os
import platform

from automizor import version
from automizor.exceptions import AutomizorError

OS_SYSTEM, OS_RELEASE, _ = platform.system_alias(
    platform.system(), platform.release(), platform.version()
)


def get_api_config() -> tuple[str, str]:
    token_string = os.getenv("AUTOMIZOR_AGENT_TOKEN")

    if not token_string:
        raise AutomizorError("AUTOMIZOR_AGENT_TOKEN is not set.")

    try:
        token, url = token_string.strip().split("@")
    except ValueError as exc:
        raise AutomizorError(
            "AUTOMIZOR_AGENT_TOKEN is not in the correct format."
        ) from exc
    return url, token


def get_headers(token: str) -> dict:
    return {
        "Authorization": f"Token {token}",
        "User-Agent": f"Automizor/{version} {OS_SYSTEM}/{OS_RELEASE}",
    }


# Decorator to make a class a singleton
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance
