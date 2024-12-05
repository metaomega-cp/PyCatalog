
from managers.UiManager import UiManager
from managers.tab_manager import TabManager
from managers.properties_manager import PropertiesManager
from managers.tree_manager import TreeManager


class App():
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui_manager = UiManager(self)
        self.tabs_manager = TabManager(self)
        self.properties_manager = PropertiesManager(self)
        self.tree_manager = TreeManager(self)

