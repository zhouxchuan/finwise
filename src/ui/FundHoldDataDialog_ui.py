# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FundHoldDataDialog.ui'
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
    QFormLayout, QFrame, QHBoxLayout, QLayout,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FundHoldDataDialog(object):
    def setupUi(self, FundHoldDataDialog):
        if not FundHoldDataDialog.objectName():
            FundHoldDataDialog.setObjectName(u"FundHoldDataDialog")
        FundHoldDataDialog.resize(874, 624)
        self.verticalLayout_2 = QVBoxLayout(FundHoldDataDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(FundHoldDataDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 844, 800))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 800))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.holdRatioWidget = QWidget(self.scrollAreaWidgetContents)
        self.holdRatioWidget.setObjectName(u"holdRatioWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.holdRatioWidget.sizePolicy().hasHeightForWidth())
        self.holdRatioWidget.setSizePolicy(sizePolicy1)
        self.holdRatioWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.holdRatioWidget)

        self.holdShareWidget = QWidget(self.scrollAreaWidgetContents)
        self.holdShareWidget.setObjectName(u"holdShareWidget")
        sizePolicy1.setHeightForWidth(self.holdShareWidget.sizePolicy().hasHeightForWidth())
        self.holdShareWidget.setSizePolicy(sizePolicy1)
        self.holdShareWidget.setMinimumSize(QSize(0, 0))
        self.holdShareWidget.setMaximumSize(QSize(16777215, 16777215))
        self.holdShareWidget.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.holdShareWidget)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.holdBondWidget = QWidget(self.scrollAreaWidgetContents)
        self.holdBondWidget.setObjectName(u"holdBondWidget")
        sizePolicy1.setHeightForWidth(self.holdBondWidget.sizePolicy().hasHeightForWidth())
        self.holdBondWidget.setSizePolicy(sizePolicy1)
        self.holdBondWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.holdBondWidget)

        self.holdIndustryWidget = QWidget(self.scrollAreaWidgetContents)
        self.holdIndustryWidget.setObjectName(u"holdIndustryWidget")
        sizePolicy1.setHeightForWidth(self.holdIndustryWidget.sizePolicy().hasHeightForWidth())
        self.holdIndustryWidget.setSizePolicy(sizePolicy1)
        self.holdIndustryWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.holdIndustryWidget)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(FundHoldDataDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(FundHoldDataDialog)
        self.buttonBox.accepted.connect(FundHoldDataDialog.accept)
        self.buttonBox.rejected.connect(FundHoldDataDialog.reject)

        QMetaObject.connectSlotsByName(FundHoldDataDialog)
    # setupUi

    def retranslateUi(self, FundHoldDataDialog):
        FundHoldDataDialog.setWindowTitle(QCoreApplication.translate("FundHoldDataDialog", u"\u57fa\u91d1\u6301\u4ed3", None))
    # retranslateUi

