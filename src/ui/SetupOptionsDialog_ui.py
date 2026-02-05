# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetupOptionsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_SetupOptionsDialog(object):
    def setupUi(self, SetupOptionsDialog):
        if not SetupOptionsDialog.objectName():
            SetupOptionsDialog.setObjectName(u"SetupOptionsDialog")
        SetupOptionsDialog.resize(424, 416)
        SetupOptionsDialog.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(SetupOptionsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(SetupOptionsDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.databaseTab = QWidget()
        self.databaseTab.setObjectName(u"databaseTab")
        self.verticalLayout_2 = QVBoxLayout(self.databaseTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(20, 20, 20, -1)
        self.label = QLabel(self.databaseTab)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.hostLineEdit = QLineEdit(self.databaseTab)
        self.hostLineEdit.setObjectName(u"hostLineEdit")

        self.gridLayout.addWidget(self.hostLineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.databaseTab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.portLineEdit = QLineEdit(self.databaseTab)
        self.portLineEdit.setObjectName(u"portLineEdit")

        self.gridLayout.addWidget(self.portLineEdit, 1, 1, 1, 1)

        self.label_5 = QLabel(self.databaseTab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.databaseLineEdit = QLineEdit(self.databaseTab)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setEchoMode(QLineEdit.EchoMode.Normal)

        self.gridLayout.addWidget(self.databaseLineEdit, 2, 1, 1, 1)

        self.label_3 = QLabel(self.databaseTab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.userLineEdit = QLineEdit(self.databaseTab)
        self.userLineEdit.setObjectName(u"userLineEdit")

        self.gridLayout.addWidget(self.userLineEdit, 3, 1, 1, 1)

        self.label_4 = QLabel(self.databaseTab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.passwordLineEdit = QLineEdit(self.databaseTab)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.passwordLineEdit, 4, 1, 1, 1)

        self.testButton = QPushButton(self.databaseTab)
        self.testButton.setObjectName(u"testButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.testButton.sizePolicy().hasHeightForWidth())
        self.testButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.testButton, 5, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.msgLabel = QLabel(self.databaseTab)
        self.msgLabel.setObjectName(u"msgLabel")

        self.verticalLayout_2.addWidget(self.msgLabel)

        self.tabWidget.addTab(self.databaseTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(SetupOptionsDialog)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(SetupOptionsDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SetupOptionsDialog)
        self.cancelButton.clicked.connect(SetupOptionsDialog.reject)
        self.okButton.clicked.connect(SetupOptionsDialog.onOkButtonClicked)
        self.testButton.clicked.connect(SetupOptionsDialog.onTestButtonClicked)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SetupOptionsDialog)
    # setupUi

    def retranslateUi(self, SetupOptionsDialog):
        SetupOptionsDialog.setWindowTitle(QCoreApplication.translate("SetupOptionsDialog", u"\u8bbe\u7f6e\u57fa\u91d1\u8d26\u6237", None))
        self.label.setText(QCoreApplication.translate("SetupOptionsDialog", u"\u6570\u636e\u5e93\u4e3b\u673a:", None))
        self.hostLineEdit.setText(QCoreApplication.translate("SetupOptionsDialog", u"localhost", None))
        self.label_2.setText(QCoreApplication.translate("SetupOptionsDialog", u"\u6570\u636e\u5e93\u7aef\u53e3:", None))
        self.portLineEdit.setText(QCoreApplication.translate("SetupOptionsDialog", u"3306", None))
        self.label_5.setText(QCoreApplication.translate("SetupOptionsDialog", u"\u6570\u636e\u5e93\u540d\u79f0:", None))
        self.databaseLineEdit.setText(QCoreApplication.translate("SetupOptionsDialog", u"finwise", None))
        self.label_3.setText(QCoreApplication.translate("SetupOptionsDialog", u"\u6570\u636e\u5e93\u8d26\u53f7:", None))
        self.userLineEdit.setText(QCoreApplication.translate("SetupOptionsDialog", u"finwise", None))
        self.label_4.setText(QCoreApplication.translate("SetupOptionsDialog", u"\u6570\u636e\u5e93\u5bc6\u7801:", None))
        self.passwordLineEdit.setText(QCoreApplication.translate("SetupOptionsDialog", u"123456", None))
        self.testButton.setText(QCoreApplication.translate("SetupOptionsDialog", u"\u6d4b\u8bd5\u8fde\u63a5", None))
        self.msgLabel.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.databaseTab), QCoreApplication.translate("SetupOptionsDialog", u"\u6570\u636e\u5e93", None))
        self.okButton.setText(QCoreApplication.translate("SetupOptionsDialog", u"\u786e\u5b9a", None))
        self.cancelButton.setText(QCoreApplication.translate("SetupOptionsDialog", u"\u53d6\u6d88", None))
    # retranslateUi

