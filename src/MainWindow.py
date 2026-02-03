from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QSplitter, QWidget, QSizePolicy, QListWidgetItem, QMenu, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QAction
from numpy import format_float_positional


from utils.mysqldb import MySQLDB
from ui.MainWindow_ui import Ui_mainWindow
from LoginDialog import LoginDialog
from SetupDataDialog import SetupDataDialog
from SetupFundDialog import SetupFundDialog
from TradeFundDialog import TradeFundDialog
from AnalyzeIndexDialog import AnalyzeIndexDialog
from AboutDialog import AboutDialog
from FundBasicInfoDialog import FundBasicInfoDialog
from FundNetValueDialog import FundNetValueDialog
from FundHoldDataDialog import FundHoldDataDialog
from FundActionDialog import FundActionDialog
from FundAccountInitDialog import FundAccountInitDialog

from utils.utils import format_float


class MainWindow(QMainWindow, Ui_mainWindow):
    '''
    主窗口类
    '''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.userid = None
        self.current_fund = {"code": None, "name": None}

        self.setWindowTitle('基金分析1.0 [未登录]')
        self.statusBar.showMessage('请先登录验证账户密码')
        self.setContentsMargins(5, 0, 5, 0)

        toolbar_spacer = QWidget()
        toolbar_spacer.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolBar.addWidget(toolbar_spacer)
        self.toolBar.addAction(self.actionExit)

        self.splitter = QSplitter(Qt.Horizontal, childrenCollapsible=False)
        self.splitter.addWidget(self.leftWidget)
        self.splitter.addWidget(self.rightWidget)
        self.setCentralWidget(self.splitter)

        self.fundNameLabel.setText('[未选择基金]')

        self.fundListWidget.setEnabled(False)
        self.fundListWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fundListWidget.customContextMenuRequested.connect(self.onActionFundListWidgetContextMenu)
        self.fundListWidgetContextMenu = QMenu(self)
        self.fundListWidgetContextMenu.addAction(QAction(u'基本信息', self, triggered=self.onActionFundBasicInfoTriggered))
        self.fundListWidgetContextMenu.addAction(QAction(u'净值数据', self, triggered=self.onActionFundNetValueTriggered))
        self.fundListWidgetContextMenu.addAction(QAction(u'基金持仓', self, triggered=self.onActionFundHoldDataTriggered))

        self.anvTableWidget.setEnabled(False)
        self.anvTableWidget.setColumnCount(3)
        self.anvTableWidget.setHorizontalHeaderLabels(['日期', '单位净值', '累计净值'])
        self.anvTableWidget.setRowCount(0)
        self.anvTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.actionTableWidget.setEnabled(False)
        self.actionTableWidget.setColumnCount(4)
        self.actionTableWidget.setHorizontalHeaderLabels(['日期', '交易', '数额', '标注'])
        self.actionTableWidget.setRowCount(0)
        self.actionTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.actionTableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.actionTableWidget.customContextMenuRequested.connect(self.onActionTableWidgetContextMenu)
        self.actionTableWidgetContextMenu = QMenu(self)
        self.actionTableWidgetContextMenu.addAction(QAction(u'买入交易', self, triggered=self.onActionTradeBuyTriggered))
        self.actionTableWidgetContextMenu.addAction(QAction(u'卖出交易', self, triggered=self.onActionTradeSellTriggered))
        self.actionTableWidgetContextMenu.addAction(QAction(u'撤销交易', self, triggered=self.onActionTradeRevokeTriggered))

    def loadFundList(self):
        '''
        加载基金列表
        '''
        fund_list = MySQLDB.getFundList()
        if fund_list:
            self.fundListWidget.clear()
            for fund in fund_list:
                item = QListWidgetItem(fund['code'] + ' ' + fund['name'])
                item.setData(
                    Qt.UserRole, {'code': fund['code'], 'name': fund['name']})
                self.fundListWidget.addItem(item)
            self.fundListWidget.setCurrentRow(0)
        else:
            self.statusBar.showMessage('没有获取到基金列表')

    def setActionStatus(self, isLoggedIn):
        '''
        设置登录/注销后界面状态
        param: isLoggedIn: 登录状态
        '''
        self.actionLogin.setEnabled(not isLoggedIn)
        self.actionLogout.setEnabled(isLoggedIn)
        self.actionSync.setEnabled(isLoggedIn)
        self.fundListWidget.setEnabled(isLoggedIn)
        self.anvTableWidget.setEnabled(isLoggedIn)
        self.actionTableWidget.setEnabled(isLoggedIn)

        if isLoggedIn:
            self.statusBar.showMessage(f'{self.userid} 已登录', 3000)
        else:
            self.userid = None
            self.setWindowTitle('基金分析1.0 [未登录]')
            self.statusBar.showMessage('请先登录验证账户密码')
            self.fundListWidget.clear()
            self.fundNameLabel.setText('[未选择基金]')
            self.anvTableWidget.clearContents()
            self.anvTableWidget.setRowCount(0)
            self.actionTableWidget.clearContents()
            self.actionTableWidget.setRowCount(0)

    def closeEvent(self, event):
        '''
        窗口关闭事件
        '''
        if QMessageBox.question(self, '提示', "是否确定退出应用程序?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def onActionLoginTriggered(self):
        '''
        登录ACTION事件
        '''
        loginDialog = LoginDialog(self)
        if loginDialog.exec() == QDialog.Accepted:
            self.userid = loginDialog.userid
            self.setWindowTitle(f'基金分析1.0 [{self.userid}]')
            self.statusBar.showMessage(f'{self.userid} 已登录', 3000)
            self.setActionStatus(True)

            # 加载基金数据
            self.loadFundList()

    def onActionLogoutTriggered(self):
        '''
        注销ACTION事件
        '''
        self.setWindowTitle('基金分析1.0 [未登录]')
        self.statusBar.showMessage('已注销', 3000)
        self.setActionStatus(False)

    def onActionExitTriggered(self):
        '''
        退出ACTION事件
        '''
        self.close()

    def onActionTradeFundTriggered(self):
        tradeFundDialog = TradeFundDialog(self)
        tradeFundDialog.exec()

    def onActionAnalyzeIndexTriggered(self):
        analyzeIndexDialog = AnalyzeIndexDialog(self)
        analyzeIndexDialog.exec()

    def onActionSetupFundTriggered(self):
        setupFundDialog = SetupFundDialog(self)
        if setupFundDialog.exec() == QDialog.Accepted:
            self.loadFundList()

    def onActionSetupDataTriggered(self):
        setupDataDialog = SetupDataDialog(self)
        if setupDataDialog.exec() == QDialog.Accepted:
            self.loadFundList()

    def onActionAboutTriggered(self):
        aboutDialog = AboutDialog(self)
        aboutDialog.exec()

    def onActionFundBasicInfoTriggered(self):
        dialog = FundBasicInfoDialog(parent=self, params=self.current_fund)
        dialog.loadData()
        dialog.exec()

    def onActionFundNetValueTriggered(self):
        dialog = FundNetValueDialog(parent=self, params=self.current_fund)
        dialog.loadData(6)
        dialog.exec()

    def onActionFundHoldDataTriggered(self):
        dialog = FundHoldDataDialog(parent=self, params=self.current_fund)
        dialog.loadData()
        dialog.exec()

    def onActionAccountInitTriggered(self):
        dialog = FundAccountInitDialog(parent=self, params=self.current_fund)
        if dialog.exec() == QDialog.Accepted:
            self.showFundAccountData(self.current_fund["code"])

    def onActionFundListWidgetContextMenu(self, pos):
        '''
        基金列表项右键点击事件
        param: pos: 右键点击位置
        '''
        item = self.fundListWidget.itemAt(pos)
        if item is None:
            return
        self.fundListWidgetContextMenu.exec(self.fundListWidget.mapToGlobal(pos))

    def onFundListWidgetItemSelectionChanged(self):
        '''
        基金列表项选择事件
        '''
        item = self.fundListWidget.currentItem()
        if item is None:
            return
        item_data = item.data(Qt.UserRole)
        if item_data is None:
            return
        self.current_fund['code'] = item_data['code']
        self.current_fund['name'] = item_data['name']

        self.statusBar.showMessage(f'已选择 [{self.current_fund["code"]}] {self.current_fund["name"]}')
        self.showFundAccountData(self.current_fund["code"])
        self.showFundNetValueData(self.current_fund["code"])
        self.showFundActionData(self.current_fund["code"])

    def showFundAccountData(self, code):
        '''
        显示基金详情
        param: code: 基金代码
        '''
        # 显示基金持仓表
        held_data = MySQLDB.getFundAccountData(code)
        if held_data is None:
            return

        fund_name = held_data["name"]
        held_cost = float(held_data["held_cost"])
        held_shares = float(held_data["held_shares"])
        self.fundNameLabel.setText(f'{fund_name} [{code}]')
        self.fundHeldCostLabel.setText(f'{held_cost:,.2f}')
        self.fundHeldSharesLabel.setText(f'{held_shares:,.2f}')

        # 显示基金最新净值
        nv_data = MySQLDB.getFundLatestNetValue(code)
        if nv_data is None:
            return
        nv_date = nv_data["trade_date"]
        nv_value = float(nv_data["asset_net_value"])
        nv_growth = float(nv_data["growth_rate"])

        self.fundNVDateLabel.setText(f'{nv_date}')
        self.fundNetValueLabel.setText(f'{nv_value:,.4f}')
        if nv_growth < 0:
            self.fundADRatioLabel.setStyleSheet('font-size:20px; font-weight:bold; color: green;')
        else:
            self.fundADRatioLabel.setStyleSheet('font-size:20px; font-weight:bold; color: red;')
        self.fundADRatioLabel.setText(f'{nv_growth:,.2f}%')

        total_value = nv_value * held_shares
        self.fundTotalLabel.setText(f'{total_value:,.2f}')

        profit_value = total_value - held_cost
        self.fundProfitLabel.setText(f'{profit_value:,.2f}')
        if profit_value < 0:
            self.fundProfitLabel.setStyleSheet('font-size:20px; font-weight:bold; color: green;')
        else:
            self.fundProfitLabel.setStyleSheet('font-size:20px; font-weight:bold; color: red;')

        if held_cost == 0:
            profit_ratio = 0
        else:
            profit_ratio = profit_value / held_cost
        self.fundProfitRatioLabel.setText(f'{profit_ratio*100:,.2f}%')
        if profit_ratio < 0:
            self.fundProfitRatioLabel.setStyleSheet('font-size:20px; font-weight:bold; color: green;')
        else:
            self.fundProfitRatioLabel.setStyleSheet('font-size:20px; font-weight:bold; color: red;')

    def showFundNetValueData(self, code):
        if code is None:
            return
        # 从数据库加载基金持仓数据
        end_date = QDate.currentDate()
        start_date = end_date.addDays(-365)
        data = MySQLDB.getFundNetValue(code, start_date.toString('yyyy-MM-dd'), end_date.toString('yyyy-MM-dd'))
        if data is None:
            return

        # 填充基金持仓数据到表格
        self.anvTableWidget.clearContents()
        self.anvTableWidget.setRowCount(len(data))
        for row, item in enumerate(data):
            for col, value in enumerate(item.values()):
                table_item = QTableWidgetItem(str(value))
                table_item.setData(Qt.UserRole, item)
                table_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.anvTableWidget.setItem(row, col, table_item)

    def showFundActionData(self, code):
        if code is None:
            return

        # 从数据库加载基金持仓数据
        data = MySQLDB.getFundActionData(code)
        if data is None:
            return

        self.actionTableWidget.clearContents()
        self.actionTableWidget.setRowCount(len(data))
        for row, item in enumerate(data):
            for col, value in enumerate(item.values()):
                if col == 1:
                    if value == '买入':
                        value = '买入金额'
                    elif value == '卖出':
                        value = '卖出份额'
                elif col == 2:
                    value = format_float(value, 2)
                table_item = QTableWidgetItem(str(value))
                table_item.setData(Qt.UserRole, item)
                table_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.actionTableWidget.setItem(row, col, table_item)

    def onActionTableWidgetContextMenu(self, pos):
        '''
        基金持仓表项右键点击事件
        param: pos: 右键点击位置
        '''
        table_item = self.actionTableWidget.itemAt(pos)
        if table_item is None:
            self.actionTableWidgetContextMenu.actions()[2].setEnabled(False)
        else:
            item = table_item.data(Qt.UserRole)
            remark = item['remark']
            self.actionTableWidgetContextMenu.actions()[2].setEnabled(remark == '未执行')

        self.actionTableWidgetContextMenu.exec(self.actionTableWidget.mapToGlobal(pos))

    def onActionTradeBuyTriggered(self):
        '''
        买入交易ACTION事件
        '''
        dialog = FundActionDialog(parent=self, params=self.current_fund, mode='买入')
        if dialog.exec() == QDialog.Accepted:
            self.showFundActionData(self.current_fund['code'])

    def onActionTradeSellTriggered(self):
        '''
        卖出交易ACTION事件
        '''
        dialog = FundActionDialog(parent=self, params=self.current_fund, mode='卖出')
        if dialog.exec() == QDialog.Accepted:
            self.showFundActionData(self.current_fund['code'])

    def onActionTradeRevokeTriggered(self):
        '''
        撤销交易ACTION事件
        '''
        code = self.current_fund['code']
        name = self.current_fund['name']

        table_item = self.actionTableWidget.currentItem()
        if table_item is None:
            return
        item = table_item.data(Qt.UserRole)
        action_date = item['action_date']
        if QMessageBox.question(self, '提示', f"是否确定撤销 [{code}] {name} {action_date} 的交易记录?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            MySQLDB.deleteFundActionData(code, action_date)
            self.showFundActionData(code)
