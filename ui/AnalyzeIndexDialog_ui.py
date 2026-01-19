# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnalyzeIndexDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AnalyzeIndexDialog(object):
    def setupUi(self, AnalyzeIndexDialog):
        if not AnalyzeIndexDialog.objectName():
            AnalyzeIndexDialog.setObjectName(u"AnalyzeIndexDialog")
        AnalyzeIndexDialog.resize(1181, 845)
        self.verticalLayout = QVBoxLayout(AnalyzeIndexDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(AnalyzeIndexDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.symbolComboBox = QComboBox(self.frame)
        self.symbolComboBox.setObjectName(u"symbolComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symbolComboBox.sizePolicy().hasHeightForWidth())
        self.symbolComboBox.setSizePolicy(sizePolicy)
        self.symbolComboBox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.symbolComboBox)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.startDateEdit = QDateEdit(self.frame)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setMaximumDateTime(QDateTime(QDate(2050, 12, 31), QTime(23, 59, 59)))
        self.startDateEdit.setMinimumDateTime(QDateTime(QDate(1999, 12, 31), QTime(0, 0, 0)))
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDate(QDate(2026, 1, 9))

        self.horizontalLayout.addWidget(self.startDateEdit)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.endDateEdit = QDateEdit(self.frame)
        self.endDateEdit.setObjectName(u"endDateEdit")
        self.endDateEdit.setMaximumDateTime(QDateTime(QDate(2050, 12, 31), QTime(23, 59, 59)))
        self.endDateEdit.setMinimumDateTime(QDateTime(QDate(1999, 12, 30), QTime(0, 0, 0)))
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(QDate(2026, 1, 9))

        self.horizontalLayout.addWidget(self.endDateEdit)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.showPushButton = QPushButton(self.frame)
        self.showPushButton.setObjectName(u"showPushButton")

        self.horizontalLayout.addWidget(self.showPushButton)

        self.cancelButton = QPushButton(self.frame)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.frame)

        self.dataWidget = QWidget(AnalyzeIndexDialog)
        self.dataWidget.setObjectName(u"dataWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dataWidget.sizePolicy().hasHeightForWidth())
        self.dataWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.dataWidget)


        self.retranslateUi(AnalyzeIndexDialog)
        self.cancelButton.clicked.connect(AnalyzeIndexDialog.reject)
        self.showPushButton.clicked.connect(AnalyzeIndexDialog.onShowPushButtonClicked)

        self.symbolComboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(AnalyzeIndexDialog)
    # setupUi

    def retranslateUi(self, AnalyzeIndexDialog):
        AnalyzeIndexDialog.setWindowTitle(QCoreApplication.translate("AnalyzeIndexDialog", u"\u6307\u6570\u5206\u6790", None))
        self.label.setText(QCoreApplication.translate("AnalyzeIndexDialog", u"\u6307\u6807\uff1a", None))
        self.symbolComboBox.setCurrentText("")
        self.label_2.setText(QCoreApplication.translate("AnalyzeIndexDialog", u"\u5f00\u59cb\u65e5\u671f\uff1a", None))
        self.startDateEdit.setDisplayFormat(QCoreApplication.translate("AnalyzeIndexDialog", u"yyyy-MM-dd", None))
        self.label_3.setText(QCoreApplication.translate("AnalyzeIndexDialog", u"\u7ed3\u675f\u65e5\u671f\uff1a", None))
        self.endDateEdit.setDisplayFormat(QCoreApplication.translate("AnalyzeIndexDialog", u"yyyy-MM-dd", None))
        self.showPushButton.setText(QCoreApplication.translate("AnalyzeIndexDialog", u"\u663e\u793a", None))
        self.cancelButton.setText(QCoreApplication.translate("AnalyzeIndexDialog", u"\u53d6\u6d88", None))
    # retranslateUi

