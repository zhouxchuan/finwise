# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TradeFundDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QDialog,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_TradeFundDialog(object):
    def setupUi(self, TradeFundDialog):
        if not TradeFundDialog.objectName():
            TradeFundDialog.setObjectName(u"TradeFundDialog")
        TradeFundDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        TradeFundDialog.resize(1080, 768)
        self.verticalLayout = QVBoxLayout(TradeFundDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(TradeFundDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.startDateEdit = QDateEdit(TradeFundDialog)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDate(QDate(2026, 1, 1))

        self.horizontalLayout.addWidget(self.startDateEdit)

        self.label_2 = QLabel(TradeFundDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.endDateEdit = QDateEdit(TradeFundDialog)
        self.endDateEdit.setObjectName(u"endDateEdit")
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(QDate(2026, 1, 1))

        self.horizontalLayout.addWidget(self.endDateEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.showButton = QPushButton(TradeFundDialog)
        self.showButton.setObjectName(u"showButton")

        self.horizontalLayout.addWidget(self.showButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(TradeFundDialog)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.saveButton = QPushButton(TradeFundDialog)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.cancelButton = QPushButton(TradeFundDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(TradeFundDialog)
        self.showButton.clicked.connect(TradeFundDialog.onShowButtonClicked)
        self.saveButton.clicked.connect(TradeFundDialog.onSaveButtonClicked)
        self.cancelButton.clicked.connect(TradeFundDialog.reject)
        self.tableWidget.cellChanged.connect(TradeFundDialog.onTableCellChanged)

        QMetaObject.connectSlotsByName(TradeFundDialog)
    # setupUi

    def retranslateUi(self, TradeFundDialog):
        TradeFundDialog.setWindowTitle(QCoreApplication.translate("TradeFundDialog", u"\u57fa\u91d1\u4ea4\u6613", None))
        self.label.setText(QCoreApplication.translate("TradeFundDialog", u"\u4ece", None))
        self.label_2.setText(QCoreApplication.translate("TradeFundDialog", u"\u5230", None))
        self.showButton.setText(QCoreApplication.translate("TradeFundDialog", u"\u663e\u793a", None))
        self.saveButton.setText(QCoreApplication.translate("TradeFundDialog", u"\u4fdd\u5b58", None))
        self.cancelButton.setText(QCoreApplication.translate("TradeFundDialog", u"\u53d6\u6d88", None))
    # retranslateUi

