# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SyncFundHistoryDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SyncFundHistoryDialog(object):
    def setupUi(self, SyncFundHistoryDialog):
        if not SyncFundHistoryDialog.objectName():
            SyncFundHistoryDialog.setObjectName(u"SyncFundHistoryDialog")
        SyncFundHistoryDialog.resize(733, 462)
        SyncFundHistoryDialog.setMinimumSize(QSize(0, 0))
        SyncFundHistoryDialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(SyncFundHistoryDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(SyncFundHistoryDialog)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(200, 0))
        self.listWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.listWidget.setSpacing(1)
        self.listWidget.setModelColumn(0)

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.frame = QFrame(SyncFundHistoryDialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.processTip1 = QLabel(self.frame)
        self.processTip1.setObjectName(u"processTip1")

        self.verticalLayout_2.addWidget(self.processTip1)

        self.progressBar1 = QProgressBar(self.frame)
        self.progressBar1.setObjectName(u"progressBar1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar1.sizePolicy().hasHeightForWidth())
        self.progressBar1.setSizePolicy(sizePolicy2)
        self.progressBar1.setMinimumSize(QSize(0, 0))
        self.progressBar1.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar1.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(9)
        self.progressBar1.setFont(font)
        self.progressBar1.setAutoFillBackground(False)
        self.progressBar1.setStyleSheet(u"")
        self.progressBar1.setValue(0)
        self.progressBar1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar1.setTextVisible(False)
        self.progressBar1.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar1.setInvertedAppearance(False)
        self.progressBar1.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_2.addWidget(self.progressBar1)

        self.processTip3 = QLabel(self.frame)
        self.processTip3.setObjectName(u"processTip3")

        self.verticalLayout_2.addWidget(self.processTip3)

        self.progressBar3 = QProgressBar(self.frame)
        self.progressBar3.setObjectName(u"progressBar3")
        self.progressBar3.setValue(0)
        self.progressBar3.setTextVisible(False)

        self.verticalLayout_2.addWidget(self.progressBar3)

        self.processTip2 = QLabel(self.frame)
        self.processTip2.setObjectName(u"processTip2")

        self.verticalLayout_2.addWidget(self.processTip2)

        self.progressBar2 = QProgressBar(self.frame)
        self.progressBar2.setObjectName(u"progressBar2")
        sizePolicy2.setHeightForWidth(self.progressBar2.sizePolicy().hasHeightForWidth())
        self.progressBar2.setSizePolicy(sizePolicy2)
        self.progressBar2.setMinimumSize(QSize(0, 0))
        self.progressBar2.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar2.setBaseSize(QSize(0, 0))
        self.progressBar2.setFont(font)
        self.progressBar2.setAutoFillBackground(False)
        self.progressBar2.setStyleSheet(u"")
        self.progressBar2.setValue(0)
        self.progressBar2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar2.setTextVisible(False)
        self.progressBar2.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar2.setInvertedAppearance(False)
        self.progressBar2.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_2.addWidget(self.progressBar2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.syncButton = QPushButton(SyncFundHistoryDialog)
        self.syncButton.setObjectName(u"syncButton")
        self.syncButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.syncButton)

        self.cancelButton = QPushButton(SyncFundHistoryDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SyncFundHistoryDialog)
        self.syncButton.clicked.connect(SyncFundHistoryDialog.onSyncButtonClicked)
        self.listWidget.itemSelectionChanged.connect(SyncFundHistoryDialog.onItemSelectionChanged)
        self.cancelButton.clicked.connect(SyncFundHistoryDialog.onCancelButtonClicked)

        QMetaObject.connectSlotsByName(SyncFundHistoryDialog)
    # setupUi

    def retranslateUi(self, SyncFundHistoryDialog):
        SyncFundHistoryDialog.setWindowTitle(QCoreApplication.translate("SyncFundHistoryDialog", u"\u540c\u6b65\u57fa\u91d1\u5386\u53f2\u6570\u636e", None))
        self.processTip1.setText(QCoreApplication.translate("SyncFundHistoryDialog", u"\u540c\u6b65\u57fa\u672c\u6570\u636e...", None))
        self.processTip3.setText(QCoreApplication.translate("SyncFundHistoryDialog", u"\u66f4\u65b0\u5386\u53f2\u6570\u636e...", None))
        self.processTip2.setText(QCoreApplication.translate("SyncFundHistoryDialog", u"\u66f4\u65b0\u6240\u6240\u6709\u5386\u53f2\u6570\u636e...", None))
        self.syncButton.setText(QCoreApplication.translate("SyncFundHistoryDialog", u"\u66f4\u65b0", None))
        self.cancelButton.setText(QCoreApplication.translate("SyncFundHistoryDialog", u"\u53d6\u6d88", None))
    # retranslateUi

