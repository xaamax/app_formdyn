from app.shared.exceptions import ApplicationException


class FormNotFoundError(ApplicationException):
    def __init__(self):
        super().__init__('Form not found')
