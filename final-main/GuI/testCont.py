# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testCont.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 302)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.perK = QtWidgets.QPushButton(self.centralwidget)
        self.perK.setGeometry(QtCore.QRect(50, 60, 131, 23))
        self.perK.setObjectName("perK")
        self.perSize = QtWidgets.QPushButton(self.centralwidget)
        self.perSize.setGeometry(QtCore.QRect(360, 60, 181, 23))
        self.perSize.setObjectName("perSize")
        self.perT = QtWidgets.QPushButton(self.centralwidget)
        self.perT.setGeometry(QtCore.QRect(200, 60, 141, 23))
        self.perT.setObjectName("perT")
        self.perK_2 = QtWidgets.QPushButton(self.centralwidget)
        self.perK_2.setGeometry(QtCore.QRect(50, 190, 131, 23))
        self.perK_2.setObjectName("perK_2")
        self.perT_2 = QtWidgets.QPushButton(self.centralwidget)
        self.perT_2.setGeometry(QtCore.QRect(200, 190, 141, 23))
        self.perT_2.setObjectName("perT_2")
        self.perSize_2 = QtWidgets.QPushButton(self.centralwidget)
        self.perSize_2.setGeometry(QtCore.QRect(360, 190, 181, 23))
        self.perSize_2.setObjectName("perSize_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 61, 16))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 20, 491, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(543, 30, 20, 81))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 100, 551, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 91, 16))
        self.label_2.setObjectName("label_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(90, 150, 461, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(540, 160, 20, 81))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 230, 551, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 21))
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
        self.perK.setText(_translate("MainWindow", "Changing values of k"))
        self.perSize.setText(_translate("MainWindow", "Changing values of graphe size"))
        self.perT.setText(_translate("MainWindow", "Changing values of T"))
        self.perK_2.setText(_translate("MainWindow", "Changing values of k"))
        self.perT_2.setText(_translate("MainWindow", "Changing values of T"))
        self.perSize_2.setText(_translate("MainWindow", "Changing values of graphe size"))
        self.label.setText(_translate("MainWindow", "Modularite"))
        self.label_2.setText(_translate("MainWindow", "Random selection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
