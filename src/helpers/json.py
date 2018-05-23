import json

__all__ = (
    'json_dumps',
)


def json_dumps(d):
    return json.dumps(d, default=str)
