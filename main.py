from PyQt6 import QtCore, QtGui, QtWidgets

import sys
from application import App


def window():

    qApp = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    # InitManager
    MainWindow.showMaximized()
    application = App(MainWindow)

    MainWindow.show()

    sys.exit(qApp.exec())
if __name__ == '__main__':
       window()