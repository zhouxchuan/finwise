# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TradeFundDialog.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDateTimeEdit,
    QDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_TradeFundDialog(object):
    def setupUi(self, TradeFundDialog):
        if not TradeFundDialog.objectName():
            TradeFundDialog.setObjectName(u"TradeFundDialog")
        TradeFundDialog.resize(480, 498)
        self.verticalLayout_2 = QVBoxLayout(TradeFundDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(TradeFundDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dateLabel = QLabel(self.frame)
        self.dateLabel.setObjectName(u"dateLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateLabel.sizePolicy().hasHeightForWidth())
        self.dateLabel.setSizePolicy(sizePolicy)
        self.dateLabel.setMinimumSize(QSize(51, 0))

        self.horizontalLayout_3.addWidget(self.dateLabel)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy1)
        self.dateEdit.setStyleSheet(u"height:25px;padding: 0px 15px 0px 0px;")
        self.dateEdit.setFrame(True)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.dateEdit.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2026, 1, 1))

        self.horizontalLayout_3.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.amountLabel = QLabel(self.frame)
        self.amountLabel.setObjectName(u"amountLabel")
        sizePolicy.setHeightForWidth(self.amountLabel.sizePolicy().hasHeightForWidth())
        self.amountLabel.setSizePolicy(sizePolicy)
        self.amountLabel.setMinimumSize(QSize(51, 0))

        self.horizontalLayout_6.addWidget(self.amountLabel)

        self.amountEdit = QLineEdit(self.frame)
        self.amountEdit.setObjectName(u"amountEdit")
        sizePolicy1.setHeightForWidth(self.amountEdit.sizePolicy().hasHeightForWidth())
        self.amountEdit.setSizePolicy(sizePolicy1)
        self.amountEdit.setStyleSheet(u"height:25px;")
        self.amountEdit.setFrame(True)

        self.horizontalLayout_6.addWidget(self.amountEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.estimateButton = QPushButton(self.frame)
        self.estimateButton.setObjectName(u"estimateButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.estimateButton.sizePolicy().hasHeightForWidth())
        self.estimateButton.setSizePolicy(sizePolicy2)
        self.estimateButton.setMinimumSize(QSize(0, 0))
        self.estimateButton.setBaseSize(QSize(0, 0))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistShuffle))
        self.estimateButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.estimateButton)

        self.estimateLabel = QLabel(self.frame)
        self.estimateLabel.setObjectName(u"estimateLabel")
        sizePolicy1.setHeightForWidth(self.estimateLabel.sizePolicy().hasHeightForWidth())
        self.estimateLabel.setSizePolicy(sizePolicy1)
        self.estimateLabel.setFrameShape(QFrame.Shape.StyledPanel)

        self.horizontalLayout_2.addWidget(self.estimateLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 272, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(TradeFundDialog)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(TradeFundDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(TradeFundDialog)
        self.amountEdit.editingFinished.connect(TradeFundDialog.onAmountEditingFinished)
        self.estimateButton.clicked.connect(TradeFundDialog.onEstimateButtonClicked)
        self.okButton.clicked.connect(TradeFundDialog.accept)
        self.cancelButton.clicked.connect(TradeFundDialog.reject)

        QMetaObject.connectSlotsByName(TradeFundDialog)
    # setupUi

    def retranslateUi(self, TradeFundDialog):
        TradeFundDialog.setWindowTitle(QCoreApplication.translate("TradeFundDialog", u"\u57fa\u91d1\u64cd\u4f5c", None))
        self.dateLabel.setText(QCoreApplication.translate("TradeFundDialog", u"\u4ea4\u6613\u65e5\u671f:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("TradeFundDialog", u"yyyy-MM-dd", None))
        self.amountLabel.setText(QCoreApplication.translate("TradeFundDialog", u"\u4ea4\u6613\u6570\u91cf:", None))
        self.estimateButton.setText("")
        self.estimateLabel.setText("")
        self.okButton.setText(QCoreApplication.translate("TradeFundDialog", u"\u786e\u5b9a", None))
        self.cancelButton.setText(QCoreApplication.translate("TradeFundDialog", u"\u53d6\u6d88", None))
    # retranslateUi

