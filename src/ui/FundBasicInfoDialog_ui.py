# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FundBasicInfoDialog.ui'
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
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FundBasicInfoDialog(object):
    def setupUi(self, FundBasicInfoDialog):
        if not FundBasicInfoDialog.objectName():
            FundBasicInfoDialog.setObjectName(u"FundBasicInfoDialog")
        FundBasicInfoDialog.resize(683, 563)
        self.verticalLayout = QVBoxLayout(FundBasicInfoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(FundBasicInfoDialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.buttonBox = QDialogButtonBox(FundBasicInfoDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(FundBasicInfoDialog)
        self.buttonBox.accepted.connect(FundBasicInfoDialog.accept)
        self.buttonBox.rejected.connect(FundBasicInfoDialog.reject)

        QMetaObject.connectSlotsByName(FundBasicInfoDialog)
    # setupUi

    def retranslateUi(self, FundBasicInfoDialog):
        FundBasicInfoDialog.setWindowTitle(QCoreApplication.translate("FundBasicInfoDialog", u"\u57fa\u672c\u4fe1\u606f", None))
    # retranslateUi

