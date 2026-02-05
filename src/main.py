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

    # # 获取当前脚本所在目录
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # # 设置应用程序级别的默认图标（所有窗口默认使用）
    # app.setWindowIcon(QIcon(os.path.join(current_dir, "rc/logo.ico")))

    app.setWindowIcon(QIcon(":/images/logo.ico"))

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())
