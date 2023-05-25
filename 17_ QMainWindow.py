# menü işlemlerinin extra olarak yer aldığı pencerele

from PyQt5.QtWidgets import *
import sys

class main_pen(QMainWindow):
    def __init__(self):
        super().__init__()

main_application=QApplication(sys.argv)
main_window=main_pen()
main_window.show()
main_application.exec()
