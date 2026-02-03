
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from ui.FundActionDialog_ui import Ui_FundActionDialog
from utils.mysqldb import MySQLDB
from utils.utils import string_to_float, format_float


class FundActionDialog(QDialog, Ui_FundActionDialog):
    def __init__(self, parent=None, params=None, mode=None):
        super(FundActionDialog, self).__init__(parent)
        self.setupUi(self)
        self.data = params
        self.mode = mode
        self.amount = 0.00

        self.dateEdit.setDate(QDate.currentDate())
        if self.mode == '买入':
            self.setWindowTitle(f"{self.data['name']} [{self.data['code']}] 买入交易")
            self.amountLabel.setText(f"买入金额:")
            self.amountEdit.setText(format_float(self.amount, 2))
        elif self.mode == '卖出':
            self.setWindowTitle(f"{self.data['name']} [{self.data['code']}] 卖出交易")
            self.amountLabel.setText("卖出份额:")
            self.amountEdit.setText(format_float(self.amount, 2))
        else:
            self.msgLabel.setText("无效的交易模式")
            self.buttonBox.button(self.buttonBox.Ok).setEnabled(False)

    def onAmountEditingFinished(self):
        if self.amountEdit.text():
            self.amount = string_to_float(self.amountEdit.text())
            if self.amount is None:
                return
            self.amountEdit.setText(format_float(self.amount, 2))

    def onEstimateButtonClicked(self):
        res = MySQLDB.getFundLatestNetValue(self.data['code'])
        if res:
            trade_date = res['trade_date']
            net_value = res['asset_net_value']
            if trade_date is None or net_value is None:
                self.estimateLabel.setText("预计失败")
                return

            if self.mode == '买入':
                share = self.amount / net_value
                self.estimateLabel.setText(f"按{trade_date}净值{net_value}计算，份额为{format_float(share, 2)}")
            elif self.mode == '卖出':
                cost = self.amount * net_value
                self.estimateLabel.setText(f"按{trade_date}净值{net_value}计算，金额为{format_float(cost, 2)}")

    def accept(self):
        action_date = self.dateEdit.date().toString('yyyy-MM-dd')
        rowcount = MySQLDB.setFundActionData(self.data['code'], action_date, self.mode, self.amount)
        if rowcount > 0:
            return super().accept()
        else:
            return super().reject()
