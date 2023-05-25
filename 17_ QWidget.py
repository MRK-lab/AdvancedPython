# kullanılan ekran pencereleri


from PyQt5.QtWidgets import *
import sys

class widget_pen(QWidget):
    def __init__(self):
        super().__init__()


widget_application=QApplication(sys.argv)
widget_window=widget_pen()
widget_window.show()
widget_application.exec()





