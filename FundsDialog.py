from PySide6.QtWidgets import QDialog, QListWidgetItem, QMessageBox
from PySide6.QtCore import Qt, QThread, QObject, Signal
from ui.FundsDialog_ui import Ui_FundsDialog
from utils.datasource import fundDataSource
from utils.mysqldb import MySQLDB

# -----------------------------------------------------------------------------
# 工作线程类，用于在后台获取基金数据
class DataFetchThread(QThread):
    # 定义信号，用于传递数据和状态
    data_fetched = Signal(list)  # 传递基金数据列表
    fetch_error = Signal(str)    # 传递错误信息

    def run(self):
        try:
            # 从数据源获取所有基金
            df = fundDataSource.getAllFunds()
            fund_data = []
            for index, row in df.iterrows():
                # if '易方达' not in row['name']:
                #     continue
                fund_data.append({
                    'code': row['code'],
                    'name': row['name']
                })
            self.data_fetched.emit(fund_data)
        except Exception as e:
            self.fetch_error.emit(str(e))

# -----------------------------------------------------------------------------
# 基金对话框类
class FundsDialog(QDialog, Ui_FundsDialog):
    def __init__(self):
        super(FundsDialog, self).__init__()
        self.setupUi(self)
        
        # 创建线程实例
        self.data_thread = None
        # 存储初始基金清单数据
        self.initial_funds = []        
        
        # 连接信号槽
        self.initConnections()
        
        # 填充数据
        self.fillLeftListWidget()
        self.fillRightListWidget()

    def initConnections(self):
        pass  # 可以在这里添加其他信号槽连接

    def fillLeftListWidget(self):
        # 显示加载提示
        self.leftListWidget.clear()
        loading_item = QListWidgetItem("正在加载数据...")
        self.leftListWidget.addItem(loading_item)
        
        # 创建并启动数据获取线程
        self.data_thread = DataFetchThread()
        self.data_thread.data_fetched.connect(self.onDataFetched)
        self.data_thread.fetch_error.connect(self.onDataFetchError)
        self.data_thread.finished.connect(self.onThreadFinished)
        self.data_thread.start()

    def fillRightListWidget(self):
        self.rightListWidget.clear()
        # 从数据库中获取已选择的基金
        funds = MySQLDB.getFundList()
        # 更新初始基金清单数据
        self.initial_funds = [{'code': fund['code'], 'name': fund['name']} for fund in funds]
          
        for fund in funds:
            item = QListWidgetItem(fund['code'] + ' ' + fund['name'])
            item.setData(Qt.UserRole, {'code': fund['code'], 'name': fund['name']})
            self.rightListWidget.addItem(item)

    def onDataFetched(self, fund_data):
        # 清空列表并填充数据
        self.leftListWidget.clear()
        for fund in fund_data:
            item = QListWidgetItem(fund['code'] + ' ' + fund['name'])
            item.setData(Qt.UserRole, {'code': fund['code'], 'name': fund['name']})
            self.leftListWidget.addItem(item)

    def onDataFetchError(self, error_message):
        # 显示错误信息
        self.leftListWidget.clear()
        error_item = QListWidgetItem("加载失败，请稍后重试")
        self.leftListWidget.addItem(error_item)
        QMessageBox.warning(self, "错误", f"加载基金数据失败：{error_message}")

    def onThreadFinished(self):
        # 线程结束后清理资源
        self.data_thread = None

    def onAddButtonClicked(self):
        # 获取allListWidget中所有选中的项
        selected_items = self.leftListWidget.selectedItems()
    
        if not selected_items:
            QMessageBox.information(self, "提示", "请先选择要添加的基金")
            return
        
        # 将选中的项添加到rightListWidget中
        for item in selected_items:
            # 获取项的数据  
            fund_data = item.data(Qt.UserRole)
            code = fund_data['code']
            name = fund_data['name']
        
            # 检查该项是否已存在于rightListWidget中
            exists = False
            for i in range(self.rightListWidget.count()):
                existing_item = self.rightListWidget.item(i)
                existing_data = existing_item.data(Qt.UserRole)
                if existing_data['code'] == code:
                    exists = True
                    break
        
            # 如果不存在，则添加
            if not exists:
                new_item = QListWidgetItem(code + ' ' + name)
                new_item.setData(Qt.UserRole, {'code': code, 'name': name})
                self.rightListWidget.addItem(new_item)

    def onRemoveButtonClicked(self):
        # 获取rightListWidget中所有选中的项
        selected_items = self.rightListWidget.selectedItems()
        
        if not selected_items:
            QMessageBox.information(self, "提示", "请先选择要移除的基金")
            return
        
        # 将选中的项从rightListWidget中移除
        for item in selected_items:
            self.rightListWidget.takeItem(self.rightListWidget.row(item))

    def onSaveButtonClicked(self):
        # 获取当前右侧列表中的基金数据
        current_funds = []
        for i in range(self.rightListWidget.count()):
            item = self.rightListWidget.item(i)
            fund_data = item.data(Qt.UserRole)
            current_funds.append({'code': fund_data['code'], 'name': fund_data['name']})
        
        # 将基金列表转换为以code为键的字典，便于比较
        initial_funds_dict = {fund['code']: fund for fund in self.initial_funds}
        current_funds_dict = {fund['code']: fund for fund in current_funds}
        
        # 找出新增的基金（在当前列表但不在初始列表中）
        added_funds = []
        for code, fund in current_funds_dict.items():
            if code not in initial_funds_dict:
                added_funds.append(fund)
        
        # 找出删除的基金（在初始列表但不在当前列表中）
        removed_funds = []
        for code, fund in initial_funds_dict.items():
            if code not in current_funds_dict:
                removed_funds.append(fund)
        
        # 同步数据库
        try:
            # 添加新增的基金
            for fund in added_funds:
                MySQLDB.setFundItem(fund['code'], fund['name'])
            
            # 删除移除的基金
            for fund in removed_funds:
                MySQLDB.deleteFundItem(fund['code'])
            
            # 更新初始基金清单数据
            self.initial_funds = current_funds.copy()
            
            # 显示操作结果
            if added_funds or removed_funds:
                message = ""
                if added_funds:
                    message += f"新增了 {len(added_funds)} 个基金\n"
                if removed_funds:
                    message += f"删除了 {len(removed_funds)} 个基金\n"
                QMessageBox.information(self, "保存成功", f"数据已同步到数据库：\n{message}")

                QDialog.accept(self)
            else:
                QMessageBox.information(self, "提示", "没有需要同步的数据")
                
        except Exception as e:
            QMessageBox.critical(self, "错误", f"同步数据失败：{str(e)}")

    def closeEvent(self, event):
        # 窗口关闭时确保线程已停止
        if self.data_thread and self.data_thread.isRunning():
            self.data_thread.quit()
            self.data_thread.wait()
        event.accept()