from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QSplitter, QWidget, QSizePolicy, QListWidgetItem, QTableWidgetItem, QHeaderView, QToolTip, QVBoxLayout
from PySide6.QtCore import Qt, Signal, QThread, QMutex
from PySide6.QtGui import QCursor, QPainter, QBrush, QColor, QPen
from PySide6.QtCharts import QChart, QChartView, QValueAxis, QDateTimeAxis, QPieSeries, QSplineSeries
from PySide6.QtCore import QDateTime
from ui.MainWindow_ui import Ui_mainWindow
from LoginDialog import LoginDialog
from TradeFundDialog import TradeFundDialog
from SyncDialog import SyncDialog
from FundsDialog import FundsDialog
from AnalyzeIndexDialog import AnalyzeIndexDialog

from utils.mysqldb import MySQLDB
from utils.datasource import fundDataSource

from datetime import datetime
from classes.KChartView import KChartView

# -----------------------------------------------------------------------------
# 主窗口类
# -----------------------------------------------------------------------------


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('基金分析1.0 [未登录]')
        self.statusBar.showMessage('请先登录验证账户密码')
        self.setContentsMargins(5, 0, 5, 0)

        self.period_map = {
            "半年": 6,
            "一年": 12,
            "三年": 36,
            "五年": 60,
            "成立来": 0
        }

        toolbar_spacer = QWidget()
        toolbar_spacer.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolBar.addWidget(toolbar_spacer)
        self.toolBar.addAction(self.actionExit)

        self.splitter = QSplitter(Qt.Horizontal, childrenCollapsible=False)
        self.splitter.addWidget(self.leftListWidget)
        self.splitter.addWidget(self.fundTabWidget)
        self.setCentralWidget(self.splitter)

        self.fundBasicTableWidget.setHorizontalHeaderLabels(['项目', '内容'])
       # 设置第一列居中对齐，第二列宽度扩展最大宽度
        self.fundBasicTableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.fundBasicTableWidget.setColumnWidth(0, 100)
        self.fundBasicTableWidget.horizontalHeader(
        ).setSectionResizeMode(1, QHeaderView.Stretch)
        self.fundBasicTableWidget.setWordWrap(True)

        self.itemData = None
        self.fundHoldThread = None

        self.fund_name_label.setStyleSheet(
            "font-size: 16px; font-weight: bold;")
        self.fund_code_label.setStyleSheet("font-size: 12px;")
        self.anv_value_label.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #FF0000;")
        self.anv_growthrate_label.setStyleSheet(
            "font-size: 12px; color: #FF0000;")
        self.cnv_value_label.setStyleSheet(
            "font-size: 16px;font-weight: bold;")
        self.nv_lastest_date_label.setStyleSheet("font-size: 12px;")
        self.fundTabWidget.setCurrentIndex(0)

        # 初始化图表
        self.initNetValueChart()
        self.initHoldChart()

    # 初始化净值图表
    def initNetValueChart(self):
        # 创建ANV图表
        self.anv_chart = QChart()
        self.anv_chart.setTitle("单位净值走势图")
        self.anv_chart.setAnimationOptions(QChart.SeriesAnimations)
        self.anv_chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.anv_chart.setBackgroundVisible(True)

        # 创建图表视图
        self.anv_chartview = KChartView(self.anv_chart)
        self.anv_chartview.setRenderHint(QPainter.Antialiasing)

        # 设置图表视图背景为透明
        self.anv_chartview.setStyleSheet("background: transparent;")
        self.anv_chartview.setBackgroundBrush(QBrush(QColor(0, 0, 0, 0)))

        # 设置图表视图的尺寸策略，使其能够扩展填充可用空间
        self.anv_chartview.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.anv_chartview.setMinimumSize(400, 300)  # 设置最小尺寸

        # 设置布局
        anv_layout = self.anvChartWidget.layout()
        if anv_layout is None:
            anv_layout = QVBoxLayout(self.anvChartWidget)
        anv_layout.setContentsMargins(0, 0, 0, 0)  # 移除边距
        anv_layout.setSpacing(0)  # 移除间距
        anv_layout.addWidget(self.anv_chartview)

        # 创建CNV图表
        self.cnv_chart = QChart()
        self.cnv_chart.setTitle("累计净值走势图")
        self.cnv_chart.setAnimationOptions(QChart.SeriesAnimations)
        self.cnv_chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.cnv_chart.setBackgroundVisible(True)

        # 创建图表视图
        self.cnv_chartview = KChartView(self.cnv_chart)
        self.cnv_chartview.setRenderHint(QPainter.Antialiasing)

        # 设置图表视图背景为透明
        self.cnv_chartview.setStyleSheet("background: transparent;")
        self.cnv_chartview.setBackgroundBrush(QBrush(QColor(0, 0, 0, 0)))

        # 设置图表视图的尺寸策略，使其能够扩展填充可用空间
        self.cnv_chartview.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.cnv_chartview.setMinimumSize(400, 300)  # 设置最小尺寸

        # 设置布局
        cnv_layout = self.cnvChartWidget.layout()
        if cnv_layout is None:
            cnv_layout = QVBoxLayout(self.cnvChartWidget)
        cnv_layout.setContentsMargins(0, 0, 0, 0)  # 移除边距
        cnv_layout.setSpacing(0)  # 移除间距
        cnv_layout.addWidget(self.cnv_chartview)

    def initHoldChart(self):

        # -------------------- holdRadio --------------------

        # 创建图表
        self.holdRatioChart = QChart()
        self.holdRatioChart.setTitle("基金持仓比例")
        self.holdRatioChart.setAnimationOptions(QChart.SeriesAnimations)
        self.holdRatioChart.setTheme(QChart.ChartTheme.ChartThemeDark)

        self.holdRatioChart.legend().setVisible(True)
        self.holdRatioChart.legend().setAlignment(Qt.AlignRight)

        # 创建图表视图
        self.holdRatioChartView = QChartView(self.holdRatioChart)
        self.holdRatioChartView.setRenderHint(QPainter.Antialiasing)
        # 设置图表视图背景为透明
        self.holdRatioChartView.setStyleSheet("background: transparent;")
        self.holdRatioChartView.setBackgroundBrush(QBrush(QColor(0, 0, 0, 0)))

        holdRatioLayout = self.holdRatioWidget.layout()
        if holdRatioLayout is None:
            holdRatioLayout = QVBoxLayout(self.holdRatioWidget)
        holdRatioLayout.setContentsMargins(0, 0, 0, 0)
        holdRatioLayout.addWidget(self.holdRatioChartView)

        # -------------------- holdShare --------------------

        # 创建图表
        self.holdShareChart = QChart()
        self.holdShareChart.setTitle("基金持仓股票")
        self.holdShareChart.setAnimationOptions(QChart.SeriesAnimations)
        self.holdShareChart.setTheme(QChart.ChartTheme.ChartThemeBrownSand)
        self.holdShareChart.legend().setVisible(True)
        self.holdShareChart.legend().setAlignment(Qt.AlignRight)

        # 创建图表视图
        self.holdShareChartView = QChartView(self.holdShareChart)
        self.holdShareChartView.setRenderHint(QPainter.Antialiasing)
        # 设置图表视图背景为透明
        self.holdShareChartView.setStyleSheet("background: transparent;")
        self.holdShareChartView.setBackgroundBrush(QBrush(QColor(0, 0, 0, 0)))

        holdShareLayout = self.holdShareWidget.layout()
        if holdShareLayout is None:
            holdShareLayout = QVBoxLayout(self.holdShareWidget)
        holdShareLayout.setContentsMargins(0, 0, 0, 0)
        holdShareLayout.addWidget(self.holdShareChartView)

        # -------------------- holdBond --------------------

        # 创建图表
        self.holdBondChart = QChart()
        self.holdBondChart.setTitle("基金持仓债券")
        self.holdBondChart.setAnimationOptions(QChart.SeriesAnimations)
        self.holdBondChart.setTheme(QChart.ChartTheme.ChartThemeBlueNcs)
        self.holdBondChart.legend().setVisible(True)
        self.holdBondChart.legend().setAlignment(Qt.AlignRight)

        # 创建图表视图
        self.holdBondChartView = QChartView(self.holdBondChart)
        self.holdBondChartView.setRenderHint(QPainter.Antialiasing)
        # 设置图表视图背景为透明
        self.holdBondChartView.setStyleSheet("background: transparent;")
        self.holdBondChartView.setBackgroundBrush(QBrush(QColor(0, 0, 0, 0)))

        holdBondLayout = self.holdBondWidget.layout()
        if holdBondLayout is None:
            holdBondLayout = QVBoxLayout(self.holdBondWidget)
        holdBondLayout.setContentsMargins(0, 0, 0, 0)
        holdBondLayout.addWidget(self.holdBondChartView)

        # -------------------- holdIndustry --------------------

        # 创建图表
        self.holdIndustryChart = QChart()
        self.holdIndustryChart.setTitle("基金持仓行业")
        self.holdIndustryChart.setAnimationOptions(QChart.SeriesAnimations)
        self.holdIndustryChart.setTheme(
            QChart.ChartTheme.ChartThemeBlueCerulean)
        self.holdIndustryChart.legend().setVisible(True)
        self.holdIndustryChart.legend().setAlignment(Qt.AlignRight)

        # 创建图表视图
        self.holdIndustryChartView = QChartView(self.holdIndustryChart)
        self.holdIndustryChartView.setRenderHint(QPainter.Antialiasing)
        # 设置图表视图背景为透明
        self.holdIndustryChartView.setStyleSheet("background: transparent;")
        self.holdIndustryChartView.setBackgroundBrush(
            QBrush(QColor(0, 0, 0, 0)))

        holdIndustryLayout = self.holdIndustryWidget.layout()
        if holdIndustryLayout is None:
            holdIndustryLayout = QVBoxLayout(self.holdIndustryWidget)
        holdIndustryLayout.setContentsMargins(0, 0, 0, 0)
        holdIndustryLayout.addWidget(self.holdIndustryChartView)

    # 加载基金数据
    def loadFundList(self):
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

    # 加载基金净值数据
    def loadFundNetValueData(self, code, period=6):
        from dateutil.relativedelta import relativedelta

        latest_net_value = MySQLDB.getFundLatestNetValue(code)
        if latest_net_value:
            self.anv_value_label.setText(
                f'{latest_net_value["asset_net_value"]}')
            anv_growth_rate = latest_net_value["growth_rate"]
            if anv_growth_rate > 0:
                self.anv_growthrate_label.setStyleSheet(
                    "font-size: 12px; color: #FF0000;")
            elif anv_growth_rate < 0:
                self.anv_growthrate_label.setStyleSheet(
                    "font-size: 12px; color: #00FF00;")
            else:
                self.anv_growthrate_label.setStyleSheet(
                    "font-size: 12px; color: #999999;")
            self.anv_growthrate_label.setText(f'{anv_growth_rate}%')
            self.cnv_value_label.setText(
                f'{latest_net_value["cum_net_value"]}')
            self.nv_lastest_date_label.setText(f'{anv_growth_rate}')
        self.nv_lastest_date_label.setText(f'{latest_net_value["trade_date"]}')

        net_value_data = None
        if period == 0:
            net_value_data = MySQLDB.getFundHistoryNetValues(code)
        else:
            months_ago = datetime.now() - relativedelta(months=period)
            period_date = months_ago.strftime('%Y-%m-%d')
            current_date = datetime.now().strftime('%Y-%m-%d')
            net_value_data = MySQLDB.getFundHistoryNetValues(
                code, start_date=period_date, end_date=current_date)

        if not net_value_data:
            self.statusBar.showMessage(f'没有获取到基金 {code} 的净值数据')
            return

        # 清除之前的图表数据
        self.anv_chart.removeAllSeries()
        self.cnv_chart.removeAllSeries()
        # 清除之前的坐标轴
        anv_axes = self.anv_chart.axes()
        cnv_axes = self.cnv_chart.axes()
        for axis in anv_axes:
            self.anv_chart.removeAxis(axis)
        for axis in cnv_axes:
            self.cnv_chart.removeAxis(axis)

        pen = QPen()

        # 创建单位净值系列
        anv_series = QSplineSeries()
        anv_series.setName("单位净值")
        pen.setColor(QColor(255, 0, 0))
        pen.setWidth(2)
        anv_series.setPen(pen)

        # 创建累计净值系列
        cnv_series = QSplineSeries()
        cnv_series.setName("累计净值")
        pen.setColor(QColor(99, 99, 99))
        pen.setWidth(2)
        cnv_series.setPen(pen)

        # 处理数据
        for data in net_value_data:
            try:
                # 解析日期
                trade_date = data.get('trade_date')
                if trade_date:
                    if isinstance(trade_date, str):
                        date_obj = datetime.strptime(trade_date, '%Y-%m-%d')
                    else:
                        date_obj = trade_date

                    # 转换为QDateTime
                    qdatetime = QDateTime(date_obj)

                    # 获取净值数据
                    anv_values = data.get('asset_net_value', 0)
                    cnv_value = data.get('cum_net_value', 0)

                    if anv_values:
                        anv_series.append(
                            qdatetime.toMSecsSinceEpoch(), float(anv_values))

                    if cnv_value:
                        cnv_series.append(
                            qdatetime.toMSecsSinceEpoch(), float(cnv_value))

            except (ValueError, TypeError) as e:
                print(f"数据解析错误: {e}")
                continue

        # 添加系列到图表
        if anv_series.count() > 0:
            self.anv_chart.addSeries(anv_series)

        if cnv_series.count() > 0:
            self.cnv_chart.addSeries(cnv_series)

        pen.setColor(QColor(55, 55, 55))
        pen.setWidth(1)
        pen.setStyle(Qt.DashLine)

        # 设置X轴（时间轴）
        anv_axis_x = QDateTimeAxis()
        anv_axis_x.setFormat("yyyy-MM-dd")
        anv_axis_x.setTitleText("日期")
        anv_axis_x.setGridLinePen(pen)
        anv_axis_x.setTickCount(10)
        self.anv_chart.addAxis(anv_axis_x, Qt.AlignBottom)

        cnd_axis_x = QDateTimeAxis()
        cnd_axis_x.setFormat("yyyy-MM-dd")
        cnd_axis_x.setTitleText("日期")
        cnd_axis_x.setGridLinePen(pen)
        cnd_axis_x.setTickCount(10)
        self.cnv_chart.addAxis(cnd_axis_x, Qt.AlignBottom)

        # 设置Y轴（净值轴）
        anv_axis_y = QValueAxis()
        anv_axis_y.setTitleText("单位净值")
        anv_axis_y.setLabelFormat("%.2f")
        anv_axis_y.setGridLinePen(pen)
        anv_axis_y.setTickCount(10)
        if anv_series.count() > 0:
            # 计算单位净值的数据范围并设置Y轴范围
            min_anv = min(point.y() for point in anv_series.points())
            max_anv = max(point.y() for point in anv_series.points())
            # 添加一些边距以确保数据完全显示
            margin = (max_anv - min_anv) * 0.1  # 10%的边距
            anv_axis_y.setRange(min_anv - margin, max_anv + margin)
        self.anv_chart.addAxis(anv_axis_y, Qt.AlignLeft)

        cnv_axis_y = QValueAxis()
        cnv_axis_y.setTitleText("单位净值")
        cnv_axis_y.setLabelFormat("%.2f")
        cnv_axis_y.setGridLinePen(pen)
        cnv_axis_y.setTickCount(10)
        # 计算累计净值的数据范围并设置Y轴范围
        if cnv_series.count() > 0:
            min_cnv = min(point.y() for point in cnv_series.points())
            max_cnv = max(point.y() for point in cnv_series.points())
            # 添加一些边距以确保数据完全显示
            margin = (max_cnv - min_cnv) * 0.1  # 10%的边距
            cnv_axis_y.setRange(min_cnv - margin, max_cnv + margin)
        self.cnv_chart.addAxis(cnv_axis_y, Qt.AlignLeft)

        # 将系列附加到坐标轴
        if anv_series.count() > 0:
            anv_series.attachAxis(anv_axis_x)
            anv_series.attachAxis(anv_axis_y)

        if cnv_series.count() > 0:
            cnv_series.attachAxis(cnd_axis_x)
            cnv_series.attachAxis(cnv_axis_y)

        # 创建图例
        self.anv_chart.legend().setVisible(False)
        self.cnv_chart.legend().setVisible(False)

        # 强制刷新图表视图，确保图表充满视图
        self.anv_chartview.update()
        self.cnv_chartview.update()

        self.statusBar.showMessage(
            f'已加载基金 {code} 的净值数据，共 {len(net_value_data)} 条记录')

    # 加载基金持仓数据
    def loadFundHold(self, code):
        # 确保之前的线程已正确停止
        if self.fundHoldThread is not None:
            self.fundHoldThread.signal.disconnect()
            self.fundHoldThread.stop()
            self.fundHoldThread = None

        # 创建新线程并启动
        self.fundHoldThread = FundHoldThread(code)
        self.fundHoldThread.signal.connect(
            self.onFundHoldData, Qt.QueuedConnection)
        self.fundHoldThread.start()

    # 槽函数(处理基金持仓数据信号)
    def onFundHoldData(self, code, hold_ratio, hold_share, hold_bond, hold_industry):

        # ----------------- holdRatio --------------------
        self.holdRatioChart.removeAllSeries()
        if hold_ratio is not None:
            hold_ratio_series = QPieSeries()
            hold_ratio_series.setName("持仓比例")

            # 设置饼图样式：取消边框
            hold_ratio_series.setPieSize(0.8)  # 设置饼图大小
            hold_ratio_series.setHoleSize(0.2)  # 设置中间孔洞大小（可选）

            for index, row in hold_ratio.iterrows():
                asset_type = row['资产类型']
                ratio = row['仓位占比']

                # 创建饼图切片并添加
                slice = hold_ratio_series.append(asset_type, ratio)

                # 设置切片标签显示比例值
                slice.setLabel(f"{asset_type}: {ratio}%")
                slice.setLabelVisible(False)
                slice.setBorderWidth(0)
                slice.setBorderColor(QColor(0, 0, 0, 0))

            self.holdRatioChart.addSeries(hold_ratio_series)
        else:
            self.statusBar.showMessage(f'没有获取到基金 {code} 的持仓比列数据')

        # ----------------- holdShare --------------------
        self.holdShareChart.removeAllSeries()
        if hold_share is not None:
            hold_share_series = QPieSeries()
            hold_share_series.setName("持仓股票")

            # 设置饼图样式：取消边框
            hold_share_series.setPieSize(0.8)  # 设置饼图大小
            hold_share_series.setHoleSize(0.2)  # 设置中间孔洞大小（可选）

            for index, row in hold_share.iterrows():
                if index > 9:
                    break
                stock_name = row['股票名称']
                stock_ratio = row['占净值比例']

                # 创建饼图切片并添加
                slice = hold_share_series.append(stock_name, stock_ratio)

                # 设置切片标签显示比例值
                slice.setLabel(f"{stock_name}: {stock_ratio}%")
                slice.setLabelVisible(False)
                slice.setBorderWidth(0)
                slice.setBorderColor(QColor(0, 0, 0, 0))

            self.holdShareChart.addSeries(hold_share_series)
        else:
            self.statusBar.showMessage(f'没有获取到基金 {code} 的持仓股票数据')

        # ----------------- holdBond --------------------
        self.holdBondChart.removeAllSeries()
        if hold_bond is not None:
            hold_bond_series = QPieSeries()
            hold_bond_series.setName("持仓债券")

            # 设置饼图样式：取消边框
            hold_bond_series.setPieSize(0.8)  # 设置饼图大小
            hold_bond_series.setHoleSize(0.2)  # 设置中间孔洞大小（可选）

            for index, row in hold_bond.iterrows():
                bond_name = row['债券名称']
                bond_ratio = row['占净值比例']

                # 创建饼图切片并添加
                slice = hold_bond_series.append(bond_name, bond_ratio)

                # 设置切片标签显示比例值
                slice.setLabel(f"{bond_name}: {bond_ratio}%")
                slice.setLabelVisible(False)
                slice.setBorderWidth(0)
                slice.setBorderColor(QColor(0, 0, 0, 0))

            self.holdBondChart.addSeries(hold_bond_series)
        else:
            self.statusBar.showMessage(f'没有获取到基金 {code} 的持仓债券数据')

        # ----------------- holdIndustry --------------------
        self.holdIndustryChart.removeAllSeries()
        if hold_industry is not None:
            hold_industry_series = QPieSeries()
            hold_industry_series.setName("持仓行业")

            # 设置饼图样式：取消边框
            hold_industry_series.setPieSize(0.8)  # 设置饼图大小
            hold_industry_series.setHoleSize(0.2)  # 设置中间孔洞大小（可选）

            for index, row in hold_industry.iterrows():
                industry_name = row['行业类别']
                industry_ratio = row['占净值比例']

                # 创建饼图切片并添加
                slice = hold_industry_series.append(
                    industry_name, industry_ratio)

                # 设置切片标签显示比例值
                slice.setLabel(f"{industry_name}: {industry_ratio}%")
                slice.setLabelVisible(False)
                slice.setBorderWidth(0)
                slice.setBorderColor(QColor(0, 0, 0, 0))

            self.holdIndustryChart.addSeries(hold_industry_series)
        else:
            self.statusBar.showMessage(f'没有获取到基金 {code} 的持仓行业数据')

    # 设置登录/注销后界面状态
    def setActionStatus(self, isLoggedIn):
        self.actionLogin.setEnabled(not isLoggedIn)
        self.actionLogout.setEnabled(isLoggedIn)
        self.actionSync.setEnabled(isLoggedIn)
        self.fundListWidget.setEnabled(isLoggedIn)
        self.fundTabWidget.setEnabled(isLoggedIn)

    # 窗口关闭事件
    def closeEvent(self, event):
        if QMessageBox.question(self, '提示', "是否确定退出应用程序?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            if self.fundHoldThread is not None:
                self.fundHoldThread.stop()
                self.fundHoldThread = None
            event.accept()
        else:
            event.ignore()

    # 登录ACTION事件
    def onActionLoginTriggered(self):
        loginDialog = LoginDialog()
        if loginDialog.exec() == QDialog.Accepted:
            self.setWindowTitle(f'基金分析1.0 [{loginDialog.userid}]')
            self.statusBar.showMessage(f'{loginDialog.userid} 已登录', 3000)
            self.setActionStatus(True)

            # 加载基金数据
            self.loadFundList()

    # 注销ACTION事件
    def onActionLogoutTriggered(self):
        self.setWindowTitle('基金分析1.0 [未登录]')
        self.statusBar.showMessage('已注销', 3000)
        self.setActionStatus(False)

    # 退出ACTION事件
    def onActionExitTriggered(self):
        self.close()

    def onActionTradeFundTriggered(self):
        tradeFundDialog = TradeFundDialog()
        tradeFundDialog.exec()

    def onActionAnalyzeIndexTriggered(self):
        analyzeIndexDialog = AnalyzeIndexDialog()
        analyzeIndexDialog.exec()

    # 设置ACTION事件
    def onActionSetupTriggered(self):
        fundsDialog = FundsDialog()
        if fundsDialog.exec() == QDialog.Accepted:
            self.loadFundList()

    # 更新数据ACTION事件
    def onActionSyncTriggered(self):
        syncDialog = SyncDialog()
        syncDialog.exec()

    # 基金列表项点击事件
    def onCurrentRowChanged(self, currentRow):
        if currentRow < 0:
            return

        item = self.fundListWidget.item(currentRow)
        self.itemData = item.data(Qt.UserRole)
        if self.itemData is None:
            self.statusBar.showMessage('请选择基金项')
            return
        item_code = self.itemData['code']
        item_name = self.itemData['name']

        self.statusBar.showMessage(f'选中了 {item_name} [{item_code}]')
        self.fundBasicTableWidget.setRowCount(0)

        fund_basic_item = MySQLDB.getFundBasicData(item_code)
        if fund_basic_item is None:
            self.statusBar.showMessage(
                f'没有获取到 {self.itemData["name"]} [{self.itemData["code"]}] 的基本数据')
            return

        # 定义要显示的数据行
        rows = [
            {'item': '基金代码', 'content': fund_basic_item['code']},
            {'item': '基金名称', 'content': fund_basic_item['name']},
            {'item': '基金全称', 'content': fund_basic_item['fullname']},
            {'item': '成立日期', 'content': fund_basic_item['found_date']},
            {'item': '基金规模', 'content': fund_basic_item['scale']},
            {'item': '基金公司', 'content': fund_basic_item['company']},
            {'item': '基金经理', 'content': fund_basic_item['manager']},
            {'item': '托管银行', 'content': fund_basic_item['bank']},
            {'item': '基金类型', 'content': fund_basic_item['type']},
            {'item': '评级机构', 'content': fund_basic_item['agency']},
            {'item': '基金评级', 'content': fund_basic_item['rating']},
            {'item': '投资策略',
                'content': fund_basic_item['investment_strategy']},
            {'item': '投资目标', 'content': fund_basic_item['investment_goal']},
            {'item': '业绩比较基准', 'content': fund_basic_item['benchmark']}
        ]

        # 设置表格行数
        self.fundBasicTableWidget.setRowCount(len(rows))

        # 将rows数据填入fundBasicTableWidget
        for i, row in enumerate(rows):
            # 第一列：项目名称，居中对齐
            item0 = QTableWidgetItem(row['item'])
            item0.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.fundBasicTableWidget.setItem(i, 0, item0)

            # 第二列：内容，处理空值
            value = row['content'] if row['content'] is not None and row['content'] != '' else ''
            item1 = QTableWidgetItem(str(value))
            item1.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.fundBasicTableWidget.setItem(i, 1, item1)

        self.fund_name_label.setText(item_name)
        self.fund_code_label.setText(item_code)
        self.loadFundNetValueData(item_code)
        self.periodRadioButton1.setChecked(True)
        self.loadFundHold(item_code)

    def onFundBasicTableWidgetCellEntered(self, row, column):
        if column == 1 and row > 10:
            item = self.fundBasicTableWidget.item(row, column)
            if item is not None:
                QToolTip.showText(QCursor.pos(), item.text())

    def onFundNetValuePeriodChanged(self):
        code = self.itemData['code']

        if self.periodRadioButton1.isChecked():
            self.loadFundNetValueData(code, self.period_map["半年"])
        elif self.periodRadioButton2.isChecked():
            self.loadFundNetValueData(code, self.period_map["一年"])
        elif self.periodRadioButton3.isChecked():
            self.loadFundNetValueData(code, self.period_map["三年"])
        elif self.periodRadioButton4.isChecked():
            self.loadFundNetValueData(code, self.period_map["五年"])
        elif self.periodRadioButton5.isChecked():
            self.loadFundNetValueData(code, self.period_map["成立来"])
        else:
            self.statusBar.showMessage('请选择时间范围')

# -----------------------------------------------------------------------------
# 获取基金持仓数据线程
# -----------------------------------------------------------------------------


class FundHoldThread(QThread):
    # 正确的信号定义应该在类级别
    signal = Signal(str, object, object, object, object)

    def __init__(self, code):
        super().__init__()
        self.code = code
        self.isWorking = True
        self._mutex = QMutex()  # 添加互斥锁

    def run(self):
        try:
            if not self.isWorking:
                return

            hold_ratio = fundDataSource.getFundHoldRatio(self.code)
            hold_share = fundDataSource.getFundHoldShare(self.code)
            hold_bond = fundDataSource.getFundHoldBond(self.code)
            hold_industry = fundDataSource.getFundHoldIndustry(self.code)
            if not self.isWorking:
                return

            self.signal.emit(self.code, hold_ratio, hold_share,
                             hold_bond, hold_industry)
        except Exception as e:
            print(f'获取基金持仓数据失败：{e}')
        finally:
            self.isWorking = False

    def stop(self):
        self._mutex.lock()  # 加锁
        self.isWorking = False
        self._mutex.unlock()

        if self.isRunning():
            self.quit()
            if not self.wait(1000):
                self.terminate()
                self.wait(500)
