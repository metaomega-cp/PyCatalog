from ui.main.side_tree import CustomNode
import os
import json

class TreeManager():
    def __init__(self, app):
        self.app = app
        self.side_tree = self.app.ui_manager.side_tree
        self.side_tree.listeners.append(self)
        self.side_tree.main_model.tooltip_provider = self

        self.tooltips = {}
        self.miniapps = []

        self.initTree()

    def initTree(self):
        c1=CustomNode("folder", ["folder"])
        c1.addChild(CustomNode("inside", ["inside"]))
        self.side_tree.main_model.addChild(c1)
        with open("excluded-apps.json", "r") as f:
            excluded = json.loads(f.read())
        for app_name in os.listdir("miniapps"):
            if app_name in excluded:
                continue
            if app_name[:3].isnumeric() and os.path.isdir(f"miniapps/{app_name}"):
                name = app_name
                tooltip = "No Tooltip Provided"
                if os.path.exists(f"miniapps/{app_name}/about.json"):
                    with open(f"miniapps/{app_name}/about.json", "r") as f:
                        about=json.loads(f.read())
                        if "disable" in about.keys():
                            continue
                        name = about["name"]
                        tooltip = about["short_description"]
                self.miniapps.append(app_name)
                self.tooltips[app_name] = tooltip
                self.side_tree.main_model.addChild(CustomNode(app_name,[name]))

    def get_tooltip_for_id(self,id):
        return self.tooltips[id]
    # EVENTS
    def selection_changed(self,nodes):
        [print("sel changed",node.id) for node in nodes]
    def item_expanded(self,node):
        if isinstance(node, CustomNode):
            print("item expanded", node.id)
    def item_collapsed(self,node):
        if isinstance(node, CustomNode):
            print("item collapsed", node.id)
    def item_doubleClicked(self,node):
        if node.id in self.miniapps:
            self.app.tabs_manager.open_miniapp(node.id)
    def item_enterPressed(self,nodes):
        [self.app.tabs_manager.open_miniapp(node.id) for node in nodes]



