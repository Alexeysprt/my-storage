# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'triatlon.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(310, 30, 101, 41))
        self.name.setObjectName("name")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(80, 120, 47, 13))
        self.time.setObjectName("time")
        self.stone = QtWidgets.QLabel(self.centralwidget)
        self.stone.setGeometry(QtCore.QRect(240, 120, 47, 13))
        self.stone.setObjectName("stone")
        self.cactoo = QtWidgets.QLabel(self.centralwidget)
        self.cactoo.setGeometry(QtCore.QRect(410, 120, 47, 13))
        self.cactoo.setObjectName("cactoo")
        self.donkey = QtWidgets.QLabel(self.centralwidget)
        self.donkey.setGeometry(QtCore.QRect(580, 120, 47, 13))
        self.donkey.setObjectName("donkey")
        self.run = QtWidgets.QLabel(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(80, 190, 47, 13))
        self.run.setObjectName("run")
        self.swim = QtWidgets.QLabel(self.centralwidget)
        self.swim.setGeometry(QtCore.QRect(70, 270, 61, 16))
        self.swim.setObjectName("swim")
        self.bike = QtWidgets.QLabel(self.centralwidget)
        self.bike.setGeometry(QtCore.QRect(70, 350, 71, 16))
        self.bike.setObjectName("bike")
        self.AllTime = QtWidgets.QLabel(self.centralwidget)
        self.AllTime.setGeometry(QtCore.QRect(60, 440, 91, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.AllTime.setFont(font)
        self.AllTime.setObjectName("AllTime")
        self.stone_run = QtWidgets.QLineEdit(self.centralwidget)
        self.stone_run.setGeometry(QtCore.QRect(200, 190, 113, 20))
        self.stone_run.setObjectName("stone_run")
        self.stone_swim = QtWidgets.QLineEdit(self.centralwidget)
        self.stone_swim.setGeometry(QtCore.QRect(200, 260, 113, 20))
        self.stone_swim.setObjectName("stone_swim")
        self.stone_bike = QtWidgets.QLineEdit(self.centralwidget)
        self.stone_bike.setGeometry(QtCore.QRect(200, 350, 113, 20))
        self.stone_bike.setObjectName("stone_bike")
        self.stone_allTime = QtWidgets.QLineEdit(self.centralwidget)
        self.stone_allTime.setGeometry(QtCore.QRect(200, 440, 113, 20))
        self.stone_allTime.setObjectName("stone_allTime")
        self.cactoo_run = QtWidgets.QLineEdit(self.centralwidget)
        self.cactoo_run.setGeometry(QtCore.QRect(380, 190, 113, 20))
        self.cactoo_run.setObjectName("cactoo_run")
        self.cactoo_swim = QtWidgets.QLineEdit(self.centralwidget)
        self.cactoo_swim.setGeometry(QtCore.QRect(380, 260, 113, 20))
        self.cactoo_swim.setObjectName("cactoo_swim")
        self.cactoo_bike = QtWidgets.QLineEdit(self.centralwidget)
        self.cactoo_bike.setGeometry(QtCore.QRect(380, 350, 113, 20))
        self.cactoo_bike.setObjectName("cactoo_bike")
        self.cactoo_allTime = QtWidgets.QLineEdit(self.centralwidget)
        self.cactoo_allTime.setGeometry(QtCore.QRect(380, 440, 113, 20))
        self.cactoo_allTime.setObjectName("cactoo_allTime")
        self.donkey_run = QtWidgets.QLineEdit(self.centralwidget)
        self.donkey_run.setGeometry(QtCore.QRect(560, 190, 113, 20))
        self.donkey_run.setObjectName("donkey_run")
        self.donkey_swim = QtWidgets.QLineEdit(self.centralwidget)
        self.donkey_swim.setGeometry(QtCore.QRect(560, 260, 113, 20))
        self.donkey_swim.setObjectName("donkey_swim")
        self.donkey_bike = QtWidgets.QLineEdit(self.centralwidget)
        self.donkey_bike.setGeometry(QtCore.QRect(560, 350, 113, 20))
        self.donkey_bike.setObjectName("donkey_bike")
        self.donkey_allTime = QtWidgets.QLineEdit(self.centralwidget)
        self.donkey_allTime.setGeometry(QtCore.QRect(560, 440, 113, 20))
        self.donkey_allTime.setObjectName("donkey_allTime")
        self.score = QtWidgets.QPushButton(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(70, 510, 75, 23))
        self.score.setObjectName("score")
        self.champion = QtWidgets.QPushButton(self.centralwidget)
        self.champion.setGeometry(QtCore.QRect(350, 520, 75, 23))
        self.champion.setObjectName("champion")
        self.champions = QtWidgets.QLineEdit(self.centralwidget)
        self.champions.setGeometry(QtCore.QRect(510, 520, 113, 20))
        self.champions.setObjectName("champions")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Триатлон"))
        self.time.setText(_translate("MainWindow", "Время"))
        self.stone.setText(_translate("MainWindow", "Камушек"))
        self.cactoo.setText(_translate("MainWindow", "Кактус"))
        self.donkey.setText(_translate("MainWindow", "Осел"))
        self.run.setText(_translate("MainWindow", "Бег"))
        self.swim.setText(_translate("MainWindow", "Плавание"))
        self.bike.setText(_translate("MainWindow", "Велосипед"))
        self.AllTime.setText(_translate("MainWindow", "общее время"))
        self.score.setText(_translate("MainWindow", "Счет"))
        self.champion.setText(_translate("MainWindow", "Чемпион"))
