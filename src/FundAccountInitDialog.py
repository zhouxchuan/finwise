from ui.FundAccountInitDialog_ui import Ui_FundAccountInitDialog
from PySide6.QtWidgets import QDialog

from utils.utils import string_to_float
from utils.mysqldb import MySQLDB


class FundAccountInitDialog(QDialog, Ui_FundAccountInitDialog):
    def __init__(self, parent=None, params=None):
        super(FundAccountInitDialog, self).__init__(parent)
        self.setupUi(self)
        self.params = params
        self.fundLabel.setText(f"{self.params['name']} [{self.params['code']}] 初始成本及份额")

    def accept(self):
        self.initCost = string_to_float(self.costEdit.text())
        self.initShare = string_to_float(self.shareEdit.text())

        if self.initCost <= 0 or self.initShare <= 0:
            self.msgLabel.setText("初始成本和初始份额必须大于0")
            return

        rowcount = MySQLDB.setFundAccountInitData(self.params['code'], self.initCost, self.initShare)
        if rowcount > 0:
            return super().accept()
        else:
            return super().reject()
