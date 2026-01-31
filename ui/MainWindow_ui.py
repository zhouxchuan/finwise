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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolBar, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1443, 1026)
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
        self.fundTabWidget = QTabWidget(self.centralWidget)
        self.fundTabWidget.setObjectName(u"fundTabWidget")
        self.fundTabWidget.setEnabled(False)
        self.fundTabWidget.setGeometry(QRect(340, 30, 871, 671))
        self.fundTabWidget.setTabBarAutoHide(False)
        self.fundNetvalueWidget = QWidget()
        self.fundNetvalueWidget.setObjectName(u"fundNetvalueWidget")
        self.verticalLayout_3 = QVBoxLayout(self.fundNetvalueWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nvFrame = QFrame(self.fundNetvalueWidget)
        self.nvFrame.setObjectName(u"nvFrame")
        self.nvFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.nvFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.nvFrame)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.fund_name_label = QLabel(self.nvFrame)
        self.fund_name_label.setObjectName(u"fund_name_label")

        self.horizontalLayout_2.addWidget(self.fund_name_label)

        self.fund_code_label = QLabel(self.nvFrame)
        self.fund_code_label.setObjectName(u"fund_code_label")
        self.fund_code_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.fund_code_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.line_3 = QFrame(self.nvFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.anv_name_label = QLabel(self.nvFrame)
        self.anv_name_label.setObjectName(u"anv_name_label")
        self.anv_name_label.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.anv_name_label)

        self.anv_value_label = QLabel(self.nvFrame)
        self.anv_value_label.setObjectName(u"anv_value_label")

        self.horizontalLayout_2.addWidget(self.anv_value_label)

        self.anv_growthrate_label = QLabel(self.nvFrame)
        self.anv_growthrate_label.setObjectName(u"anv_growthrate_label")
        self.anv_growthrate_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.anv_growthrate_label)

        self.line = QFrame(self.nvFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.cnv_name_label = QLabel(self.nvFrame)
        self.cnv_name_label.setObjectName(u"cnv_name_label")

        self.horizontalLayout_2.addWidget(self.cnv_name_label)

        self.cnv_value_label = QLabel(self.nvFrame)
        self.cnv_value_label.setObjectName(u"cnv_value_label")
        self.cnv_value_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_2.addWidget(self.cnv_value_label)

        self.line_2 = QFrame(self.nvFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.nv_lastest_date_label = QLabel(self.nvFrame)
        self.nv_lastest_date_label.setObjectName(u"nv_lastest_date_label")
        self.nv_lastest_date_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.nv_lastest_date_label)


        self.verticalLayout_3.addWidget(self.nvFrame)

        self.fundNetValuePeriodGroupBox = QGroupBox(self.fundNetvalueWidget)
        self.fundNetValuePeriodGroupBox.setObjectName(u"fundNetValuePeriodGroupBox")
        self.fundNetValuePeriodGroupBox.setFlat(False)
        self.horizontalLayout_3 = QHBoxLayout(self.fundNetValuePeriodGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.periodRadioButton1 = QRadioButton(self.fundNetValuePeriodGroupBox)
        self.periodRadioButton1.setObjectName(u"periodRadioButton1")
        self.periodRadioButton1.setChecked(True)

        self.horizontalLayout_3.addWidget(self.periodRadioButton1)

        self.periodRadioButton2 = QRadioButton(self.fundNetValuePeriodGroupBox)
        self.periodRadioButton2.setObjectName(u"periodRadioButton2")

        self.horizontalLayout_3.addWidget(self.periodRadioButton2)

        self.periodRadioButton3 = QRadioButton(self.fundNetValuePeriodGroupBox)
        self.periodRadioButton3.setObjectName(u"periodRadioButton3")

        self.horizontalLayout_3.addWidget(self.periodRadioButton3)

        self.periodRadioButton4 = QRadioButton(self.fundNetValuePeriodGroupBox)
        self.periodRadioButton4.setObjectName(u"periodRadioButton4")

        self.horizontalLayout_3.addWidget(self.periodRadioButton4)

        self.periodRadioButton5 = QRadioButton(self.fundNetValuePeriodGroupBox)
        self.periodRadioButton5.setObjectName(u"periodRadioButton5")

        self.horizontalLayout_3.addWidget(self.periodRadioButton5)


        self.verticalLayout_3.addWidget(self.fundNetValuePeriodGroupBox)

        self.anvChartWidget = QWidget(self.fundNetvalueWidget)
        self.anvChartWidget.setObjectName(u"anvChartWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anvChartWidget.sizePolicy().hasHeightForWidth())
        self.anvChartWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.anvChartWidget)

        self.cnvChartWidget = QWidget(self.fundNetvalueWidget)
        self.cnvChartWidget.setObjectName(u"cnvChartWidget")
        sizePolicy.setHeightForWidth(self.cnvChartWidget.sizePolicy().hasHeightForWidth())
        self.cnvChartWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.cnvChartWidget)

        self.fundTabWidget.addTab(self.fundNetvalueWidget, "")
        self.fundHoldingWidget = QWidget()
        self.fundHoldingWidget.setObjectName(u"fundHoldingWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.fundHoldingWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea = QScrollArea(self.fundHoldingWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 88, 800))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 800))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.holdRatioWidget = QWidget(self.scrollAreaWidgetContents)
        self.holdRatioWidget.setObjectName(u"holdRatioWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.holdRatioWidget.sizePolicy().hasHeightForWidth())
        self.holdRatioWidget.setSizePolicy(sizePolicy2)
        self.holdRatioWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.holdRatioWidget)

        self.holdShareWidget = QWidget(self.scrollAreaWidgetContents)
        self.holdShareWidget.setObjectName(u"holdShareWidget")
        sizePolicy2.setHeightForWidth(self.holdShareWidget.sizePolicy().hasHeightForWidth())
        self.holdShareWidget.setSizePolicy(sizePolicy2)
        self.holdShareWidget.setMinimumSize(QSize(0, 0))
        self.holdShareWidget.setMaximumSize(QSize(16777215, 16777215))
        self.holdShareWidget.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.holdShareWidget)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.holdBondWidget = QWidget(self.scrollAreaWidgetContents)
        self.holdBondWidget.setObjectName(u"holdBondWidget")
        sizePolicy2.setHeightForWidth(self.holdBondWidget.sizePolicy().hasHeightForWidth())
        self.holdBondWidget.setSizePolicy(sizePolicy2)
        self.holdBondWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.holdBondWidget)

        self.holdIndustryWidget = QWidget(self.scrollAreaWidgetContents)
        self.holdIndustryWidget.setObjectName(u"holdIndustryWidget")
        sizePolicy2.setHeightForWidth(self.holdIndustryWidget.sizePolicy().hasHeightForWidth())
        self.holdIndustryWidget.setSizePolicy(sizePolicy2)
        self.holdIndustryWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.holdIndustryWidget)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_5.addWidget(self.scrollArea)

        self.fundTabWidget.addTab(self.fundHoldingWidget, "")
        self.fundScaleWidget = QWidget()
        self.fundScaleWidget.setObjectName(u"fundScaleWidget")
        self.fundTabWidget.addTab(self.fundScaleWidget, "")
        self.fundBasicWidget = QWidget()
        self.fundBasicWidget.setObjectName(u"fundBasicWidget")
        self.verticalLayout_2 = QVBoxLayout(self.fundBasicWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fundBasicTableWidget = QTableWidget(self.fundBasicWidget)
        if (self.fundBasicTableWidget.columnCount() < 2):
            self.fundBasicTableWidget.setColumnCount(2)
        self.fundBasicTableWidget.setObjectName(u"fundBasicTableWidget")
        self.fundBasicTableWidget.setMouseTracking(True)
        self.fundBasicTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fundBasicTableWidget.setAlternatingRowColors(False)
        self.fundBasicTableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.fundBasicTableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.fundBasicTableWidget.setShowGrid(False)
        self.fundBasicTableWidget.setWordWrap(False)
        self.fundBasicTableWidget.setColumnCount(2)
        self.fundBasicTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.fundBasicTableWidget)

        self.fundTabWidget.addTab(self.fundBasicWidget, "")
        self.leftListWidget = QWidget(self.centralWidget)
        self.leftListWidget.setObjectName(u"leftListWidget")
        self.leftListWidget.setGeometry(QRect(30, 10, 274, 461))
        self.verticalLayout = QVBoxLayout(self.leftListWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.leftListWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Shape.StyledPanel)
        self.label.setFrameShadow(QFrame.Shadow.Sunken)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.fundListWidget = QListWidget(self.leftListWidget)
        self.fundListWidget.setObjectName(u"fundListWidget")
        self.fundListWidget.setEnabled(False)
        self.fundListWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fundListWidget.setAlternatingRowColors(True)
        self.fundListWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.fundListWidget)

        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(mainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1443, 33))
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
        self.actionSync.triggered.connect(mainWindow.onActionSyncTriggered)
        self.actionSetup.triggered.connect(mainWindow.onActionSetupTriggered)
        self.fundListWidget.currentRowChanged.connect(mainWindow.onCurrentRowChanged)
        self.fundBasicTableWidget.cellEntered.connect(mainWindow.onFundBasicTableWidgetCellEntered)
        self.periodRadioButton3.clicked.connect(mainWindow.onFundNetValuePeriodChanged)
        self.periodRadioButton2.clicked.connect(mainWindow.onFundNetValuePeriodChanged)
        self.periodRadioButton5.clicked.connect(mainWindow.onFundNetValuePeriodChanged)
        self.periodRadioButton4.clicked.connect(mainWindow.onFundNetValuePeriodChanged)
        self.periodRadioButton1.clicked.connect(mainWindow.onFundNetValuePeriodChanged)
        self.actionAnalyzeIndex.triggered.connect(mainWindow.onActionAnalyzeIndexTriggered)
        self.actionTradeFund.triggered.connect(mainWindow.onActionTradeFundTriggered)
        self.actionAbout.triggered.connect(mainWindow.onActionAboutTriggered)

        self.fundTabWidget.setCurrentIndex(0)


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
        self.fund_name_label.setText("")
        self.fund_code_label.setText("")
        self.anv_name_label.setText(QCoreApplication.translate("mainWindow", u"\u5355\u4f4d\u51c0\u503c", None))
        self.anv_value_label.setText(QCoreApplication.translate("mainWindow", u"0.00", None))
        self.anv_growthrate_label.setText(QCoreApplication.translate("mainWindow", u"0.00", None))
        self.cnv_name_label.setText(QCoreApplication.translate("mainWindow", u"\u7d2f\u8ba1\u51c0\u503c", None))
        self.cnv_value_label.setText(QCoreApplication.translate("mainWindow", u"0.00", None))
        self.nv_lastest_date_label.setText("")
        self.periodRadioButton1.setText(QCoreApplication.translate("mainWindow", u"\u534a\u5e74", None))
        self.periodRadioButton2.setText(QCoreApplication.translate("mainWindow", u"\u4e00\u5e74", None))
        self.periodRadioButton3.setText(QCoreApplication.translate("mainWindow", u"\u4e09\u5e74", None))
        self.periodRadioButton4.setText(QCoreApplication.translate("mainWindow", u"\u4e94\u5e74", None))
        self.periodRadioButton5.setText(QCoreApplication.translate("mainWindow", u"\u6210\u7acb\u6765", None))
        self.fundTabWidget.setTabText(self.fundTabWidget.indexOf(self.fundNetvalueWidget), QCoreApplication.translate("mainWindow", u"\u51c0\u503c", None))
        self.fundTabWidget.setTabText(self.fundTabWidget.indexOf(self.fundHoldingWidget), QCoreApplication.translate("mainWindow", u"\u6301\u4ed3", None))
        self.fundTabWidget.setTabText(self.fundTabWidget.indexOf(self.fundScaleWidget), QCoreApplication.translate("mainWindow", u"\u89c4\u6a21", None))
        self.fundTabWidget.setTabText(self.fundTabWidget.indexOf(self.fundBasicWidget), QCoreApplication.translate("mainWindow", u"\u8d44\u6599", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u6240\u9009\u57fa\u91d1\u5217\u8868", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"\u6587\u4ef6(F)", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mainWindow", u"\u5e2e\u52a9(H)", None))
        self.menuTool.setTitle(QCoreApplication.translate("mainWindow", u"\u5de5\u5177(&T)", None))
        self.menu.setTitle(QCoreApplication.translate("mainWindow", u"\u64cd\u4f5c(O)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("mainWindow", u"toolBar", None))
    # retranslateUi

