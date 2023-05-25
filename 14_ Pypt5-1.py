# pypt5 kütüphanesi

import sys
from PyQt5 import QtWidgets

application=QtWidgets.QApplication(sys.argv)

window=QtWidgets.QWidget()


window.show()
window.setWindowTitle("Hello World")
sys.exit(application.exec())
