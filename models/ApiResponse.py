class ApiResponse:
    def __init__(self, code, type, message):
        # integer: code
        self.code = code

        # string: type
        self.type = type

        # string: message
        self.message = message

    def to_dict(self):
        return {
            "code": self.code,
            "type": self.type,
            "message": self.message,
        }
