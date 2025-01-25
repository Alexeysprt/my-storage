import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from triatlon import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("triatlon.ui", self)
        self.score.clicked.connect(self.clickme)

    def clickme(self):
        print("dfsdjhkfj")
        res=(int(self.stone_run))+(int(self.stone_swim))+(int(self.stone_bike))
        self.stone_allTime=res
        res2=(int(self.cactoo_run))+(int(self.cactoo_swim))+(int(self.cactoo_bike))
        self.cactoo_allTime=res2
        res3=(int(self.donkey_run))+(int(self.donkey_swim))+(int(self.donkey_bike))
        self.donkey_allTime=res3
    
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()