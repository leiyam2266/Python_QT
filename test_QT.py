from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

X = 200
Y = 200
width = 300
height = 300

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(X, Y, width, height)
    win.setWindowTitle("eDoctor")

    win.show()
    sys.exit(app.exec_())

window()
