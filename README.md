# YouTube Downloader

![YouTube Downloader](https://github.com/wwenrr/youtube-downloader/releases)

YouTube Downloader là một ứng dụng mạnh mẽ giúp bạn tải video và âm thanh từ YouTube với nhiều tùy chọn chất lượng khác nhau.

## Tính năng
- Tải video với độ phân giải tùy chỉnh
- Tải âm thanh dưới dạng MP3
- Hỗ trợ giao diện đồ họa (GUI) với PyQt6
- Hỗ trợ đa luồng để tối ưu hiệu suất
- Sử dụng `yt-dlp` để xử lý video

## Cấu trúc dự án
```
 youtube-downloader/
 ├── assets/                 # Chứa các tài nguyên như icon, file UI
 │   ├── gui/                # File giao diện GUI (.ui)
 │   ├── acorn.png           # Icon của ứng dụng
 ├── resources/              # Các tệp nhị phân như yt-dlp, ffmpeg
 ├── src/                    # Mã nguồn chính
 │   ├── view/               # Thành phần giao diện
 │   │   ├── main_window.py  # Cửa sổ chính
 │   │   ├── submit_button.py # Xử lý nút tải
 │   ├── service/            # Các dịch vụ xử lý nền
 │   │   ├── download.py     # Chức năng tải video
 │   ├── exception/          # Xử lý ngoại lệ
 │   │   |── download_opt_exception.py
 ├── venv/                   # Môi trường ảo Python
 ├── requirements.txt        # Danh sách thư viện cần thiết
 ├── ytb_downloader.spec     # File cấu hình cho PyInstaller
 ├── README.md               # Tài liệu hướng dẫn
 ├── main.py                 # Điểm vào chính của ứng dụng
```

## Cài đặt
```sh
git clone https://github.com/wwenrr/youtube-downloader.git
cd youtube-downloader
python -m venv venv
source venv/bin/activate  # Trên macOS/Linux
venv\Scripts\activate     # Trên Windows
pip install -r requirements.txt
```

## Chạy ứng dụng
```sh
python main.py
```

## Đóng gói thành file thực thi
```sh
pyinstaller --noconsole --onefile --icon=assets/acorn.png main.py
```

