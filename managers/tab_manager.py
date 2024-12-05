
import json
import importlib
import pip
from typing import List, Optional


import PyQt6.QtWidgets
import PyQt6.QtGui
import PyQt6.QtCore

class TabManager():
    def __init__(self, app):
        self.app = app
        self.miniapps_classes = {}
        self.tabWidget = self.app.ui_manager.root_ui.tabWidget

        self.initEventHandlers()

    def initEventHandlers(self):
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tabWidget.currentChanged.connect(lambda index: print(f"Current tab changed to {index}"))

    def closeTab(self, index):
        print(index)
        self.tabWidget.removeTab(index)

    def open_miniapp(self, miniapp):
        try:
            self.miniapps_classes[miniapp] = importlib.import_module(f"miniapps.{miniapp}.miniapp")
            a = self.miniapps_classes[miniapp].MiniApp()
            tab_1_pot = a.get_ui()
            tab_1_pot.setObjectName(miniapp)
            self.tabWidget.addTab(tab_1_pot, miniapp)
        except ModuleNotFoundError as e:
            tab_1_pot = self.getModuleNotFoundTab(miniapp)
            tab_1_pot.setObjectName(miniapp)
            self.tabWidget.addTab(tab_1_pot, miniapp)
        self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)

    def getModuleNotFoundTab(self, miniapp):
        ui = PyQt6.QtWidgets.QWidget()
        layout = PyQt6.QtWidgets.QVBoxLayout()
        ui.setLayout(layout)

        label = PyQt6.QtWidgets.QLabel()
        with open(f"miniapps/{miniapp}/about.json", "r") as f:
            modules = json.loads(f.read())['required_modules']
        label.setText(f"Some modules may be lacking. '{miniapp}' requires the following modules to run:\n{modules}\nDo you want to install them?")
        label.setFixedSize(1000, 50)
        label.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(label)

        self.button = PyQt6.QtWidgets.QPushButton()
        self.button.setText("Install modules")
        label.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignTop)

        self.button.clicked.connect(lambda: self.install_modules(miniapp, modules))
        layout.addWidget(self.button)

        return ui

    def install_modules(self,miniapp,modules):
        self.button.setEnabled(False)
        self.button.setText(f"Install modules (LOADING)")
        pip.main(["install"]+modules.split(","))
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        self.open_miniapp(miniapp)