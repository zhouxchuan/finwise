from ui.InitFundAccountDialog_ui import Ui_InitFundAccountDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from utils.utils import format_convert
from utils.mysqldb import MySQLDB


class InitFundAccountDialog(QDialog, Ui_InitFundAccountDialog):
    def __init__(self, parent=None, params=None):
        super(InitFundAccountDialog, self).__init__(parent)
        self.setupUi(self)
        self.params = params
        self.fundLabel.setText(f"{self.params['name']} [{self.params['code']}] 初始成本及份额")

    def accept(self):
        self.initCost = format_convert.string_to_decimal(self.costEdit.text())
        self.initShare = format_convert.string_to_decimal(self.shareEdit.text())

        if self.initCost <= 0 or self.initShare <= 0:
            self.msgLabel.setText("初始成本和初始份额必须大于0")
            return

        rowcount = MySQLDB.initFundHoldingData(self.params['code'], self.initCost, self.initShare)
        if rowcount > 0:
            return super().accept()
        else:
            return super().reject()
