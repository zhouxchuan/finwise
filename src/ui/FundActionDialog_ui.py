# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FundActionDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QCheckBox,
    QDateEdit, QDateTimeEdit, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_FundActionDialog(object):
    def setupUi(self, FundActionDialog):
        if not FundActionDialog.objectName():
            FundActionDialog.setObjectName(u"FundActionDialog")
        FundActionDialog.resize(363, 504)
        self.verticalLayout = QVBoxLayout(FundActionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(FundActionDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.dateEdit = QDateEdit(FundActionDialog)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setStyleSheet(u"height:25px;padding: 0px 15px 0px 0px;")
        self.dateEdit.setFrame(False)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.dateEdit.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2026, 1, 1))

        self.horizontalLayout_3.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(FundActionDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.netvalueEdit = QLineEdit(FundActionDialog)
        self.netvalueEdit.setObjectName(u"netvalueEdit")
        self.netvalueEdit.setStyleSheet(u"height:25px;")
        self.netvalueEdit.setFrame(False)

        self.horizontalLayout_2.addWidget(self.netvalueEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(FundActionDialog)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 50))
        self.line.setStyleSheet(u"margin:50px 0px;")
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(FundActionDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buyRadioButton = QRadioButton(FundActionDialog)
        self.buyRadioButton.setObjectName(u"buyRadioButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buyRadioButton.sizePolicy().hasHeightForWidth())
        self.buyRadioButton.setSizePolicy(sizePolicy1)
        self.buyRadioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.buyRadioButton)

        self.sellRadioButton = QRadioButton(FundActionDialog)
        self.sellRadioButton.setObjectName(u"sellRadioButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sellRadioButton.sizePolicy().hasHeightForWidth())
        self.sellRadioButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.sellRadioButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(FundActionDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.costEdit = QLineEdit(FundActionDialog)
        self.costEdit.setObjectName(u"costEdit")
        self.costEdit.setStyleSheet(u"height:25px;")
        self.costEdit.setFrame(False)

        self.horizontalLayout_6.addWidget(self.costEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(FundActionDialog)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(51, 0))

        self.horizontalLayout_4.addWidget(self.label_6)

        self.linkButton = QPushButton(FundActionDialog)
        self.linkButton.setObjectName(u"linkButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistShuffle))
        self.linkButton.setIcon(icon)
        self.linkButton.setCheckable(True)
        self.linkButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.linkButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(FundActionDialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.shareEdit = QLineEdit(FundActionDialog)
        self.shareEdit.setObjectName(u"shareEdit")
        self.shareEdit.setStyleSheet(u"height:25px;")
        self.shareEdit.setFrame(False)

        self.horizontalLayout_7.addWidget(self.shareEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.msgLabel = QLabel(FundActionDialog)
        self.msgLabel.setObjectName(u"msgLabel")

        self.verticalLayout.addWidget(self.msgLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.saveCheckBox = QCheckBox(FundActionDialog)
        self.saveCheckBox.setObjectName(u"saveCheckBox")

        self.verticalLayout.addWidget(self.saveCheckBox)

        self.line_2 = QFrame(FundActionDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.buttonBox = QDialogButtonBox(FundActionDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(FundActionDialog)
        self.buttonBox.accepted.connect(FundActionDialog.accept)
        self.buttonBox.rejected.connect(FundActionDialog.reject)
        self.dateEdit.dateChanged.connect(FundActionDialog.onDateChanged)
        self.costEdit.editingFinished.connect(FundActionDialog.onCostEditingFinished)
        self.shareEdit.editingFinished.connect(FundActionDialog.onShareEditingFinished)

        QMetaObject.connectSlotsByName(FundActionDialog)
    # setupUi

    def retranslateUi(self, FundActionDialog):
        FundActionDialog.setWindowTitle(QCoreApplication.translate("FundActionDialog", u"\u57fa\u91d1\u64cd\u4f5c", None))
        self.label.setText(QCoreApplication.translate("FundActionDialog", u"\u64cd\u4f5c\u65e5\u671f:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("FundActionDialog", u"yyyy-MM-dd", None))
        self.label_2.setText(QCoreApplication.translate("FundActionDialog", u"\u5355\u4f4d\u51c0\u503c:", None))
        self.label_3.setText(QCoreApplication.translate("FundActionDialog", u"\u4e70\u5356\u64cd\u4f5c:", None))
        self.buyRadioButton.setText(QCoreApplication.translate("FundActionDialog", u"\u4e70\u5165", None))
        self.sellRadioButton.setText(QCoreApplication.translate("FundActionDialog", u"\u5356\u51fa", None))
        self.label_4.setText(QCoreApplication.translate("FundActionDialog", u"\u4e70\u5356\u91d1\u989d:", None))
        self.label_6.setText("")
        self.linkButton.setText("")
        self.label_5.setText(QCoreApplication.translate("FundActionDialog", u"\u4e70\u5356\u4efd\u989d:", None))
        self.msgLabel.setText("")
        self.saveCheckBox.setText(QCoreApplication.translate("FundActionDialog", u"\u4ec5\u4fdd\u5b58\u6570\u636e\uff0c\u4e0d\u6267\u884c\u540c\u6b65\u64cd\u4f5c", None))
    # retranslateUi

