# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(5000, 5000))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 801, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CreateTest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateTest.sizePolicy().hasHeightForWidth())
        self.CreateTest.setSizePolicy(sizePolicy)
        self.CreateTest.setMinimumSize(QtCore.QSize(799, 60))
        self.CreateTest.setMaximumSize(QtCore.QSize(799, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.CreateTest.setFont(font)
        self.CreateTest.setObjectName("CreateTest")
        self.verticalLayout.addWidget(self.CreateTest)
        self.PassTest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PassTest.sizePolicy().hasHeightForWidth())
        self.PassTest.setSizePolicy(sizePolicy)
        self.PassTest.setMinimumSize(QtCore.QSize(799, 60))
        self.PassTest.setMaximumSize(QtCore.QSize(799, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.PassTest.setFont(font)
        self.PassTest.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.PassTest.setMouseTracking(False)
        self.PassTest.setAutoFillBackground(False)
        self.PassTest.setObjectName("PassTest")
        self.verticalLayout.addWidget(self.PassTest)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 21))
        self.menubar.setDefaultUp(False)
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
        self.CreateTest.setText(_translate("MainWindow", "Создать тест"))
        self.PassTest.setText(_translate("MainWindow", "Пройти тест"))
