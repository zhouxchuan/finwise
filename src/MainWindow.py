from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QSplitter, QWidget, QSizePolicy, QListWidgetItem, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

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

from utils.mysqldb import MySQLDB


class MainWindow(QMainWindow, Ui_mainWindow):
    '''
    主窗口类
    '''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.userid = None

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

        self.fundTabelLabel.setText('[未选择基金]')

        self.fundListWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fundListWidget.customContextMenuRequested.connect(self.onFundListWidgetContextMenu)
        self.fundListWidgetContextMenu = QMenu(self)
        self.fundListWidgetContextMenu.addAction(QAction(u'基本信息', self, triggered=self.onActionFundBasicInfoTriggered))
        self.fundListWidgetContextMenu.addAction(QAction(u'净值数据', self, triggered=self.onActionFundNetValueTriggered))
        self.fundListWidgetContextMenu.addAction(QAction(u'基金持仓', self, triggered=self.onActionFundHoldDataTriggered))

    def setActionStatus(self, isLoggedIn):
        '''
        设置登录/注销后界面状态
        param: isLoggedIn: 登录状态
        '''
        self.actionLogin.setEnabled(not isLoggedIn)
        self.actionLogout.setEnabled(isLoggedIn)
        self.actionSync.setEnabled(isLoggedIn)
        self.leftWidget.setEnabled(isLoggedIn)
        self.rightWidget.setEnabled(isLoggedIn)

        if isLoggedIn:
            self.statusBar.showMessage(f'{self.userid} 已登录', 3000)
        else:
            self.userid = None
            self.setWindowTitle('基金分析1.0 [未登录]')
            self.statusBar.showMessage('请先登录验证账户密码')
            self.fundListWidget.clear()
            self.fundTabelLabel.setText('[未选择基金]')
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
        item = self.fundListWidget.currentItem()
        if item is None:
            return
        item_data = item.data(Qt.UserRole)
        if item_data is None:
            return
        dialog = FundBasicInfoDialog(parent=self, params=item_data)
        dialog.loadData()
        dialog.exec()

    def onActionFundNetValueTriggered(self):
        item = self.fundListWidget.currentItem()
        if item is None:
            return
        item_data = item.data(Qt.UserRole)
        if item_data is None:
            return
        dialog = FundNetValueDialog(parent=self, params=item_data)
        dialog.loadData(6)
        dialog.exec()

    def onActionFundHoldDataTriggered(self):
        item = self.fundListWidget.currentItem()
        if item is None:
            return
        item_data = item.data(Qt.UserRole)
        if item_data is None:
            return
        dialog = FundHoldDataDialog(parent=self, params=item_data)
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
        item_code = item_data['code']
        item_name = item_data['name']
        self.fundTabelLabel.setText(f'[{item_code}] {item_name}')

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
