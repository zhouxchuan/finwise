# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FundNetValueDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_FundNetValueDialog(object):
    def setupUi(self, FundNetValueDialog):
        if not FundNetValueDialog.objectName():
            FundNetValueDialog.setObjectName(u"FundNetValueDialog")
        FundNetValueDialog.resize(840, 658)
        self.verticalLayout = QVBoxLayout(FundNetValueDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleFrame = QFrame(FundNetValueDialog)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.fund_name_label = QLabel(self.titleFrame)
        self.fund_name_label.setObjectName(u"fund_name_label")

        self.horizontalLayout_2.addWidget(self.fund_name_label)

        self.fund_code_label = QLabel(self.titleFrame)
        self.fund_code_label.setObjectName(u"fund_code_label")
        self.fund_code_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.fund_code_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.line_3 = QFrame(self.titleFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.anv_name_label = QLabel(self.titleFrame)
        self.anv_name_label.setObjectName(u"anv_name_label")
        self.anv_name_label.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.anv_name_label)

        self.anv_value_label = QLabel(self.titleFrame)
        self.anv_value_label.setObjectName(u"anv_value_label")

        self.horizontalLayout_2.addWidget(self.anv_value_label)

        self.anv_growthrate_label = QLabel(self.titleFrame)
        self.anv_growthrate_label.setObjectName(u"anv_growthrate_label")
        self.anv_growthrate_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.anv_growthrate_label)

        self.line = QFrame(self.titleFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.cnv_name_label = QLabel(self.titleFrame)
        self.cnv_name_label.setObjectName(u"cnv_name_label")

        self.horizontalLayout_2.addWidget(self.cnv_name_label)

        self.cnv_value_label = QLabel(self.titleFrame)
        self.cnv_value_label.setObjectName(u"cnv_value_label")
        self.cnv_value_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.cnv_value_label)

        self.line_2 = QFrame(self.titleFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.nv_lastest_date_label = QLabel(self.titleFrame)
        self.nv_lastest_date_label.setObjectName(u"nv_lastest_date_label")
        self.nv_lastest_date_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.nv_lastest_date_label)


        self.verticalLayout.addWidget(self.titleFrame)

        self.periodFrame = QFrame(FundNetValueDialog)
        self.periodFrame.setObjectName(u"periodFrame")
        self.periodFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.periodFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.periodFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.periodRadioButton1 = QRadioButton(self.periodFrame)
        self.periodRadioButton1.setObjectName(u"periodRadioButton1")
        self.periodRadioButton1.setChecked(True)

        self.horizontalLayout.addWidget(self.periodRadioButton1)

        self.periodRadioButton2 = QRadioButton(self.periodFrame)
        self.periodRadioButton2.setObjectName(u"periodRadioButton2")

        self.horizontalLayout.addWidget(self.periodRadioButton2)

        self.periodRadioButton3 = QRadioButton(self.periodFrame)
        self.periodRadioButton3.setObjectName(u"periodRadioButton3")

        self.horizontalLayout.addWidget(self.periodRadioButton3)

        self.periodRadioButton4 = QRadioButton(self.periodFrame)
        self.periodRadioButton4.setObjectName(u"periodRadioButton4")

        self.horizontalLayout.addWidget(self.periodRadioButton4)

        self.periodRadioButton5 = QRadioButton(self.periodFrame)
        self.periodRadioButton5.setObjectName(u"periodRadioButton5")

        self.horizontalLayout.addWidget(self.periodRadioButton5)


        self.verticalLayout.addWidget(self.periodFrame)

        self.anvChartWidget = QWidget(FundNetValueDialog)
        self.anvChartWidget.setObjectName(u"anvChartWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anvChartWidget.sizePolicy().hasHeightForWidth())
        self.anvChartWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.anvChartWidget)

        self.cnvChartWidget = QWidget(FundNetValueDialog)
        self.cnvChartWidget.setObjectName(u"cnvChartWidget")
        sizePolicy.setHeightForWidth(self.cnvChartWidget.sizePolicy().hasHeightForWidth())
        self.cnvChartWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.cnvChartWidget)

        self.buttonBox = QDialogButtonBox(FundNetValueDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(FundNetValueDialog)
        self.buttonBox.accepted.connect(FundNetValueDialog.accept)
        self.buttonBox.rejected.connect(FundNetValueDialog.reject)

        QMetaObject.connectSlotsByName(FundNetValueDialog)
    # setupUi

    def retranslateUi(self, FundNetValueDialog):
        FundNetValueDialog.setWindowTitle(QCoreApplication.translate("FundNetValueDialog", u"\u57fa\u91d1\u51c0\u503c", None))
        self.fund_name_label.setText("")
        self.fund_code_label.setText("")
        self.anv_name_label.setText(QCoreApplication.translate("FundNetValueDialog", u"\u5355\u4f4d\u51c0\u503c", None))
        self.anv_value_label.setText(QCoreApplication.translate("FundNetValueDialog", u"0.00", None))
        self.anv_growthrate_label.setText(QCoreApplication.translate("FundNetValueDialog", u"0.00", None))
        self.cnv_name_label.setText(QCoreApplication.translate("FundNetValueDialog", u"\u7d2f\u8ba1\u51c0\u503c", None))
        self.cnv_value_label.setText(QCoreApplication.translate("FundNetValueDialog", u"0.00", None))
        self.nv_lastest_date_label.setText("")
        self.periodRadioButton1.setText(QCoreApplication.translate("FundNetValueDialog", u"\u534a\u5e74", None))
        self.periodRadioButton2.setText(QCoreApplication.translate("FundNetValueDialog", u"\u4e00\u5e74", None))
        self.periodRadioButton3.setText(QCoreApplication.translate("FundNetValueDialog", u"\u4e09\u5e74", None))
        self.periodRadioButton4.setText(QCoreApplication.translate("FundNetValueDialog", u"\u4e94\u5e74", None))
        self.periodRadioButton5.setText(QCoreApplication.translate("FundNetValueDialog", u"\u6210\u7acb\u6765", None))
    # retranslateUi

