import ui.main.main_ui
import ui.main.side_tree

class UiManager():
    def __init__(self, app):
        self.app = app
        self.init_Root()

    def init_Root(self):
        self.root_ui = ui.main.main_ui.Ui_MainWindow()
        self.root_ui.setupUi(self.app.main_window)
        self.side_tree = ui.main.side_tree.SideTree(self.app, self.root_ui.tree_space)
