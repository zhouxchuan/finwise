import sys
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow

# 程序入口
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())
