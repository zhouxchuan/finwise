from ui.CreateFundAccountDialog_ui import Ui_CreateFundAccountDialog
from PySide6.QtWidgets import QDialog, QMessageBox, QListWidgetItem
from PySide6.QtCore import Qt, QThread, Signal
from utils.datasource import fundDataSource
from utils.mysqldb import MySQLDB


class CreateFundAccountDialog(QDialog, Ui_CreateFundAccountDialog):
    def __init__(self, parent=None):
        super(CreateFundAccountDialog, self).__init__(parent)
        self.setupUi(self)
        self.dataFetchThread = DataFetchThread(self)
        self.dataFetchThread.dataSignal.connect(self.onDataReceived)

    def onSearchButtonClicked(self):
        # 获取用户输入的公司代码
        company = self.companyLineEdit.text().strip()
        if not company:
            company = '80000229'  # 默认易方达
        # 设置线程参数并启动
        self.dataFetchThread.setParams(company)
        self.dataFetchThread.start()

    def onCreateButtonClicked(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            self.msgLabel.setText('请选择基金')
            return

        for item in selected_items:
            fund = item.data(Qt.UserRole)
            res = MySQLDB.addFundAccount(fund['code'], fund['name'])
            if res > 0:
                QMessageBox.information(self, '信息', f'已创建基金账户 {fund["code"]} {fund["name"]}')
            else:
                QMessageBox.warning(self, '警告', f'创建基金账户 {fund["code"]} {fund["name"]} 失败, 请检查该基金是否已存在。')
        super().accept()

    def onDataReceived(self, data):
        '''
        接收数据线程发送的数据
        :param data: 基金数据列表
        '''
        searchText = self.searchLineEdit.text().strip()

        # 清空当前列表
        self.listWidget.clear()
        # 添加新数据
        for item in data:
            if searchText != '' and (searchText not in item['name'] and searchText not in item['code']):
                continue
            list_item = QListWidgetItem(f"{item['code']} {item['name']}")
            list_item.setData(Qt.UserRole, item)
            self.listWidget.addItem(list_item)


class DataFetchThread(QThread):
    '''
    工作线程类，用于在后台获取基金数据
    '''
    # 定义信号，用于传递数据和状态
    dataSignal = Signal(list)  # 传递基金数据列表

    def setParams(self, company='80000229'):
        self.company = company

    def run(self):
        try:
            # 从数据源获取所有基金
            data = fundDataSource.getAllFunds(self.company)
            self.dataSignal.emit(data)
        except Exception as e:
            print(f'DataFetchThread Error: {e}')
