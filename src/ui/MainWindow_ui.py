# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolBar, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1262, 810)
        mainWindow.setStyleSheet(u"QToolBar\n"
"{\n"
"	spacing:5px;\n"
"	border: none;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"	margin: 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QLabel#itemNameLabel\n"
"{\n"
"	font: 16px;\n"
"}\n"
"\n"
"QLabel#itemCodeLabel\n"
"{\n"
"	color: #999999;\n"
"}\n"
"\n"
"QLabel#currentValueLabel\n"
"{\n"
"	font: bold 16px;\n"
"	color: #990000;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	border: none;\n"
"}")
        mainWindow.setIconSize(QSize(16, 16))
        self.actionLogin = QAction(mainWindow)
        self.actionLogin.setObjectName(u"actionLogin")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.actionLogin.setIcon(icon)
        self.actionExit = QAction(mainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemShutdown))
        self.actionExit.setIcon(icon1)
        self.actionAbout = QAction(mainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionAbout.setIcon(icon2)
        self.actionLogout = QAction(mainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionLogout.setEnabled(False)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        self.actionLogout.setIcon(icon3)
        self.actionSync = QAction(mainWindow)
        self.actionSync.setObjectName(u"actionSync")
        self.actionSync.setEnabled(True)
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistRepeat))
        self.actionSync.setIcon(icon4)
        self.actionSetup = QAction(mainWindow)
        self.actionSetup.setObjectName(u"actionSetup")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.actionSetup.setIcon(icon5)
        self.actionAnalyzeIndex = QAction(mainWindow)
        self.actionAnalyzeIndex.setObjectName(u"actionAnalyzeIndex")
        self.actionTradeFund = QAction(mainWindow)
        self.actionTradeFund.setObjectName(u"actionTradeFund")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistShuffle))
        self.actionTradeFund.setIcon(icon6)
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.leftWidget = QWidget(self.centralWidget)
        self.leftWidget.setObjectName(u"leftWidget")
        self.leftWidget.setGeometry(QRect(30, 10, 274, 461))
        self.verticalLayout = QVBoxLayout(self.leftWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fundListLabel = QLabel(self.leftWidget)
        self.fundListLabel.setObjectName(u"fundListLabel")
        self.fundListLabel.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setBold(True)
        self.fundListLabel.setFont(font)
        self.fundListLabel.setStyleSheet(u"padding: 2px;font-size: 14px;")
        self.fundListLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.fundListLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.fundListLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.fundListLabel)

        self.fundListWidget = QListWidget(self.leftWidget)
        self.fundListWidget.setObjectName(u"fundListWidget")
        self.fundListWidget.setEnabled(True)
        self.fundListWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fundListWidget.setAlternatingRowColors(True)
        self.fundListWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.fundListWidget)

        self.rightWidget = QWidget(self.centralWidget)
        self.rightWidget.setObjectName(u"rightWidget")
        self.rightWidget.setGeometry(QRect(340, 20, 631, 481))
        self.verticalLayout_2 = QVBoxLayout(self.rightWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.rightWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.fundNameLabel = QLabel(self.frame)
        self.fundNameLabel.setObjectName(u"fundNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fundNameLabel.sizePolicy().hasHeightForWidth())
        self.fundNameLabel.setSizePolicy(sizePolicy)
        self.fundNameLabel.setMinimumSize(QSize(0, 25))
        self.fundNameLabel.setFont(font)
        self.fundNameLabel.setStyleSheet(u"font-size: 14px;")
        self.fundNameLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.fundNameLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.fundNameLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.fundNameLabel)

        self.fundBasicInfoButton = QPushButton(self.frame)
        self.fundBasicInfoButton.setObjectName(u"fundBasicInfoButton")
        self.fundBasicInfoButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.fundBasicInfoButton)

        self.fundNetValueButton = QPushButton(self.frame)
        self.fundNetValueButton.setObjectName(u"fundNetValueButton")
        self.fundNetValueButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.fundNetValueButton)

        self.fundHoldDataButton = QPushButton(self.frame)
        self.fundHoldDataButton.setObjectName(u"fundHoldDataButton")
        self.fundHoldDataButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.fundHoldDataButton)


        self.verticalLayout_2.addWidget(self.frame)

        self.fundDataFrame = QFrame(self.rightWidget)
        self.fundDataFrame.setObjectName(u"fundDataFrame")
        self.fundDataFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.fundDataFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.fundDataFrame)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 10, 5, 10)
        self.label = QLabel(self.fundDataFrame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.fundDataFrame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.fundDataFrame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_13 = QLabel(self.fundDataFrame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)

        self.fundTotalLabel = QLabel(self.fundDataFrame)
        self.fundTotalLabel.setObjectName(u"fundTotalLabel")
        self.fundTotalLabel.setStyleSheet(u"font-size: 20px; font-weight: bold;")

        self.gridLayout.addWidget(self.fundTotalLabel, 1, 0, 1, 1)

        self.fundProfitLabel = QLabel(self.fundDataFrame)
        self.fundProfitLabel.setObjectName(u"fundProfitLabel")
        self.fundProfitLabel.setStyleSheet(u"font-size: 20px; font-weight: bold;")

        self.gridLayout.addWidget(self.fundProfitLabel, 1, 1, 1, 1)

        self.fundProfitRatioLabel = QLabel(self.fundDataFrame)
        self.fundProfitRatioLabel.setObjectName(u"fundProfitRatioLabel")
        self.fundProfitRatioLabel.setStyleSheet(u"font-size: 20px; font-weight: bold;")

        self.gridLayout.addWidget(self.fundProfitRatioLabel, 1, 2, 1, 1)

        self.fundADRatioLabel = QLabel(self.fundDataFrame)
        self.fundADRatioLabel.setObjectName(u"fundADRatioLabel")
        self.fundADRatioLabel.setStyleSheet(u"font-size: 20px; font-weight: bold;")

        self.gridLayout.addWidget(self.fundADRatioLabel, 1, 3, 1, 1)

        self.label_8 = QLabel(self.fundDataFrame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_10 = QLabel(self.fundDataFrame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_12 = QLabel(self.fundDataFrame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)

        self.label_15 = QLabel(self.fundDataFrame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 3, 1, 1)

        self.fundHeldCostLabel = QLabel(self.fundDataFrame)
        self.fundHeldCostLabel.setObjectName(u"fundHeldCostLabel")
        self.fundHeldCostLabel.setStyleSheet(u"font-size: 14px;")

        self.gridLayout.addWidget(self.fundHeldCostLabel, 3, 0, 1, 1)

        self.fundHeldSharesLabel = QLabel(self.fundDataFrame)
        self.fundHeldSharesLabel.setObjectName(u"fundHeldSharesLabel")
        self.fundHeldSharesLabel.setStyleSheet(u"font-size: 14px;")

        self.gridLayout.addWidget(self.fundHeldSharesLabel, 3, 1, 1, 1)

        self.fundNetValueLabel = QLabel(self.fundDataFrame)
        self.fundNetValueLabel.setObjectName(u"fundNetValueLabel")
        self.fundNetValueLabel.setStyleSheet(u"font-size: 14px;")

        self.gridLayout.addWidget(self.fundNetValueLabel, 3, 2, 1, 1)

        self.fundNVDateLabel = QLabel(self.fundDataFrame)
        self.fundNVDateLabel.setObjectName(u"fundNVDateLabel")
        self.fundNVDateLabel.setStyleSheet(u"font-size: 14px;")

        self.gridLayout.addWidget(self.fundNVDateLabel, 3, 3, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout_2.addWidget(self.fundDataFrame)

        self.fundTableWidget = QTableWidget(self.rightWidget)
        if (self.fundTableWidget.columnCount() < 3):
            self.fundTableWidget.setColumnCount(3)
        if (self.fundTableWidget.rowCount() < 3):
            self.fundTableWidget.setRowCount(3)
        self.fundTableWidget.setObjectName(u"fundTableWidget")
        self.fundTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fundTableWidget.setAlternatingRowColors(True)
        self.fundTableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.fundTableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.fundTableWidget.setGridStyle(Qt.PenStyle.DotLine)
        self.fundTableWidget.setRowCount(3)
        self.fundTableWidget.setColumnCount(3)
        self.fundTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.fundTableWidget)

        self.frame_2 = QFrame(self.rightWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(mainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1262, 33))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTool = QMenu(self.menuBar)
        self.menuTool.setObjectName(u"menuTool")
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        mainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(mainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setIconSize(QSize(18, 18))
        self.toolBar.setFloatable(True)
        mainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuTool.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTool.addSeparator()
        self.menuTool.addAction(self.actionSync)
        self.menuTool.addSeparator()
        self.menuTool.addSeparator()
        self.menuTool.addAction(self.actionSetup)
        self.menu.addAction(self.actionTradeFund)
        self.menu.addSeparator()
        self.menu.addAction(self.actionAnalyzeIndex)
        self.toolBar.addAction(self.actionLogin)
        self.toolBar.addAction(self.actionLogout)
        self.toolBar.addAction(self.actionTradeFund)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(mainWindow)
        self.actionLogin.triggered.connect(mainWindow.onActionLoginTriggered)
        self.actionExit.triggered.connect(mainWindow.onActionExitTriggered)
        self.actionLogout.triggered.connect(mainWindow.onActionLogoutTriggered)
        self.actionSync.triggered.connect(mainWindow.onActionSetupDataTriggered)
        self.actionSetup.triggered.connect(mainWindow.onActionSetupFundTriggered)
        self.actionAnalyzeIndex.triggered.connect(mainWindow.onActionAnalyzeIndexTriggered)
        self.actionTradeFund.triggered.connect(mainWindow.onActionTradeFundTriggered)
        self.actionAbout.triggered.connect(mainWindow.onActionAboutTriggered)
        self.fundListWidget.itemSelectionChanged.connect(mainWindow.onFundListWidgetItemSelectionChanged)
        self.fundBasicInfoButton.clicked.connect(mainWindow.onActionFundBasicInfoTriggered)
        self.fundNetValueButton.clicked.connect(mainWindow.onActionFundNetValueTriggered)
        self.fundHoldDataButton.clicked.connect(mainWindow.onActionFundHoldDataTriggered)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.actionLogin.setText(QCoreApplication.translate("mainWindow", u"\u767b\u5f55(&L)...", None))
        self.actionLogin.setIconText(QCoreApplication.translate("mainWindow", u"\u767b\u5f55", None))
#if QT_CONFIG(tooltip)
        self.actionLogin.setToolTip(QCoreApplication.translate("mainWindow", u"\u767b\u5f55\u5e94\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionLogin.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("mainWindow", u"\u9000\u51fa(&Q)", None))
        self.actionExit.setIconText(QCoreApplication.translate("mainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("mainWindow", u"\u9000\u51fa\u5f53\u524d\u5e94\u7528\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("mainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("mainWindow", u"\u5173\u4e8e(&A)...", None))
#if QT_CONFIG(tooltip)
        self.actionAbout.setToolTip(QCoreApplication.translate("mainWindow", u"\u5173\u4e8e...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("mainWindow", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionLogout.setText(QCoreApplication.translate("mainWindow", u"\u6ce8\u9500(&O)", None))
        self.actionLogout.setIconText(QCoreApplication.translate("mainWindow", u"\u6ce8\u9500", None))
#if QT_CONFIG(tooltip)
        self.actionLogout.setToolTip(QCoreApplication.translate("mainWindow", u"\u6ce8\u9500\u8d26\u6237", None))
#endif // QT_CONFIG(tooltip)
        self.actionSync.setText(QCoreApplication.translate("mainWindow", u"\u6570\u636e\u66f4\u65b0(&R)...", None))
        self.actionSync.setIconText(QCoreApplication.translate("mainWindow", u"\u6570\u636e\u66f4\u65b0", None))
#if QT_CONFIG(tooltip)
        self.actionSync.setToolTip(QCoreApplication.translate("mainWindow", u"\u6570\u636e\u66f4\u65b0...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSync.setShortcut(QCoreApplication.translate("mainWindow", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSetup.setText(QCoreApplication.translate("mainWindow", u"\u8bbe\u7f6e(&S)", None))
        self.actionSetup.setIconText(QCoreApplication.translate("mainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.actionSetup.setToolTip(QCoreApplication.translate("mainWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.actionAnalyzeIndex.setText(QCoreApplication.translate("mainWindow", u"\u6307\u6570\u5206\u6790(&I)...", None))
        self.actionAnalyzeIndex.setIconText(QCoreApplication.translate("mainWindow", u"\u6307\u6570\u5206\u6790", None))
#if QT_CONFIG(tooltip)
        self.actionAnalyzeIndex.setToolTip(QCoreApplication.translate("mainWindow", u"\u6307\u6570\u5206\u6790(I)...", None))
#endif // QT_CONFIG(tooltip)
        self.actionTradeFund.setText(QCoreApplication.translate("mainWindow", u"\u57fa\u91d1\u4ea4\u6613(O)...", None))
        self.actionTradeFund.setIconText(QCoreApplication.translate("mainWindow", u"\u57fa\u91d1\u4ea4\u6613", None))
#if QT_CONFIG(tooltip)
        self.actionTradeFund.setToolTip(QCoreApplication.translate("mainWindow", u"\u57fa\u91d1\u4ea4\u6613", None))
#endif // QT_CONFIG(tooltip)
        self.fundListLabel.setText(QCoreApplication.translate("mainWindow", u"\u6240\u9009\u57fa\u91d1\u5217\u8868", None))
        self.fundNameLabel.setText(QCoreApplication.translate("mainWindow", u"\u57fa\u91d1\u540d\u79f0[\u57fa\u91d1\u4ee3\u7801]", None))
        self.fundBasicInfoButton.setText(QCoreApplication.translate("mainWindow", u"\u57fa\u672c\u4fe1\u606f", None))
        self.fundNetValueButton.setText(QCoreApplication.translate("mainWindow", u"\u51c0\u503c\u56fe\u8868", None))
        self.fundHoldDataButton.setText(QCoreApplication.translate("mainWindow", u"\u57fa\u91d1\u6301\u4ed3", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u603b\u8d44\u4ea7:", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u6301\u4ed3\u6536\u76ca:", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\u6536\u76ca\u7387:", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"\u65e5\u6da8\u8dcc:", None))
        self.fundTotalLabel.setText(QCoreApplication.translate("mainWindow", u"000000000.00", None))
        self.fundProfitLabel.setText(QCoreApplication.translate("mainWindow", u"00000000.00", None))
        self.fundProfitRatioLabel.setText(QCoreApplication.translate("mainWindow", u"0.00%", None))
        self.fundADRatioLabel.setText(QCoreApplication.translate("mainWindow", u"0.00%", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"\u6301\u4ed3\u6210\u672c:", None))
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"\u6301\u6709\u4efd\u989d:", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"\u6700\u65b0\u51c0\u503c:", None))
        self.label_15.setText(QCoreApplication.translate("mainWindow", u"\u51c0\u503c\u65e5\u671f:", None))
        self.fundHeldCostLabel.setText(QCoreApplication.translate("mainWindow", u"000000000.00", None))
        self.fundHeldSharesLabel.setText(QCoreApplication.translate("mainWindow", u"000000000.00", None))
        self.fundNetValueLabel.setText(QCoreApplication.translate("mainWindow", u"0.0000", None))
        self.fundNVDateLabel.setText(QCoreApplication.translate("mainWindow", u"0000-00-00", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"\u6587\u4ef6(F)", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mainWindow", u"\u5e2e\u52a9(H)", None))
        self.menuTool.setTitle(QCoreApplication.translate("mainWindow", u"\u5de5\u5177(&T)", None))
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u64cd\u4f5c(O)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("mainWindow", u"toolBar", None))
    # retranslateUi

