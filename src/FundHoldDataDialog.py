from PySide6.QtWidgets import QDialog, QSizePolicy, QVBoxLayout, QButtonGroup
from PySide6.QtCore import Qt, QDateTime, Signal, QThread
from PySide6.QtGui import QPainter, QColor, QBrush, QFont
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from ui.FundHoldDataDialog_ui import Ui_FundHoldDataDialog
from utils.datasource import fundDataSource
from classes.KChartView import KChartView
from datetime import datetime
from dateutil.relativedelta import relativedelta


class FundHoldDataDialog(QDialog, Ui_FundHoldDataDialog):
    def __init__(self, parent=None, params={'code': None, 'name': None}):
        super(FundHoldDataDialog, self).__init__(parent)
        self.setupUi(self)
        self.code = params['code']
        self.name = params['name']

        self.fundHoldThread = FundHoldDataThread()
        self.fundHoldThread.fundHoldDataEvent.connect(self.onFundHoldDataEvent)

        # 初始化图表
        self.initChart()

    def initChart(self):
        '''
        初始化图表
        '''
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

    def loadData(self):
        '''
        加载基金持仓数据
        '''
        # 确保之前的线程已正确停止
        self.fundHoldThread.stop()
        self.fundHoldThread.setParams(self.code)
        self.fundHoldThread.start()

    def onFundHoldDataEvent(self, hold_ratio, hold_share, hold_bond, hold_industry):
        '''
        基金持仓数据事件处理
        param: code: 基金代码
        param: hold_ratio: 持仓比例
        param: hold_share: 持仓股票
        param: hold_bond: 持仓债券
        param: hold_industry: 持仓行业
        '''
        self.updateHoldRatioChart(hold_ratio)
        self.updateHoldShareChart(hold_share)
        self.updateHoldBondChart(hold_bond)
        self.updateHoldIndustryChart(hold_industry)

    def updateHoldRatioChart(self, hold_ratio):
        '''
        更新持仓比例图表
        param: hold_ratio: 持仓比例
        '''
        self.holdRatioChart.removeAllSeries()
        series = QPieSeries()
        series.setName("持仓比例")
        for index, row in hold_ratio.iterrows():
            asset_type = row['资产类型']
            ratio = row['仓位占比']

            # 创建饼图切片并添加
            slice = series.append(asset_type, ratio)

            # 设置切片标签显示比例值
            slice.setLabel(f"{asset_type}: {ratio}%")
            slice.setLabelVisible(False)
            slice.setBorderWidth(0)
            slice.setBorderColor(QColor(0, 0, 0, 0))
        self.holdRatioChart.addSeries(series)

    def updateHoldShareChart(self, hold_share):
        '''
        更新持仓股票图表
        param: hold_share: 持仓股票
        '''
        self.holdShareChart.removeAllSeries()
        series = QPieSeries()
        series.setName("持仓股票")
        for index, row in hold_share.iterrows():
            if index > 9:
                break
            stock_name = row['股票名称']
            stock_ratio = row['占净值比例']

            # 创建饼图切片并添加
            slice = series.append(stock_name, stock_ratio)

            # 设置切片标签显示比例值
            slice.setLabel(f"{stock_name}: {stock_ratio}%")
            slice.setLabelVisible(False)
            slice.setBorderWidth(0)
            slice.setBorderColor(QColor(0, 0, 0, 0))
        self.holdShareChart.addSeries(series)

    def updateHoldBondChart(self, hold_bond):
        '''
        更新持仓债券图表
        param: hold_bond: 持仓债券
        '''
        self.holdBondChart.removeAllSeries()
        series = QPieSeries()
        series.setName("持仓债券")

        for index, row in hold_bond.iterrows():
            bond_name = row['债券名称']
            bond_ratio = row['占净值比例']

            # 创建饼图切片并添加
            slice = series.append(bond_name, bond_ratio)

            # 设置切片标签显示比例值
            slice.setLabel(f"{bond_name}: {bond_ratio}%")
            slice.setLabelVisible(False)
            slice.setBorderWidth(0)
            slice.setBorderColor(QColor(0, 0, 0, 0))
        self.holdBondChart.addSeries(series)

    def updateHoldIndustryChart(self, hold_industry):
        '''
        更新持仓行业图表
        param: hold_industry: 持仓行业
        '''
        self.holdIndustryChart.removeAllSeries()
        series = QPieSeries()
        series.setName("持仓行业")
        for index, row in hold_industry.iterrows():
            industry_name = row['行业类别']
            industry_ratio = row['占净值比例']

            # 创建饼图切片并添加
            slice = series.append(industry_name, industry_ratio)

            # 设置切片标签显示比例值
            slice.setLabel(f"{industry_name}: {industry_ratio}%")
            slice.setLabelVisible(False)
            slice.setBorderWidth(0)
            slice.setBorderColor(QColor(0, 0, 0, 0))
        self.holdIndustryChart.addSeries(series)


class FundHoldDataThread(QThread):
    '''
    获取基金持仓数据线程
    '''
    fundHoldDataEvent = Signal(object, object, object, object)

    def __init__(self):
        super().__init__()
        self.code = None

    def setParams(self, code):
        self.code = code

    def stop(self):
        if self.isRunning():
            self.quit()
            self.wait(1000)
            if self.isRunning():
                self.terminate()
                self.wait()

    def run(self):
        try:
            hold_ratio = fundDataSource.getFundHoldRatio(self.code)
            hold_share = fundDataSource.getFundHoldShare(self.code)
            hold_bond = fundDataSource.getFundHoldBond(self.code)
            hold_industry = fundDataSource.getFundHoldIndustry(self.code)
            self.fundHoldDataEvent.emit(hold_ratio, hold_share, hold_bond, hold_industry)
        except Exception as e:
            print(f'获取基金持仓数据失败：{e}')
