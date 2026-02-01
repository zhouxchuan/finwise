from PySide6.QtWidgets import QDialog
from ui.AboutDialog_ui import Ui_AboutDialog


class AboutDialog(QDialog, Ui_AboutDialog):
    '''
    关于对话框类
    '''

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
