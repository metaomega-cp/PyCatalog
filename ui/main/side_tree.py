from PyQt6 import QtCore, QtWidgets

class SideTree(QtWidgets.QTreeView):
    def __init__(self, app, parent=None, *args, **kwargs):
        super().__init__()
        self.app = app
        self.listeners = []
        self.initUI(parent)

        self.main_model = Model1()
        self.setModel(self.main_model)

        self.initEventHandlers()

    def initUI(self,parent):
        parent.addWidget(self)

        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.setStyleSheet("")
        self.setAutoExpandDelay(5)

        self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)

        self.customContextMenuRequested.connect(self.openMenu)

    def initEventHandlers(self):
        self.selectionModel().selectionChanged.connect(self.on_item_selection_changed)
        self.expanded.connect(self.on_item_expanded)
        self.collapsed.connect(self.on_item_collapsed)
        self.doubleClicked.connect(self.on_treeView_doubleClicked)
        self.installEventFilter(self)

    def openMenu(self, position):
        indexes = self.selectedIndexes()
        if len(indexes) > 0:
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1

            menu = QtWidgets.QMenu()
            if level == 0:
                menu.addAction(self.tr("Edit person"))
            elif level == 1:
                menu.addAction(self.tr("Edit object/container"))
            elif level == 2:
                menu.addAction(self.tr("Edit object"))

            menu.exec_(self.viewport().mapToGlobal(position))

# EVENT HANDLERS
    def on_item_selection_changed(self, selected, current):
        [listener.selection_changed([i.internalPointer() for i in selected.indexes()]) for listener in self.listeners]

    def on_item_expanded(self, index):
        [listener.item_expanded(index.internalPointer()) for listener in self.listeners]

    def on_item_collapsed(self, index):
        [listener.item_collapsed(index.internalPointer()) for listener in self.listeners]

    def on_treeView_doubleClicked(self, index):
        [listener.item_doubleClicked(index.internalPointer()) for listener in self.listeners]

    def eventFilter(self, obj, event):
        if obj == self and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.EnterKeyType.EnterKeyReturn:
                [listener.item_enterPressed([index.internalPointer() for index in self.selectedIndexes()]) for listener in self.listeners]
                return True  # Consume the event
        return False



class Model1(QtCore.QAbstractItemModel):
    def __init__(self):
        QtCore.QAbstractItemModel.__init__(self)
        self._root = RootNode()
        self.tooltip_provider = None

    def addChildren(self, nodes):
        for node in nodes:
            self._root.addChild(node)

    def rowCount(self, index):
        if index.isValid():
            return index.internalPointer().childCount()
        return self._root.childCount()

    def addChild(self, node):
        self._root.addChild(node)

    def index(self, row, column, _parent=None):
        if not _parent or not _parent.isValid():
            parent = self._root
        else:
            parent = _parent.internalPointer()

        if not QtCore.QAbstractItemModel.hasIndex(self, row, column, _parent):
            return QtCore.QModelIndex()

        child = parent.child(row)
        if child:
            return QtCore.QAbstractItemModel.createIndex(self, row, column, child)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if index.isValid():
            p = index.internalPointer().parent()
            if p:
                return QtCore.QAbstractItemModel.createIndex(self, p.row(), 0, p)
        return QtCore.QModelIndex()

    def columnCount(self, index):
        if index.isValid():
            return index.internalPointer().columnCount()
        return self._root.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return node.data(index.column())
        if role == QtCore.Qt.ItemDataRole.ToolTipRole:
            if isinstance(node,CustomNode):
                return self.tooltip_provider.get_tooltip_for_id(node.id)
        return None

    # def flags(self, index):
    #     if not index.isValid():
    #         return QtCore.Qt.NoItemFlags # 0
    #     return QtCore.Qt.ItemIsSelectable # or Qt.ItemIsEnabled

class RootNode(object):
    def __init__(self):
        self._columncount = 0
        self._children = []
        self._parent = None
        self._row = 0

    def columnCount(self):
        return self._columncount

    def childCount(self):
        return len(self._children)

    def child(self, row):
        if row >= 0 and row < self.childCount():
            return self._children[row]

    def parent(self):
        return self._parent

    def row(self):
        return self._row

    def addChild(self, child):
        child._parent = self
        child._row = len(self._children)
        self._children.append(child)
        self._columncount = max(child.columnCount(), self._columncount)

class CustomNode(object):
    def __init__(self, id, data):
        self.id = id
        self._data = data
        if type(data) == tuple:
            self._data = list(data)
        if type(data) is str or not hasattr(data, '__getitem__'):
            self._data = [data]

        self._columncount = len(self._data)
        self._children = []
        self._parent = None
        self._row = 0

        # self.setToolTip("This is item 1")

    def data(self, column):
        if column >= 0 and column < len(self._data):
            return self._data[column]

    def columnCount(self):
        return self._columncount

    def childCount(self):
        return len(self._children)

    def child(self, row):
        if row >= 0 and row < self.childCount():
            return self._children[row]

    def parent(self):
        return self._parent

    def row(self):
        return self._row

    def addChild(self, child):
        child._parent = self
        child._row = len(self._children)
        self._children.append(child)
        self._columncount = max(child.columnCount(), self._columncount)

    def data_string(self):
        s=self._data[0]
        for i in range(1, len(self._data)):
            s += f" - {self._data[i]}"
        return s



