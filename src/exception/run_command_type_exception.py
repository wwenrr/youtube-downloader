class commandTypeException(Exception):
    def __init__(self, message="Tùy chọn lệnh không hợp lệ!"):
        super().__init__(message)