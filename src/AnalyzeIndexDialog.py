from PySide6.QtWidgets import QDialog
from ui.AnalyzeIndexDialog_ui import Ui_AnalyzeIndexDialog
from PySide6.QtCore import QDate,QThread,Signal,QDateTime,Qt
from utils.datasource import fundDataSource
from PySide6.QtCharts import QChart, QChartView, QSplineSeries, QDateTimeAxis, QValueAxis
from PySide6.QtGui import QPainter, QBrush, QColor, QPen
from PySide6.QtWidgets import QVBoxLayout, QSizePolicy
from datetime import datetime

# 分析指数对话框
class AnalyzeIndexDialog(QDialog, Ui_AnalyzeIndexDialog):
    def __init__(self, parent=None):
        super(AnalyzeIndexDialog, self).__init__(parent)
        self.setupUi(self)

        self.symbolComboBox.addItems(['市场表征', '一级行业', '风格指数'])
        self.symbolComboBox.setCurrentIndex(0)
        self.startDateEdit.setDate(QDate.currentDate())
        self.endDateEdit.setDate(QDate.currentDate())

        self.analyze_data = None
        self.analyzeIndexThread = None

        # 创建图表
        self.index_chart = QChart()
        self.index_chart.setTitle("指数分析图")
        self.index_chart.setAnimationOptions(QChart.SeriesAnimations)
        self.index_chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.index_chart.setBackgroundVisible(True)
       
        # 创建图表视图
        self.index_chartview = QChartView(self.index_chart)
        self.index_chartview.setRenderHint(QPainter.Antialiasing)
        
        # 设置图表视图背景为透明
        self.index_chartview.setStyleSheet("background: transparent;")
        self.index_chartview.setBackgroundBrush(QBrush(QColor(0, 0, 0, 0)))

        # 设置图表视图的尺寸策略，使其能够扩展填充可用空间
        self.index_chartview.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.index_chartview.setMinimumSize(400, 300)  # 设置最小尺寸

        # 设置布局
        data_layout = self.dataWidget.layout()
        if data_layout is None:
            data_layout = QVBoxLayout(self.dataWidget)
        data_layout.setContentsMargins(0, 0, 0, 0)  # 移除边距
        data_layout.setSpacing(0)  # 移除间距
        data_layout.addWidget(self.index_chartview)

    def onShowPushButtonClicked(self):
        if self.analyzeIndexThread:
            if self.analyzeIndexThread.isRunning():
                self.analyzeIndexThread.quit()
                self.analyzeIndexThread.wait(1000)
                if self.analyzeIndexThread.isRunning():
                    self.analyzeIndexThread.terminate()
                    self.analyzeIndexThread.wait()

        self.analyzeIndexThread = AnalyzeIndexThread(self.symbolComboBox.currentText(),self.startDateEdit.date().toString("yyyyMMdd"),self.endDateEdit.date().toString("yyyyMMdd"))
        self.analyzeIndexThread.signalAnalyzeIndexData.connect(self.onAnalyzeIndexData)
        self.analyzeIndexThread.start()
    
    def closeEvent(self, event):
        # 窗口关闭时确保线程已停止
        if self.analyzeIndexThread:
            if self.analyzeIndexThread.isRunning():
                self.analyzeIndexThread.quit()
                self.analyzeIndexThread.wait(1000)
                if self.analyzeIndexThread.isRunning():
                    self.analyzeIndexThread.terminate()
                    self.analyzeIndexThread.wait()
            self.analyzeIndexThread = None
            
        event.accept()
    
    def onAnalyzeIndexData(self, data):
        if isinstance(data, Exception):
            return

        self.analyze_data = data

        # 检查数据是否为空
        if self.analyze_data is None or self.analyze_data.empty:
            print("分析指数数据为空")
            return
        
        # 清空图表
        self.index_chart.removeAllSeries()
       # 清除之前的坐标轴
        axes = self.index_chart.axes()
        for axis in axes:
            self.index_chart.removeAxis(axis)

        pen = QPen()
        pen.setColor(QColor(55, 55, 55))
        pen.setWidth(1)
        pen.setStyle(Qt.DashLine)

        # 设置X轴（时间轴）
        axis_x = QDateTimeAxis()
        axis_x.setFormat("yyyy-MM-dd")
        axis_x.setTitleText("日期")
        axis_x.setGridLinePen(pen)
        axis_x.setTickCount(10)

        # 设置Y轴（净值轴）
        axis_y = QValueAxis()
        axis_y.setTitleText("指数值")
        axis_y.setLabelFormat("%.2f")
        axis_y.setGridLinePen(pen)
        axis_y.setTickCount(10)
        
        # 先添加坐标轴到图表
        self.index_chart.addAxis(axis_x, Qt.AlignBottom)
        self.index_chart.addAxis(axis_y, Qt.AlignLeft)

        # 创建折线图系列
        series_dict = {}
        for index, row in self.analyze_data.iterrows():
            # item_code = row['指数代码']
            row_name = row['指数名称']
            row_date = row['发布日期']
            row_value = row['收盘指数']
            # item_amount = row['成交量']
            # item_change = row['涨跌幅']
            # item_pe = row['市盈率']
            # item_pb = row['市净率']
            # item_payout = row['股息率']
                   
            # 转换为QDateTime
            # date_str = date_obj.strftime('%Y-%m-%d')
            # q_datetime = QDateTime.fromString(date_str, "yyyy-MM-dd")
            q_datetime = QDateTime.fromString(str(row_date), "yyyy-MM-dd")
            
            # 获取或创建系列
            if row_name not in series_dict:
                series = QSplineSeries()
                series.setName(row_name)
                series_dict[row_name] = series
            else:
                series = series_dict[row_name]
            
            # 添加数据点
            series.append(q_datetime.toMSecsSinceEpoch(), float(row_value))

        # 添加所有系列到图表并关联坐标轴
        for series in series_dict.values():
            self.index_chart.addSeries(series)
            series.attachAxis(axis_x)
            series.attachAxis(axis_y)


        # 设置坐标轴范围（如果有数据）
        if series_dict:
            # 获取所有数据点的时间范围
            all_dates = []
            all_values = []
            for series in series_dict.values():
                for point in series.points():
                    all_dates.append(point.x())
                    all_values.append(point.y())
            
            if all_dates:
                min_date = min(all_dates)
                max_date = max(all_dates)
                min_value = min(all_values)
                max_value = max(all_values)
                
                # 设置X轴范围
                axis_x.setRange(QDateTime.fromMSecsSinceEpoch(int(min_date)), 
                               QDateTime.fromMSecsSinceEpoch(int(max_date)))
                
                # 设置Y轴范围，留一些边距
                value_range = max_value - min_value
                margin = value_range * 0.1 if value_range > 0 else 1
                axis_y.setRange(min_value - margin, max_value + margin)
        
        # 创建图例
        self.index_chart.legend().setAlignment(Qt.AlignRight)
        self.index_chart.legend().setVisible(True)

        # 刷新图表
        self.index_chartview.update()
        print(f"图表已更新，包含 {len(series_dict)} 个指数系列")


class AnalyzeIndexThread(QThread):

    signalAnalyzeIndexData = Signal(object)

    def __init__(self, symbol,start_date,end_date):
        super(AnalyzeIndexThread, self).__init__()
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        try:
            data = fundDataSource.getAnalyzeIndexData(self.symbol,self.start_date,self.end_date)
            self.signalAnalyzeIndexData.emit(data)
        except Exception as e:
            self.signalAnalyzeIndexData.emit(e)