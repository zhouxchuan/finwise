from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtWidgets import QListWidgetItem
from utils.mysqldb import MySQLDB
from ui.SyncDialog_ui import Ui_SyncDialog
from utils.datasource import fundDataSource

class SyncDialog(QDialog, Ui_SyncDialog):
    def __init__(self):
        super(SyncDialog, self).__init__()

        self.selectedItems = None
        self.setupUi(self)

        # 从数据库中获取数据填充到listWidget
        self.fillListWidget()

        self.processDataThread = None
        self.signals = None

    # 填充listWidget
    def fillListWidget(self):
        fund_list = MySQLDB.getFundList()
        self.listWidget.clear()
        for row in fund_list:
            item = QListWidgetItem(row['code'] + ' ' + row['name'])
            item.setData(Qt.UserRole,{'code':row['code'],'name':row['name']})
            self.listWidget.addItem(item)

    # 当表格项选择改变时触发
    def onItemSelectionChanged(self):
        self.selectedItems = self.listWidget.selectedItems()
        self.syncButton.setEnabled(len(self.selectedItems) > 0)

    def onSyncButtonClicked(self):
        self.listWidget.setEnabled(False)
        self.syncButton.setEnabled(False)
        self.progressBar1.setValue(0)
        self.progressBar2.setValue(0)
        self.progressBar3.setValue(0)

        if self.processDataThread:
            if self.processDataThread.isRunning():
                self.processDataThread.quit()
                self.processDataThread.wait(1000)
                if self.processDataThread.isRunning():
                    self.processDataThread.terminate()
                    self.processDataThread.wait()

        self.processDataThread = ProcessDataThread(self.selectedItems)
        self.processDataThread.signalProgress1.connect(self.onThreadProgress1)
        self.processDataThread.signalProgress2.connect(self.onThreadProgress2)
        self.processDataThread.signalProgress3.connect(self.onThreadProgress3)
        self.processDataThread.signalProgressFinished.connect(self.onThreadProgressFinished)
        self.processDataThread.start()

    def closeEvent(self, event):
        # 窗口关闭时确保线程已停止
        if self.processDataThread:
            if self.processDataThread.isRunning():
                self.processDataThread.quit()
                self.processDataThread.wait(1000)
                if self.processDataThread.isRunning():
                    self.processDataThread.terminate()
                    self.processDataThread.wait()

        event.accept()

    def onThreadProgress1(self, value, msg):
        self.progressBar1.setValue(value)
        self.processTip1.setText(msg)

    def onThreadProgress2(self, value, msg):
        self.progressBar2.setValue(value)
        self.processTip2.setText(msg)

    def onThreadProgress3(self, value, msg):
        self.progressBar3.setValue(value)
        self.processTip3.setText(msg)

    def onThreadProgressFinished(self):
        self.listWidget.setEnabled(True)
        self.syncButton.setEnabled(True)
        self.processTip1.setText('基本信息同步完成!')
        self.processTip2.setText('所有历史数据同步完成!')
        self.processTip3.setText('单项历史数据同步完成!')
        self.progressBar1.setValue(100)
        self.progressBar2.setValue(100)
        self.progressBar3.setValue(100)
        
# ------------------------------------------------------------------------------------------
# 提取数据线程
class ProcessDataThread(QThread):
    signalProgress1 = Signal(int,str)
    signalProgress2 = Signal(int,str)
    signalProgress3 = Signal(int,str)
    signalProgressFinished = Signal()

    def __init__(self, items):
        super(ProcessDataThread, self).__init__()
        self.items =  items

    def run(self):

        try:
            selected_total = len(self.items)
            
            # 基本信息
            process1_current = 0
            fields = ['code', 'name','fullname','found_date','scale','company','manager','bank','type','agency','rating','investment_strategy','investment_goal','benchmark']
            for item in self.items:
                code = item.data(Qt.UserRole)['code']
                name = item.data(Qt.UserRole)['name']

                df = fundDataSource.getFundBasic(code)
                if df is not None:
                    # 重新构建DataFrame，让每一行的item值对应fields的值
                    data = {}
                    for index, row in df.iterrows():
                        # 确保有足够的字段对应数据
                        if index < len(fields):
                            item_name = fields[index]
                            item_value = row['value']
                            data[item_name] = item_value
                    
                    # 创建新的DataFrame
                    MySQLDB.setFundBasicData(data)
                process1_current += 100 / selected_total
                self.signalProgress1.emit(process1_current,'正在同步%s(%s)基本信息(%d%%)...' % (name,code,process1_current))
            self.signalProgress1.emit(100,'所有基本信息同步完成!')

            # 历史数据
            process2_current = 0
            for item in self.items:
                code = item.data(Qt.UserRole)['code']
                name = item.data(Qt.UserRole)['name']
                
                self.signalProgress2.emit(process2_current,'正在同步%s(%s)历史数据(%d%%)...' % (name,code,process2_current))            

                df_anv = fundDataSource.getFundAssetNetValues(code)
                df_cnv=fundDataSource.getFundCumulativeNetValues(code)

                anv_size = len(df_anv)
                process3_current=0
                for index, row in df_anv.iterrows():
                    MySQLDB.setFundHistoryAssetNetValues(code,row)
                    process3_current += 100 / anv_size
                    self.signalProgress3.emit(process3_current,'正在同步%s(%s)资产净值(%d%%)...' % (name,code,process3_current))

                cnv_size = len(df_cnv)
                process3_current=0
                for index, row in df_cnv.iterrows():
                    MySQLDB.setFundHistoryCumNetValues(code,row)
                    process3_current += 100 / cnv_size
                    self.signalProgress3.emit(process3_current,'正在同步%s(%s)累计净值(%d%%)...' % (name,code,process3_current))

                self.signalProgress3.emit(100,'同步%s(%s)历史数据完成!' % (name,code))

                process2_current += 100 / selected_total
                self.signalProgress2.emit(process2_current,'正在同步%s(%s)历史数据(%d%%)...' % (name,code,process2_current))

            self.signalProgressFinished.emit()
        except Exception as e:
            print(f'更新数据线程：{e}')
            