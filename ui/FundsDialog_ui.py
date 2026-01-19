# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FundsDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_FundsDialog(object):
    def setupUi(self, FundsDialog):
        if not FundsDialog.objectName():
            FundsDialog.setObjectName(u"FundsDialog")
        FundsDialog.resize(640, 480)
        FundsDialog.setMinimumSize(QSize(640, 480))
        self.verticalLayout_4 = QVBoxLayout(FundsDialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(FundsDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.leftListWidget = QListWidget(FundsDialog)
        self.leftListWidget.setObjectName(u"leftListWidget")
        self.leftListWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.leftListWidget.setAlternatingRowColors(True)
        self.leftListWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.leftListWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.leftListWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.leftListWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.addButton = QPushButton(FundsDialog)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout_3.addWidget(self.addButton)

        self.removeButton = QPushButton(FundsDialog)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout_3.addWidget(self.removeButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(FundsDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.rightListWidget = QListWidget(FundsDialog)
        self.rightListWidget.setObjectName(u"rightListWidget")
        self.rightListWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.rightListWidget.setAlternatingRowColors(True)
        self.rightListWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.rightListWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.rightListWidget.setSortingEnabled(False)

        self.verticalLayout_2.addWidget(self.rightListWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.saveButton = QPushButton(FundsDialog)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.cancelButton = QPushButton(FundsDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.retranslateUi(FundsDialog)
        self.cancelButton.clicked.connect(FundsDialog.reject)
        self.saveButton.clicked.connect(FundsDialog.onSaveButtonClicked)
        self.addButton.clicked.connect(FundsDialog.onAddButtonClicked)
        self.removeButton.clicked.connect(FundsDialog.onRemoveButtonClicked)

        QMetaObject.connectSlotsByName(FundsDialog)
    # setupUi

    def retranslateUi(self, FundsDialog):
        FundsDialog.setWindowTitle(QCoreApplication.translate("FundsDialog", u"\u516c\u52df\u57fa\u91d1\u5217\u8868", None))
        self.label.setText(QCoreApplication.translate("FundsDialog", u"\u6240\u6709\u516c\u5893\u57fa\u91d1:", None))
        self.addButton.setText(QCoreApplication.translate("FundsDialog", u"\u6dfb\u52a0>>", None))
        self.removeButton.setText(QCoreApplication.translate("FundsDialog", u"\u79fb\u9664<<", None))
        self.label_2.setText(QCoreApplication.translate("FundsDialog", u"\u6240\u9009\u516c\u52df\u57fa\u91d1:", None))
        self.saveButton.setText(QCoreApplication.translate("FundsDialog", u"\u4fdd\u5b58", None))
        self.cancelButton.setText(QCoreApplication.translate("FundsDialog", u"\u53d6\u6d88", None))
    # retranslateUi

