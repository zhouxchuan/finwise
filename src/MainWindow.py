from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QSplitter, QWidget, QSizePolicy, QListWidgetItem, QMenu, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

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
        self.fundListWidget.customContextMenuRequested.connect(self.onFundListWidgetContextMenu)
        self.fundListWidgetContextMenu = QMenu(self)
        self.fundListWidgetContextMenu.addAction(QAction(u'基本信息', self, triggered=self.onActionFundBasicInfoTriggered))
        self.fundListWidgetContextMenu.addAction(QAction(u'净值数据', self, triggered=self.onActionFundNetValueTriggered))
        self.fundListWidgetContextMenu.addAction(QAction(u'基金持仓', self, triggered=self.onActionFundHoldDataTriggered))

        self.fundTableWidget.setEnabled(False)
        self.fundTableWidget.setColumnCount(6)
        self.fundTableWidget.setHorizontalHeaderLabels(['日期', '买/卖', '金额', '份额', '净值', '标注'])
        self.fundTableWidget.setRowCount(0)
        self.fundTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.fundTableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fundTableWidget.customContextMenuRequested.connect(self.onFundTableWidgetContextMenu)
        self.fundTableWidgetContextMenu = QMenu(self)
        self.fundTableWidgetContextMenu.addAction(QAction(u'添加记录', self, triggered=self.onActionFundAddRecordTriggered))
        self.fundTableWidgetContextMenu.addAction(QAction(u'更新记录', self, triggered=self.onActionFundUpdateRecordTriggered))
        self.fundTableWidgetContextMenu.addAction(QAction(u'删除记录', self, triggered=self.onActionFundDeleteRecordTriggered))

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
        self.fundTableWidget.setEnabled(isLoggedIn)

        if isLoggedIn:
            self.statusBar.showMessage(f'{self.userid} 已登录', 3000)
        else:
            self.userid = None
            self.setWindowTitle('基金分析1.0 [未登录]')
            self.statusBar.showMessage('请先登录验证账户密码')
            self.fundListWidget.clear()
            self.fundNameLabel.setText('[未选择基金]')
            self.fundTableWidget.clearContents()
            self.fundTableWidget.setRowCount(0)

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

    def onFundListWidgetContextMenu(self, pos):
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
        self.fundProfitRatioLabel.setText(f'{profit_ratio:,.2f}%')
        if profit_ratio < 0:
            self.fundProfitRatioLabel.setStyleSheet('font-size:20px; font-weight:bold; color: green;')
        else:
            self.fundProfitRatioLabel.setStyleSheet('font-size:20px; font-weight:bold; color: red;')

    def showFundActionData(self, code):
        self.fundTableWidget.clearContents()
        self.fundTableWidget.setRowCount(0)
        if code is None:
            return
        # 从数据库加载基金持仓数据
        data = MySQLDB.getFundActionData(code)
        self.fundTableWidget.setRowCount(len(data))
        for row, item in enumerate(data):
            for col, value in enumerate(item.values()):
                item = QTableWidgetItem(str(value))
                item.setData(Qt.UserRole, item)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.fundTableWidget.setItem(row, col, item)

    def onFundTableWidgetContextMenu(self, pos):
        '''
        基金持仓表项右键点击事件
        param: pos: 右键点击位置
        '''
        item = self.fundTableWidget.itemAt(pos)
        if item is None:
            self.fundListWidgetContextMenu.actions()[0].setEnabled(True)
            self.fundTableWidgetContextMenu.actions()[1].setEnabled(False)
            self.fundTableWidgetContextMenu.actions()[2].setEnabled(False)
        else:
            self.fundListWidgetContextMenu.actions()[0].setEnabled(True)
            self.fundTableWidgetContextMenu.actions()[1].setEnabled(True)
            self.fundTableWidgetContextMenu.actions()[2].setEnabled(True)
        self.fundTableWidgetContextMenu.exec(self.fundTableWidget.mapToGlobal(pos))

    def onActionFundAddRecordTriggered(self):
        '''
        添加基金持仓记录ACTION事件
        '''
        dialog = FundActionDialog(parent=self, params=self.current_fund, mode='add')
        if dialog.exec() == QDialog.Accepted:
            self.showFundAccountData(self.current_fund['code'])

    def onActionFundUpdateRecordTriggered(self):
        '''
        修改基金持仓记录ACTION事件
        '''

        item = self.fundTableWidget.currentItem()
        if item is None:
            return
        row = item.row()

        action_date = self.fundTableWidget.item(row, 0).text()
        action_type = self.fundTableWidget.item(row, 1).text()
        cost_amount = self.fundTableWidget.item(row, 2).text()
        share_amount = self.fundTableWidget.item(row, 3).text()
        net_value = self.fundTableWidget.item(row, 4).text()
        remark = self.fundTableWidget.item(row, 5).text()

        params = {'code': self.current_fund['code'],
                  'name': self.current_fund['name'],
                  'action_date': action_date,
                  'action_type': action_type,
                  'cost_amount': cost_amount,
                  'share_amount': share_amount,
                  'net_value': net_value,
                  'remark': remark}
        dialog = FundActionDialog(parent=self, params=params, mode='update')
        if dialog.exec() == QDialog.Accepted:
            self.showFundAccountData(self.current_fund['code'])

    def onActionFundDeleteRecordTriggered(self):
        '''
        删除基金持仓记录ACTION事件
        '''
        code = self.current_fund['code']
        name = self.current_fund['name']

        item = self.fundTableWidget.currentItem()
        if item is None:
            return
        row = item.row()
        action_date = self.fundTableWidget.item(row, 0).text()
        if QMessageBox.question(self, '提示', f"是否确定删除 [{code}] {name} {action_date} 的持仓记录?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            MySQLDB.deleteFundActionData(code, action_date)
            self.showFundAccountData(code)
            self.statusBar.showMessage(f'已删除 [{code}] {name} {action_date} 的持仓记录', 3000)
