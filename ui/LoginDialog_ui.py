# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        if not loginDialog.objectName():
            loginDialog.setObjectName(u"loginDialog")
        loginDialog.setWindowModality(Qt.WindowModality.NonModal)
        loginDialog.resize(480, 290)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginDialog.sizePolicy().hasHeightForWidth())
        loginDialog.setSizePolicy(sizePolicy)
        loginDialog.setMinimumSize(QSize(480, 290))
        loginDialog.setMaximumSize(QSize(480, 290))
        loginDialog.setModal(False)
        self.horizontalLayout_4 = QHBoxLayout(loginDialog)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.logoFrame = QFrame(loginDialog)
        self.logoFrame.setObjectName(u"logoFrame")
        sizePolicy.setHeightForWidth(self.logoFrame.sizePolicy().hasHeightForWidth())
        self.logoFrame.setSizePolicy(sizePolicy)
        self.logoFrame.setMinimumSize(QSize(180, 260))
        self.logoFrame.setBaseSize(QSize(0, 0))
        self.logoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.logoFrame)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, -1, 30, -1)
        self.widget = QWidget(loginDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.accountLabel = QLabel(loginDialog)
        self.accountLabel.setObjectName(u"accountLabel")

        self.horizontalLayout_3.addWidget(self.accountLabel)

        self.accountText = QLineEdit(loginDialog)
        self.accountText.setObjectName(u"accountText")
        self.accountText.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.accountText.setMaxLength(32)
        self.accountText.setFrame(False)
        self.accountText.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout_3.addWidget(self.accountText)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passwordLabel = QLabel(loginDialog)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.horizontalLayout_2.addWidget(self.passwordLabel)

        self.passwordText = QLineEdit(loginDialog)
        self.passwordText.setObjectName(u"passwordText")
        self.passwordText.setMaxLength(32)
        self.passwordText.setFrame(False)
        self.passwordText.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordText.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.passwordText)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.messageLabel = QLabel(loginDialog)
        self.messageLabel.setObjectName(u"messageLabel")
        self.messageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.messageLabel.setMargin(10)

        self.verticalLayout.addWidget(self.messageLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.loginButton = QPushButton(loginDialog)
        self.loginButton.setObjectName(u"loginButton")

        self.horizontalLayout.addWidget(self.loginButton)

        self.cancelButton = QPushButton(loginDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(loginDialog)
        self.loginButton.clicked.connect(loginDialog.onLoginButtonClicked)
        self.cancelButton.clicked.connect(loginDialog.onCancelButtonClicked)

        self.cancelButton.setDefault(False)


        QMetaObject.connectSlotsByName(loginDialog)
    # setupUi

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QCoreApplication.translate("loginDialog", u"\u767b\u5f55", None))
        self.accountLabel.setText(QCoreApplication.translate("loginDialog", u"\u8d26\u53f7:", None))
        self.passwordLabel.setText(QCoreApplication.translate("loginDialog", u"\u5bc6\u7801:", None))
        self.messageLabel.setText("")
        self.loginButton.setText(QCoreApplication.translate("loginDialog", u"\u767b\u5f55", None))
        self.cancelButton.setText(QCoreApplication.translate("loginDialog", u"\u53d6\u6d88", None))
    # retranslateUi

