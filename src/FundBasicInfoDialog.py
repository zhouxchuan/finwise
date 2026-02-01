from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt
from ui.FundBasicInfoDialog_ui import Ui_FundBasicInfoDialog
from utils.mysqldb import MySQLDB


class FundBasicInfoDialog(QDialog, Ui_FundBasicInfoDialog):
    def __init__(self, parent=None, params={'code': None, 'name': None}):
        super(FundBasicInfoDialog, self).__init__(parent)
        self.setupUi(self)
        self.code = params['code']
        self.name = params['name']

        self.tableWidget.setHorizontalHeaderLabels(['项目', '内容'])
       # 设置第一列居中对齐，第二列宽度扩展最大宽度
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.setWordWrap(True)

    def loadData(self):
        self.tableWidget.setRowCount(0)

        data = MySQLDB.getFundBasicData(self.code)
        if data is None:
            return

        # 定义要显示的数据行
        rows = [
            {'item': '基金代码', 'content': data['code']},
            {'item': '基金名称', 'content': data['name']},
            {'item': '基金全称', 'content': data['fullname']},
            {'item': '成立日期', 'content': data['found_date']},
            {'item': '基金规模', 'content': data['scale']},
            {'item': '基金公司', 'content': data['company']},
            {'item': '基金经理', 'content': data['manager']},
            {'item': '托管银行', 'content': data['bank']},
            {'item': '基金类型', 'content': data['type']},
            {'item': '基金评级', 'content': data['rating']},
            {'item': '投资策略', 'content': data['investment_strategy']},
            {'item': '投资目标', 'content': data['investment_goal']},
            {'item': '业绩比较基准', 'content': data['benchmark']}
        ]

        # 设置表格行数
        self.tableWidget.setRowCount(len(rows))

        # 将rows数据填入fundBasicTableWidget
        for i, row in enumerate(rows):
            # 第一列：项目名称，居中对齐
            item0 = QTableWidgetItem(row['item'])
            item0.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tableWidget.setItem(i, 0, item0)

            # 第二列：内容，处理空值
            value = row['content'] if row['content'] is not None and row['content'] != '' else ''
            item1 = QTableWidgetItem(str(value))
            item1.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.tableWidget.setItem(i, 1, item1)
