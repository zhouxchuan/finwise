from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox
from PySide6.QtCore import Qt, QDate, QDateTime
from ui.TradeFundDialog_ui import Ui_TradeFundDialog
from utils.mysqldb import MySQLDB


# -----------------------------------------------------------------------------
class TradeFundDialog(QDialog, Ui_TradeFundDialog):
    def __init__(self):
        super(TradeFundDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & Qt.WindowMaximizeButtonHint)

        self.startDateEdit.setDate(QDate.currentDate().addDays(-15))
        self.endDateEdit.setDate(QDate.currentDate())

        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

    def onShowButtonClicked(self):
        self.tableWidget.clearContents()

        self.get_code_by_order = {}
        self.get_order_by_code = {}

        fund_ist = MySQLDB.getFundList()
        self.tableWidget.setColumnCount(len(fund_ist))
        for i, item in enumerate(fund_ist):
            item_code = item['code']
            item_order = item['order']
            item_name = item['brief_name']
            self.get_order_by_code[item_code] = item_order
            self.get_code_by_order[item_order] = item_code
            self.tableWidget.setHorizontalHeaderItem(
                item_order, QTableWidgetItem(item_name))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        start_date = self.startDateEdit.date()
        end_date = self.endDateEdit.date()
        days = start_date.daysTo(end_date)
        self.tableWidget.setRowCount(days+1)
        for i in range(0, days+1):
            i_date = start_date.addDays(i)
            row_date = i_date.toString('yyyy-MM-dd')
            self.tableWidget.setVerticalHeaderItem(
                i, QTableWidgetItem(row_date))

            print('DEBUG-%s: %s' %
                  (i, QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss:zzz'),))

            # 礼拜六礼拜天不可编辑
            week_no = i_date.dayOfWeek()
            if week_no == 6 or week_no == 7:
                for j in range(0, self.tableWidget.columnCount()):
                    row_item = QTableWidgetItem()
                    row_item.setFlags(row_item.flags() & ~(
                        Qt.ItemIsEditable | Qt.ItemIsSelectable))
                    self.tableWidget.setItem(i, j, row_item)
            else:
                trade_data = MySQLDB.getFundTradeData(row_date)
                for item in trade_data:
                    item_code = item['code']
                    item_text = item['trade_text']

                    # 查找基金在基金列表中的顺序
                    item_col = self.get_order_by_code.get(item_code, None)
                    if item_col is None:
                        continue

                    row_item = QTableWidgetItem(item_text)
                    row_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(i, item_col, row_item)

        # print('DEBUG-3: %s'% QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss:zzz'))

    def onSaveButtonClicked(self):
        QMessageBox.information(self, '提示', '暂时不支持保存')

    def onTableCellChanged(self, row, col):
        item = self.tableWidget.item(row, col)
        if item is None:
            return
        item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        item_code = self.get_code_by_order.get(col, None)
        if item_code is None:
            return
        item_date = self.tableWidget.verticalHeaderItem(row).text()
        item_text = item.text()
        if item_text == '':
            MySQLDB.removeFundTradeData(item_code, item_date)
        else:
            MySQLDB.setFundTradeData(item_code, item_date, item_text)
