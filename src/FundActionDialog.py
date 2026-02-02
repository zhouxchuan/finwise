
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from ui.FundActionDialog_ui import Ui_FundActionDialog
from utils.mysqldb import MySQLDB
from utils.utils import string_to_float, format_float


class FundActionDialog(QDialog, Ui_FundActionDialog):
    def __init__(self, parent=None, params=None, mode='add'):
        super(FundActionDialog, self).__init__(parent)
        self.setupUi(self)
        self.linkButton.setChecked(True)
        self.data = params
        self.mode = mode

        self.data['action_date'] = params.get('action_date', QDate.currentDate())
        self.data['action_type'] = params.get('action_type', 'buy')
        self.data['net_value'] = params.get('net_value', 0)
        self.data['cost_amount'] = params.get('cost_amount', 0)
        self.data['share_amount'] = params.get('share_amount', 0)

        if self.mode == 'add':
            self.setWindowTitle(f"{self.data['name']} [{self.data['code']}] 新增操作记录")
        elif self.mode == 'update':
            self.setWindowTitle(f"{self.data['name']} [{self.data['code']}] 更新操作记录")
        else:
            self.setWindowTitle(f"{self.data['name']} [{self.data['code']}] 发生错误")

        self.dateEdit.setDate(QDate.fromString(self.data['action_date'], 'yyyy-MM-dd'))
        self.netvalueEdit.setText(self.data['net_value'])

        self.buyRadioButton.setChecked(self.data['action_type'] == 'buy')
        self.sellRadioButton.setChecked(self.data['action_type'] == 'sell')

        self.costEdit.setText(self.data['cost_amount'])
        self.shareEdit.setText(self.data['share_amount'])

    def onDateChanged(self, date):
        selectedDate = date.toString('yyyy-MM-dd')
        res = MySQLDB.getFundNetValue(self.data['code'], selectedDate)
        if res:
            self.data['action_date'] = selectedDate
            self.data['net_value'] = res['asset_net_value']
            self.netvalueEdit.setText(str(res['asset_net_value']))

    def onCostEditingFinished(self):
        if self.costEdit.text():
            cost = string_to_float(self.costEdit.text())
            if cost is None:
                return
            self.costEdit.setText(format_float(cost, 2))

            self.data['cost_amount'] = cost
            net_value = string_to_float(self.netvalueEdit.text())
            if self.linkButton.isChecked() and net_value:
                share = cost / net_value
                self.data['share_amount'] = share
                self.shareEdit.setText(format_float(share, 2))

    def onShareEditingFinished(self):
        if self.shareEdit.text():
            share = string_to_float(self.shareEdit.text())
            if share is None:
                return
            self.shareEdit.setText(format_float(share, 2))

            self.data['share_amount'] = share
            net_value = string_to_float(self.netvalueEdit.text())
            if self.linkButton.isChecked() and net_value:
                cost = share * net_value
                self.data['cost_amount'] = cost
                self.costEdit.setText(format_float(cost, 2))

    def accept(self):
        self.data['action_date'] = self.dateEdit.date().toString('yyyy-MM-dd')
        self.data['action_type'] = self.buyRadioButton.text() if self.buyRadioButton.isChecked() else self.sellRadioButton.text()
        self.data['cost_amount'] = string_to_float(self.costEdit.text())
        self.data['share_amount'] = string_to_float(self.shareEdit.text())
        self.data['net_value'] = string_to_float(self.netvalueEdit.text())
        self.data['remark'] = '未执行' if self.saveCheckBox.isChecked() else '已执行'

        if self.data['action_date'] is None or self.data['action_type'] is None or \
                (self.data['cost_amount'] is None and self.data['share_amount'] is None):
            self.reject()
            return

        rowcount = MySQLDB.setFundActionData(self.data)
        if rowcount > 0:
            self.accept()
        else:
            self.reject()
