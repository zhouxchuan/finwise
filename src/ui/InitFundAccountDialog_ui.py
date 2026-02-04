# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InitFundAccountDialog.ui'
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
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_InitFundAccountDialog(object):
    def setupUi(self, InitFundAccountDialog):
        if not InitFundAccountDialog.objectName():
            InitFundAccountDialog.setObjectName(u"InitFundAccountDialog")
        InitFundAccountDialog.resize(368, 360)
        self.verticalLayout = QVBoxLayout(InitFundAccountDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(InitFundAccountDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.fundLabel = QLabel(self.frame)
        self.fundLabel.setObjectName(u"fundLabel")

        self.verticalLayout_2.addWidget(self.fundLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.costEdit = QLineEdit(self.frame)
        self.costEdit.setObjectName(u"costEdit")

        self.horizontalLayout.addWidget(self.costEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.shareEdit = QLineEdit(self.frame)
        self.shareEdit.setObjectName(u"shareEdit")

        self.horizontalLayout_2.addWidget(self.shareEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.msgLabel = QLabel(self.frame)
        self.msgLabel.setObjectName(u"msgLabel")

        self.verticalLayout_2.addWidget(self.msgLabel)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(InitFundAccountDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(InitFundAccountDialog)
        self.buttonBox.accepted.connect(InitFundAccountDialog.accept)
        self.buttonBox.rejected.connect(InitFundAccountDialog.reject)

        QMetaObject.connectSlotsByName(InitFundAccountDialog)
    # setupUi

    def retranslateUi(self, InitFundAccountDialog):
        InitFundAccountDialog.setWindowTitle(QCoreApplication.translate("InitFundAccountDialog", u"\u521d\u59cb\u5316\u8d26\u6237\u6570\u636e", None))
        self.fundLabel.setText("")
        self.label.setText(QCoreApplication.translate("InitFundAccountDialog", u"\u521d\u59cb\u91d1\u989d:", None))
        self.label_2.setText(QCoreApplication.translate("InitFundAccountDialog", u"\u521d\u59cb\u4efd\u989d:", None))
        self.msgLabel.setText("")
    # retranslateUi

