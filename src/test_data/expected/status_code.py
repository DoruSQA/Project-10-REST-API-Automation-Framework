from enum import IntEnum


class StatusCode(IntEnum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_FOUND = 404
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
