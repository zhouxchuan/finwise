# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetupFundAccountDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SetupFundAccountDialog(object):
    def setupUi(self, SetupFundAccountDialog):
        if not SetupFundAccountDialog.objectName():
            SetupFundAccountDialog.setObjectName(u"SetupFundAccountDialog")
        SetupFundAccountDialog.resize(419, 413)
        SetupFundAccountDialog.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(SetupFundAccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(SetupFundAccountDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.listWidget = QListWidget(SetupFundAccountDialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.listWidget.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.listWidget.setSupportedDragActions(Qt.DropAction.MoveAction)

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SetupFundAccountDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.deleteButton = QPushButton(SetupFundAccountDialog)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.saveButton = QPushButton(SetupFundAccountDialog)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.cancelButton = QPushButton(SetupFundAccountDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SetupFundAccountDialog)
        self.saveButton.clicked.connect(SetupFundAccountDialog.onSaveButtonClicked)
        self.cancelButton.clicked.connect(SetupFundAccountDialog.reject)
        self.deleteButton.clicked.connect(SetupFundAccountDialog.onDeleteButtonClicked)

        QMetaObject.connectSlotsByName(SetupFundAccountDialog)
    # setupUi

    def retranslateUi(self, SetupFundAccountDialog):
        SetupFundAccountDialog.setWindowTitle(QCoreApplication.translate("SetupFundAccountDialog", u"\u8bbe\u7f6e\u57fa\u91d1\u8d26\u6237", None))
        self.label_2.setText(QCoreApplication.translate("SetupFundAccountDialog", u"\u57fa\u91d1\u8d26\u6237\u5217\u8868:", None))
        self.label.setText(QCoreApplication.translate("SetupFundAccountDialog", u"*\u53ef\u62d6\u52a8\u9879\u76ee\u8c03\u6574\u663e\u793a\u987a\u5e8f", None))
        self.deleteButton.setText(QCoreApplication.translate("SetupFundAccountDialog", u"\u5220\u9664", None))
        self.saveButton.setText(QCoreApplication.translate("SetupFundAccountDialog", u"\u4fdd\u5b58", None))
        self.cancelButton.setText(QCoreApplication.translate("SetupFundAccountDialog", u"\u53d6\u6d88", None))
    # retranslateUi

