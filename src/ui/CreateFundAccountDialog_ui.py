# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateFundAccountDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_CreateFundAccountDialog(object):
    def setupUi(self, CreateFundAccountDialog):
        if not CreateFundAccountDialog.objectName():
            CreateFundAccountDialog.setObjectName(u"CreateFundAccountDialog")
        CreateFundAccountDialog.resize(451, 509)
        CreateFundAccountDialog.setMinimumSize(QSize(400, 400))
        self.verticalLayout = QVBoxLayout(CreateFundAccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(CreateFundAccountDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(CreateFundAccountDialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.companyLineEdit = QLineEdit(CreateFundAccountDialog)
        self.companyLineEdit.setObjectName(u"companyLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.companyLineEdit.sizePolicy().hasHeightForWidth())
        self.companyLineEdit.setSizePolicy(sizePolicy2)
        self.companyLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.companyLineEdit, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchLineEdit = QLineEdit(CreateFundAccountDialog)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.horizontalLayout.addWidget(self.searchLineEdit)

        self.searchButton = QPushButton(CreateFundAccountDialog)
        self.searchButton.setObjectName(u"searchButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemSearch))
        self.searchButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.searchButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.listWidget = QListWidget(CreateFundAccountDialog)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy3)
        self.listWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.listWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.listWidget)

        self.textEdit = QPlainTextEdit(CreateFundAccountDialog)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy4)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.msgLabel = QLabel(CreateFundAccountDialog)
        self.msgLabel.setObjectName(u"msgLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.msgLabel.sizePolicy().hasHeightForWidth())
        self.msgLabel.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.msgLabel)

        self.okButton = QPushButton(CreateFundAccountDialog)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout_2.addWidget(self.okButton)

        self.cancelButton = QPushButton(CreateFundAccountDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(CreateFundAccountDialog)
        self.searchButton.clicked.connect(CreateFundAccountDialog.onSearchButtonClicked)
        self.okButton.clicked.connect(CreateFundAccountDialog.onCreateButtonClicked)
        self.cancelButton.clicked.connect(CreateFundAccountDialog.reject)

        QMetaObject.connectSlotsByName(CreateFundAccountDialog)
    # setupUi

    def retranslateUi(self, CreateFundAccountDialog):
        CreateFundAccountDialog.setWindowTitle(QCoreApplication.translate("CreateFundAccountDialog", u"\u521b\u5efa\u57fa\u91d1\u8d26\u6237", None))
        self.label_2.setText(QCoreApplication.translate("CreateFundAccountDialog", u"\u516c\u53f8\u4ee3\u7801:", None))
        self.label.setText(QCoreApplication.translate("CreateFundAccountDialog", u"\u57fa\u91d1\u540d\u79f0:", None))
        self.companyLineEdit.setText(QCoreApplication.translate("CreateFundAccountDialog", u"80000229", None))
        self.searchButton.setText("")
        self.msgLabel.setText("")
        self.okButton.setText(QCoreApplication.translate("CreateFundAccountDialog", u"\u521b\u5efa", None))
        self.cancelButton.setText(QCoreApplication.translate("CreateFundAccountDialog", u"\u53d6\u6d88", None))
    # retranslateUi

