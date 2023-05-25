# soru sorup cevap alınan pencereler.

from PyQt5.QtWidgets import *
import sys


class dialog_pen(QDialog):
    def __init__(self):
        super().__init__()


dialog_application=QApplication(sys.argv)
dialog_window=dialog_pen()
dialog_window.show()
dialog_application.exec()
