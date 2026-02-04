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

    def onCancelButtonClicked(self):
        self.close()

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
        self.isWorking = False

    def setParams(self, items):
        self.items = items

    def stop(self):
        self.isWorking = False
        self.wait(1000)
        if self.isRunning():
            self.terminate()
            self.wait()

    def run(self):
        try:
            self.isWorking = True
            selected_total = len(self.items)

            # 基本信息
            process1_current = 0
            for item in self.items:
                if not self.isWorking:
                    print('基本信息同步被中断!')
                    break
                item_data = item.data(Qt.UserRole)
                code = item_data['code']
                name = item_data['name']
                result = fundDataSource.getFundBasic(code)
                if result:
                    MySQLDB.setFundAccountBasicInfo(code, result)
                process1_current += 100 / selected_total
                self.Progress1Event.emit(process1_current, '正在同步%s(%s)基本信息(%d%%)...' % (name, code, process1_current))
            self.Progress1Event.emit(100, '所有基本信息同步完成!')

            # 历史数据
            process2_current = 0
            for item in self.items:
                if not self.isWorking:
                    print('历史数据同步被中断!')
                    break
                item_data = item.data(Qt.UserRole)
                code = item_data['code']
                name = item_data['name']

                self.Progress2Event.emit(process2_current, '正在同步%s(%s)历史数据(%d%%)...' % (name, code, process2_current))

                df_anv = fundDataSource.getFundAssetNetValues(code)
                df_cnv = fundDataSource.getFundCumulativeNetValues(code)

                anv_size = len(df_anv)
                process3_current = 0
                for index, row in df_anv.iterrows():
                    if not self.isWorking:
                        print('资产净值同步被中断!')
                        break
                    MySQLDB.setFundHistoryAssetNetValues(code, row)
                    process3_current += 100 / anv_size
                    self.Progress3Event.emit(process3_current, '正在同步%s(%s)资产净值(%d%%)...' % (name, code, process3_current))

                cnv_size = len(df_cnv)
                process3_current = 0
                for index, row in df_cnv.iterrows():
                    if not self.isWorking:
                        print('累计净值同步被中断!')
                        break
                    MySQLDB.setFundHistoryCumNetValues(code, row)
                    process3_current += 100 / cnv_size
                    self.Progress3Event.emit(process3_current, '正在同步%s(%s)累计净值(%d%%)...' % (name, code, process3_current))

                self.Progress3Event.emit(100, '同步%s(%s)历史数据完成!' % (name, code))

                process2_current += 100 / selected_total
                self.Progress2Event.emit(process2_current, '正在同步%s(%s)历史数据(%d%%)...' % (name, code, process2_current))

            self.ProgressFinishedEvent.emit()
        except Exception as e:
            print(f'ProcessDataThread运行异常：{e}')

        self.isWorking = False
