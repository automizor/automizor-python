import json
import os

from dotmap import DotMap


def get(key):
    value = os.environ.get(key)
    if value:
        try:
            return DotMap(json.loads(value))
        except json.JSONDecodeError:
            return value
    return None
