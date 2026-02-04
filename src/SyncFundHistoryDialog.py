from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtWidgets import QListWidgetItem
from utils.mysqldb import MySQLDB
from ui.SyncFundHistoryDialog_ui import Ui_SyncFundHistoryDialog
from utils.datasource import fundDataSource


class SyncFundHistoryDialog(QDialog, Ui_SyncFundHistoryDialog):
    def __init__(self, parent=None):
        super(SyncFundHistoryDialog, self).__init__(parent)

        # self.selectedItems = None
        self.setupUi(self)

        # 从数据库中获取数据填充到listWidget
        self.fillListWidget()

        self.processDataThread = ProcessDataThread()
        self.processDataThread.Progress1Event.connect(self.onProgress1Event)
        self.processDataThread.Progress2Event.connect(self.onProgress2Event)
        self.processDataThread.Progress3Event.connect(self.onProgress3Event)
        self.processDataThread.ProgressFinishedEvent.connect(self.onProgressFinishedEvent)

    # 填充listWidget
    def fillListWidget(self):
        fund_list = MySQLDB.getFundAccountList()
        self.listWidget.clear()
        for item in fund_list:
            list_item = QListWidgetItem(item['code'] + ' ' + item['name'])
            list_item.setData(Qt.UserRole, {'code': item['code'], 'name': item['name']})
            self.listWidget.addItem(list_item)

    # 当表格项选择改变时触发
    def onItemSelectionChanged(self):
        # self.selectedItems = self.listWidget.selectedItems()
        self.syncButton.setEnabled(len(self.listWidget.selectedItems()) > 0)

    def onSyncButtonClicked(self):
        self.listWidget.setEnabled(False)
        self.syncButton.setEnabled(False)
        self.progressBar1.setValue(0)
        self.progressBar2.setValue(0)
        self.progressBar3.setValue(0)

        self.processDataThread.stop()
        self.processDataThread.setParams(self.listWidget.selectedItems())
        self.processDataThread.start()

    def closeEvent(self, event):
        # 窗口关闭时确保线程已停止
        self.processDataThread.stop()
        event.accept()

    def onProgress1Event(self, value, msg):
        self.progressBar1.setValue(value)
        self.processTip1.setText(msg)

    def onProgress2Event(self, value, msg):
        self.progressBar2.setValue(value)
        self.processTip2.setText(msg)

    def onProgress3Event(self, value, msg):
        self.progressBar3.setValue(value)
        self.processTip3.setText(msg)

    def onProgressFinishedEvent(self):
        self.listWidget.setEnabled(True)
        self.syncButton.setEnabled(True)
        self.processTip1.setText('基本信息同步完成!')
        self.processTip2.setText('所有历史数据同步完成!')
        self.processTip3.setText('单项历史数据同步完成!')
        self.progressBar1.setValue(100)
        self.progressBar2.setValue(100)
        self.progressBar3.setValue(100)

# ------------------------------------------------------------------------------------------


class ProcessDataThread(QThread):
    '''
    提取数据线程
    '''
    Progress1Event = Signal(int, str)
    Progress2Event = Signal(int, str)
    Progress3Event = Signal(int, str)
    ProgressFinishedEvent = Signal()

    def __init__(self):
        super(ProcessDataThread, self).__init__()

    def setParams(self, items):
        self.items = items

    def stop(self):
        self.quit()
        self.wait(1000)
        if self.isRunning():
            self.terminate()
            self.wait()

    def run(self):
        try:
            selected_total = len(self.items)

            # 基本信息
            process1_current = 0
            for item in self.items:
                code = item.data(Qt.UserRole)['code']
                name = item.data(Qt.UserRole)['name']
                result = fundDataSource.getFundBasic(code)
                if result is not None:
                    data = {
                        '基金代码': code,
                        '基金名称': name,
                        '基金全称': result.get('基金全称', '无'),
                        '成立时间': result.get('成立时间', '无'),
                        '最新规模': result.get('最新规模', '无'),
                        '基金公司': result.get('基金公司', '无'),
                        '基金经理': result.get('基金经理', '无'),
                        '托管银行': result.get('托管银行', '无'),
                        '基金类型': result.get('基金类型', '无'),
                        '评级机构': result.get('评级机构', '无'),
                        '基金评级': result.get('基金评级', '无'),
                        '投资策略': result.get('投资策略', '无'),
                        '投资目标': result.get('投资目标', '无'),
                        '业绩比较基准': result.get('业绩比较基准', '无'),
                    }
                    MySQLDB.setFundAccountBasicInfo(code, data)
                process1_current += 100 / selected_total
                self.Progress1Event.emit(process1_current, '正在同步%s(%s)基本信息(%d%%)...' % (name, code, process1_current))
            self.Progress1Event.emit(100, '所有基本信息同步完成!')

            # 历史数据
            process2_current = 0
            for item in self.items:
                code = item.data(Qt.UserRole)['code']
                name = item.data(Qt.UserRole)['name']

                self.Progress2Event.emit(process2_current, '正在同步%s(%s)历史数据(%d%%)...' % (name, code, process2_current))

                df_anv = fundDataSource.getFundAssetNetValues(code)
                df_cnv = fundDataSource.getFundCumulativeNetValues(code)

                anv_size = len(df_anv)
                process3_current = 0
                for index, row in df_anv.iterrows():
                    MySQLDB.setFundHistoryAssetNetValues(code, row)
                    process3_current += 100 / anv_size
                    self.Progress3Event.emit(process3_current, '正在同步%s(%s)资产净值(%d%%)...' % (name, code, process3_current))

                cnv_size = len(df_cnv)
                process3_current = 0
                for index, row in df_cnv.iterrows():
                    MySQLDB.setFundHistoryCumNetValues(code, row)
                    process3_current += 100 / cnv_size
                    self.Progress3Event.emit(process3_current, '正在同步%s(%s)累计净值(%d%%)...' % (name, code, process3_current))

                self.Progress3Event.emit(100, '同步%s(%s)历史数据完成!' % (name, code))

                process2_current += 100 / selected_total
                self.Progress2Event.emit(process2_current, '正在同步%s(%s)历史数据(%d%%)...' % (name, code, process2_current))

            self.ProgressFinishedEvent.emit()
        except Exception as e:
            print(f'ProcessDataThread运行异常：{e}')
