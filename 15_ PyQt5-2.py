# nesne kullanarak button oluşturma
# QToolTip: bize bilgi verir (ipucu)

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont


class p_class(QWidget):
    def __init__(self):
        super().__init__()
        self.window_design()

    def window_design(self):
        QToolTip.setFont(QFont('verdana',22))
        self.setToolTip("Bu bir penceredir")
        button_01=QPushButton("Düğme_tıklanabilir",self)
        button_01.clicked.connect(self.tiklandi)
        button_01.move(100,100)
        button_01.setToolTip("Bu bir butondur")
        self.setGeometry(150,250,500,300)
        self.setWindowTitle("Button application")
        self.show()

    def tiklandi(self):
        print("Butona tıklandı")

# main function
if __name__ == '__main__':
    application=QApplication(sys.argv)
    window=p_class()
    sys.exit(application.exec())



