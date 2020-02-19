class InternalServerError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
}
