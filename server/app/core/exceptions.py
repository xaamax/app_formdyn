class AppException(Exception):
    def __init__(self, status_code: int, detail: str):
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail


class BadRequestException(AppException):
    def __init__(self, detail: str):
        super().__init__(400, detail)


class NotFoundException(AppException):
    def __init__(self, detail: str):
        super().__init__(404, detail)


class UnauthorizedException(AppException):
    def __init__(self, detail: str):
        super().__init__(401, detail)
