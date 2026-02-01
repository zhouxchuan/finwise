from PySide6.QtCharts import QChartView
from PySide6.QtGui import QColor, QPen, Qt, QFont,QBrush
from PySide6.QtWidgets import QGraphicsLineItem,QGraphicsTextItem,QGraphicsEllipseItem
from PySide6.QtCore import QPointF
from PySide6.QtCore import QDateTime

# -----------------------------------------------------------------------------
# 自定义K线图表视图
class KChartView(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.x_line = QGraphicsLineItem()
        self.x_line.setPen(QPen(QColor(100, 100, 100), 1,Qt.DashLine))
        self.x_line.setZValue(2)
        self.x_line.setVisible(False)  # 初始隐藏

        self.y_line = QGraphicsLineItem()
        self.y_line.setPen(QPen(QColor(100, 100, 100), 1,Qt.DashLine))
        self.y_line.setZValue(2)
        self.y_line.setVisible(False)  # 初始隐藏

        self.xy_point = QGraphicsEllipseItem()
        self.xy_point.setZValue(3)
        self.xy_point.setVisible(False)
        self.xy_point.setBrush(QBrush(QColor(255, 255, 0)))
        self.xy_point.setRect(-3, -3, 6, 6)
        # self.xy_point.setPen(QPen(QColor(255, 255, 255), 1, Qt.SolidLine))

        # 创建Y轴值标签
        self.value_label = QGraphicsTextItem()
        self.value_label.setZValue(4)
        self.value_label.setVisible(False)
        self.value_label.setDefaultTextColor(QColor(255, 255, 255))
        self.value_label.setFont(QFont("Arial", 8))
        self.value_label.setFlag(QGraphicsTextItem.ItemIgnoresTransformations)

        self.scene().addItem(self.x_line)
        self.scene().addItem(self.y_line)
        self.scene().addItem(self.xy_point)
        self.scene().addItem(self.value_label)

    def enterEvent(self, event):
        self.x_line.setVisible(True)
        self.y_line.setVisible(True)
        self.xy_point.setVisible(True)
        self.value_label.setVisible(True)
        return super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.x_line.setVisible(False)
        self.y_line.setVisible(False)
        self.xy_point.setVisible(False)
        self.value_label.setVisible(False)
        return super().leaveEvent(event)
    
    def mouseMoveEvent(self, event):
        """鼠标移动事件，更新交叉线位置"""
        # 调用父类方法
        super().mouseMoveEvent(event)
        
        # 获取鼠标位置
        pos = event.position()
        x = pos.x()
        y = pos.y()
        
        # # 获取视图区域大小
        # view_rect = self.rect()
        # scene_rect = self.scene().sceneRect()
        
        # # 更新水平线 (x轴交叉线)
        # self.x_line.setLine(0, y, view_rect.width(), y)
        
        # # 更新垂直线 (y轴交叉线)
        # self.y_line.setLine(x, 0, x, view_rect.height())    

        # 获取chart的绘图区域（排除坐标轴、标题等区域）
        chart_rect = self.chart().plotArea()
        
        # 将鼠标坐标转换为chart坐标系的坐标
        chart_pos = self.chart().mapToValue(pos)

        # 获取chart坐标系的边界
        axes = self.chart().axes()
        if axes:
            # 获取X轴和Y轴的范围
            x_axis = None
            y_axis = None
            for axis in axes:
                if axis.orientation() == Qt.Horizontal:
                    x_axis = axis
                elif axis.orientation() == Qt.Vertical:
                    y_axis = axis
            
            if x_axis and y_axis:
                # 计算线条在绘图区域内的坐标
                x_min = chart_rect.left()
                x_max = chart_rect.right()
                y_min = chart_rect.top()
                y_max = chart_rect.bottom()

                # 限制鼠标坐标在绘图区域内
                x_clamped = max(x_min, min(x, x_max))
                y_clamped = max(y_min, min(y, y_max))
                
                # 获取鼠标位置处第一个series的Y值
                series_y_value = None
                if self.chart().series():
                    series = self.chart().series()[0]
                    
                    # 方法1: 使用最近的数据点
                    closest_point = None
                    min_distance = float('inf')
                    
                    # 遍历series中的所有点，找到距离鼠标X坐标最近的点
                    for i in range(series.count()):
                        point = series.at(i)
                        distance = abs(point.x() - chart_pos.x())
                        if distance < min_distance:
                            min_distance = distance
                            closest_point = point
                    
                    if closest_point:
                        series_y_value = closest_point.y()
               
                # 使用series的Y值（如果获取到），否则使用chart坐标系的Y值
                if series_y_value is not None:
                    chart_y_value = series_y_value
                else:
                    chart_y_value = chart_pos.y()
            
                # 将chart坐标系的Y值转换为视图坐标
                chart_point = QPointF(0, chart_y_value)
                view_point = self.chart().mapToPosition(chart_point)
                
                # 使用转换后的Y坐标
                y_mapped = view_point.y()
                
                # 确保y_mapped在绘图区域内
                y_mapped_clamped = max(y_min, min(y_mapped, y_max))

                 # 更新水平线 (x轴交叉线) - 使用chart坐标系的Y值对应的视图坐标
                self.x_line.setLine(x_min, y_mapped_clamped, x_max, y_mapped_clamped)
                
                # 更新垂直线 (y轴交叉线) - 只在绘图区域内绘制
                self.y_line.setLine(x_clamped, y_min, x_clamped, y_max)

                self.xy_point.setPos(x_clamped, y_mapped_clamped)

                # 更新Y轴值标签
                if hasattr(y_axis, 'labelFormat') or hasattr(x_axis, 'labelFormat'):
                    y_value = chart_pos.y()

                    x_value = chart_pos.x()
                    if x_value > 1000000000000:  # 大于2001年的毫秒时间戳
                        datetime_obj = QDateTime.fromMSecsSinceEpoch(int(x_value))
                    elif x_value > 1000000000:  # 大于2001年的秒时间戳
                        datetime_obj = QDateTime.fromSecsSinceEpoch(int(x_value))
                    else:
                        # 如果不是时间戳，显示原始数值
                        datetime_obj = None

                    if datetime_obj and datetime_obj.isValid():
                        label_text = f"{y_value:.2f}\n{datetime_obj.toString('yyyy-MM-dd')}"
                    else:
                        label_text = f"{y_value:.2f}\n{x_value}"

                    self.value_label.setPlainText(label_text)
                    # 将标签放置在Y轴右侧，与交叉线对齐
                    # self.value_label.setPos(x_max + 5, y_mapped_clamped - 10)

                    self.value_label.setPos(x_clamped + 5, y_mapped_clamped - 10)
