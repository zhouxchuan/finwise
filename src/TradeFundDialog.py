
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from ui.TradeFundDialog_ui import Ui_TradeFundDialog
from utils.mysqldb import MySQLDatabase as MySQLDB
from utils.utils import format_convert


class TradeFundDialog(QDialog, Ui_TradeFundDialog):
    def __init__(self, parent=None, params=None, mode=None):
        super(TradeFundDialog, self).__init__(parent)
        self.setupUi(self)
        self.data = params
        self.mode = mode
        self.amount = 0.00

        self.dateEdit.setDate(QDate.currentDate())
        if self.mode == '买入':
            self.setWindowTitle(f"{self.data['name']} [{self.data['code']}] 买入交易")
            self.amountLabel.setText(f"买入金额:")
            self.amountEdit.setText(format_convert.decimal_to_string(self.amount, 2))
        elif self.mode == '卖出':
            self.setWindowTitle(f"{self.data['name']} [{self.data['code']}] 卖出交易")
            self.amountLabel.setText("卖出份额:")
            self.amountEdit.setText(format_convert.decimal_to_string(self.amount, 2))
        else:
            self.setWindowTitle(f"{self.data['name']} [{self.data['code']}] 交易模式无效")
            self.okButton.setEnabled(False)

    def onAmountEditingFinished(self):
        if self.amountEdit.text():
            self.amount = format_convert.string_to_decimal(self.amountEdit.text())
            if self.amount is None:
                return
            self.amountEdit.setText(format_convert.decimal_to_string(self.amount, 2))

    def onEstimateButtonClicked(self):
        res = MySQLDB.getFundLatestNetValue(self.data['code'])
        if res:
            trade_date = res['trade_date']
            net_value = res['asset_net_value']
            net_value = format_convert.float_to_decimal(net_value, 4)
            if trade_date is None or net_value is None:
                self.estimateLabel.setText("预计失败")
                return

            if self.mode == '买入':
                share = self.amount / net_value
                self.estimateLabel.setText(f"按{trade_date}净值{net_value}计算，份额为{format_convert.decimal_to_string(share, 2)}")
            elif self.mode == '卖出':
                cost = self.amount * net_value
                self.estimateLabel.setText(f"按{trade_date}净值{net_value}计算，金额为{format_convert.decimal_to_string(cost, 2)}")

    def accept(self):
        action_date = self.dateEdit.date().toString('yyyy-MM-dd')
        rowcount = MySQLDB.setFundTradingData(self.data['code'], action_date, self.mode, self.amount)
        if rowcount > 0:
            return super().accept()
        else:
            return super().reject()
