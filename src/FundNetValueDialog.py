from PySide6.QtWidgets import QDialog, QSizePolicy, QVBoxLayout, QButtonGroup
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtCharts import QChart, QValueAxis, QSplineSeries, QDateTimeAxis
from ui.FundNetValueDialog_ui import Ui_FundNetValueDialog
from utils.mysqldb import MySQLDB
from classes.KChartView import KChartView
from datetime import datetime
from dateutil.relativedelta import relativedelta


class FundNetValueDialog(QDialog, Ui_FundNetValueDialog):
    def __init__(self, parent=None, params={'code': None, 'name': None}):
        super(FundNetValueDialog, self).__init__(parent)
        self.setupUi(self)
        self.code = params['code']
        self.name = params['name']

        # 初始化框架
        self.initFrame()

        # 初始化图表
        self.initChart()

    def initFrame(self):
        self.fund_name_label.setText(self.name)
        self.fund_code_label.setText(self.code)

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

        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.periodRadioButton1)
        self.buttonGroup.addButton(self.periodRadioButton2)
        self.buttonGroup.addButton(self.periodRadioButton3)
        self.buttonGroup.addButton(self.periodRadioButton4)
        self.buttonGroup.addButton(self.periodRadioButton5)
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.buttonClicked.connect(self.onPeriodRadioButtonClicked)

    def initChart(self):
        '''
        初始化净值图表
        '''
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

    def loadData(self, period=6):
        '''
        加载基金净值数据
        '''
        latest_net_value = MySQLDB.getFundLatestNetValue(self.code)
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
            net_value_data = MySQLDB.getFundHistoryNetValues(self.code)
        else:
            months_ago = datetime.now() - relativedelta(months=period)
            period_date = months_ago.strftime('%Y-%m-%d')
            current_date = datetime.now().strftime('%Y-%m-%d')
            net_value_data = MySQLDB.getFundHistoryNetValues(
                self.code, start_date=period_date, end_date=current_date)

        if not net_value_data:
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

    def onPeriodRadioButtonClicked(self, button):
        if button == self.periodRadioButton1:
            self.loadData(6)
        elif button == self.periodRadioButton2:
            self.loadData(12)
        elif button == self.periodRadioButton3:
            self.loadData(36)
        elif button == self.periodRadioButton4:
            self.loadData(60)
        elif button == self.periodRadioButton5:
            self.loadData(0)
        else:
            print(f'Button not found: {button.text()}')
