import sys
import os
import ctypes
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from MainWindow import MainWindow
import rc.finwise_rc

# 程序入口
if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/logo.ico"))

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())
