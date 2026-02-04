from PySide6.QtWidgets import QDialog, QListWidgetItem, QMessageBox
from PySide6.QtCore import Qt, QThread, QObject, Signal
from ui.SetupFundAccountDialog_ui import Ui_SetupFundAccountDialog
from utils.datasource import fundDataSource
from utils.mysqldb import MySQLDB


class SetupFundAccountDialog(QDialog, Ui_SetupFundAccountDialog):
    '''
     设置基金账户项类
    '''

    def __init__(self, parent=None):
        super(SetupFundAccountDialog, self).__init__(parent)
        self.setupUi(self)

        self.listWidget.clear()
        fund_list = MySQLDB.getFundAccountList()
        for item in fund_list:
            list_item = QListWidgetItem(item['code'] + ' ' + item['name'])
            list_item.setData(Qt.UserRole, {'code': item['code'], 'name': item['name']})
            self.listWidget.addItem(list_item)

    def onDeleteButtonClicked(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, '警告', '请选择要删除的基金账户项')
            return

        for item in selected_items:
            fund = item.data(Qt.UserRole)
            fund_code = fund['code']

            reply = QMessageBox.question(self, '确认删除', f'确定要删除基金账户项 {fund_code} {fund["name"]} 吗？',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                continue
            MySQLDB.deleteFundAccount(fund_code)
            self.listWidget.takeItem(self.listWidget.row(item))

    def onSaveButtonClicked(self):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            fund = item.data(Qt.UserRole)
            fund_code = fund['code']
            fund_order = i
            MySQLDB.setFundAccountListOrder(fund_code, fund_order)

        QMessageBox.information(self, '提示', '已保存基金账户项所有改变')
        super().accept()
