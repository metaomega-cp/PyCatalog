from PyQt6 import QtCore, QtGui, QtWidgets


# - centralwidget
#     - big_widget_1
#         - splitter_treeview_rest
#             - tree_space
#             - big_widget_2
#                 - splitter_tabs_sideoptions
#                     - tabWidget
#                     - splitter_sideoptions
#                 - splitter_table

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Main UI Structure
        self.big_widget_1 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.big_widget_1.setObjectName("big_widget_1")

        self.splitter_treeview_rest = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.splitter_treeview_rest.setContentsMargins(0, 0, 0, 0)
        self.splitter_treeview_rest.setObjectName("splitter_treeview_rest")
        self.big_widget_1.addWidget(self.splitter_treeview_rest)

        self.tree_space = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.tree_space.setObjectName("tree_space")
        self.splitter_treeview_rest.addWidget(self.tree_space)

        self.big_widget_2 = QtWidgets.QSplitter(QtCore.Qt.Orientation.Vertical)
        self.big_widget_2.setObjectName("big_widget_2")
        self.splitter_treeview_rest.addWidget(self.big_widget_2)

        self.splitter_tabs_sideoptions = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.splitter_tabs_sideoptions.setObjectName("splitter_tabs_sideoptions")
        self.big_widget_2.addWidget(self.splitter_tabs_sideoptions)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.splitter_tabs_sideoptions.addWidget(self.tabWidget)

        self.splitter_sideoptions = QtWidgets.QSplitter(QtCore.Qt.Orientation.Vertical)
        self.splitter_sideoptions.setObjectName("splitter_sideoptions")
        self.splitter_tabs_sideoptions.addWidget(self.splitter_sideoptions)

        self.splitter_table = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.splitter_table.setObjectName("splitter_table")
        self.big_widget_2.addWidget(self.splitter_table)




        # splitter_sideoptions
        # self.pushButton_2 = QtWidgets.QPushButton(self.splitter_sideoptions)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_2.setText("PushButton")
        # self.splitter_sideoptions.addWidget(self.pushButton_2)

        self.widget = QtWidgets.QWidget(self.splitter_sideoptions)
        self.widget.setObjectName("label")
        # self.label.setText("label")
        self.splitter_sideoptions.addWidget(self.widget)


        # splitter_sideoptions
        self.tablita = QtWidgets.QTableWidget(self.centralwidget)
        # self.tablita.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tablita.setRowCount(3)
        self.tablita.setColumnCount(4)
        self.tablita.setObjectName("tablita")
        self.splitter_table.addWidget(self.tablita)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        # self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.splitter_treeview_rest.setSizes([100,500])
        self.splitter_tabs_sideoptions.setSizes([500,100])
        self.big_widget_2.setSizes([500,100])





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuEdit.setTitle(_translate("MainWindow", "E&dit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Setti&ngs"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuHelp.setTitle(_translate("MainWindow", "Hel&p"))

