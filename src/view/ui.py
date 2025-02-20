from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from .submit_button import clicked

def start_ui():
    global window

    app = QApplication([])
    window = uic.loadUi("assets/gui/ytb.ui")  
    window.setWindowIcon(QIcon("assets/img/acorn.png"))
    window.pushButton.clicked.connect(clicked)

    window.show()
    app.exec()