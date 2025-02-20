class DownloadOptionException(Exception):
    """Ngoại lệ tùy chỉnh cho các tùy chọn tải xuống không hợp lệ."""
    
    def __init__(self, message="Tùy chọn tải xuống không hợp lệ!"):
        super().__init__(message)