import time
from PyQt6.QtCore import QThread, pyqtSignal
import threading

class DownloadThread(QThread):
    finished = pyqtSignal() 
    log_signal = pyqtSignal(str)

    def __init__(self, url, quality, opt):
        super().__init__()
        self.url = url
        self.quality = quality
        self.opt = opt

    def run(self):
        def log_callback(text):
            self.log_signal.emit(text)

        from src.service.download import download_video
        download_video(self.url, self.quality, log_callback, self.opt)
        self.finished.emit() 

def clicked():
    from src.view.ui import window
    def enable():
        window.textEdit.setDisabled(False) 
        window.comboBox.setDisabled(False)  
        window.comboBox_2.setDisabled(False) 
        window.pushButton.setDisabled(False)
        window.pushButton.setStyleSheet("""
            background-color: rgb(0, 170, 255); /* Xanh nhạt hơn */
            border-radius: 20px;
        """)
    def disable():
        window.textEdit.setDisabled(True) 
        window.comboBox.setDisabled(True)  
        window.comboBox_2.setDisabled(True) 
        window.pushButton.setDisabled(True)
        window.pushButton.setStyleSheet("""
            background-color: rgb(150, 220, 255); /* Xanh nhạt hơn */
            border-radius: 20px;
        """)
    def downloading():
        from src.service.download import download_video
        download_video(url, quality, opt)
        print("Done")
    def update_log(text):
        window.plainTextEdit.appendPlainText(text)
    def clear_log():
        window.plainTextEdit.clear()
    disable()
    clear_log()
    opt_table = {
        "tải video": "video",
        "tải âm thanh": "audio",
        "tải video và âm thanh": "both"
    }

    url = window.textEdit.toPlainText()
    quality = int(window.comboBox.currentText())
    opt = opt_table[window.comboBox_2.currentText()]

    window.thread = DownloadThread(url, quality, opt)
    window.thread.finished.connect(enable)  
    window.thread.log_signal.connect(update_log)
    window.thread.start()
