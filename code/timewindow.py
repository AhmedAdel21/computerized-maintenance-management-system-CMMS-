# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timewindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class timewindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 712)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(157, 157, 157);\n"
"")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)
        self.timelayout = QtWidgets.QFormLayout()
        self.timelayout.setContentsMargins(100, 20, -1, -1)
        self.timelayout.setHorizontalSpacing(200)
        self.timelayout.setVerticalSpacing(20)
        self.timelayout.setObjectName("timelayout")
        self.label1_1 = QtWidgets.QLabel(self.centralwidget)
        self.label1_1.setObjectName("label1_1")
        self.timelayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1_1)
        self.check1_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_1.setText("")
        self.check1_1.setObjectName("check1_1")
        self.timelayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.check1_1)
        self.label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label1_2.setObjectName("label1_2")
        self.timelayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label1_2)
        self.check1_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_2.setText("")
        self.check1_2.setObjectName("check1_2")
        self.timelayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.check1_2)
        self.label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label1_3.setObjectName("label1_3")
        self.timelayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label1_3)
        self.check1_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_3.setText("")
        self.check1_3.setObjectName("check1_3")
        self.timelayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.check1_3)
        self.label1_4 = QtWidgets.QLabel(self.centralwidget)
        self.label1_4.setObjectName("label1_4")
        self.timelayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label1_4)
        self.check1_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_4.setText("")
        self.check1_4.setObjectName("check1_4")
        self.timelayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.check1_4)
        self.label1_5 = QtWidgets.QLabel(self.centralwidget)
        self.label1_5.setObjectName("label1_5")
        self.timelayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label1_5)
        self.check1_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_5.setText("")
        self.check1_5.setObjectName("check1_5")
        self.timelayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.check1_5)
        self.label1_6 = QtWidgets.QLabel(self.centralwidget)
        self.label1_6.setObjectName("label1_6")
        self.timelayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label1_6)
        self.check1_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_6.setText("")
        self.check1_6.setObjectName("check1_6")
        self.timelayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.check1_6)
        self.label1_7 = QtWidgets.QLabel(self.centralwidget)
        self.label1_7.setObjectName("label1_7")
        self.timelayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label1_7)
        self.check1_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_7.setText("")
        self.check1_7.setObjectName("check1_7")
        self.timelayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.check1_7)
        self.label1_8 = QtWidgets.QLabel(self.centralwidget)
        self.label1_8.setObjectName("label1_8")
        self.timelayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label1_8)
        self.check1_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_8.setText("")
        self.check1_8.setObjectName("check1_8")
        self.timelayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.check1_8)
        self.label1_9 = QtWidgets.QLabel(self.centralwidget)
        self.label1_9.setObjectName("label1_9")
        self.timelayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label1_9)
        self.check1_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_9.setText("")
        self.check1_9.setObjectName("check1_9")
        self.timelayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.check1_9)
        self.label1_10 = QtWidgets.QLabel(self.centralwidget)
        self.label1_10.setObjectName("label1_10")
        self.timelayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label1_10)
        self.check1_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_10.setText("")
        self.check1_10.setObjectName("check1_10")
        self.timelayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.check1_10)
        self.label1_11 = QtWidgets.QLabel(self.centralwidget)
        self.label1_11.setObjectName("label1_11")
        self.timelayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label1_11)
        self.check1_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_11.setText("")
        self.check1_11.setObjectName("check1_11")
        self.timelayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.check1_11)
        self.label1_12 = QtWidgets.QLabel(self.centralwidget)
        self.label1_12.setObjectName("label1_12")
        self.timelayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label1_12)
        self.check1_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_12.setText("")
        self.check1_12.setObjectName("check1_12")
        self.timelayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.check1_12)
        self.label1_13 = QtWidgets.QLabel(self.centralwidget)
        self.label1_13.setObjectName("label1_13")
        self.timelayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label1_13)
        self.check1_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_13.setText("")
        self.check1_13.setObjectName("check1_13")
        self.timelayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.check1_13)
        self.label1_14 = QtWidgets.QLabel(self.centralwidget)
        self.label1_14.setObjectName("label1_14")
        self.timelayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label1_14)
        self.check1_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_14.setText("")
        self.check1_14.setObjectName("check1_14")
        self.timelayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.check1_14)
        self.label1_15 = QtWidgets.QLabel(self.centralwidget)
        self.label1_15.setObjectName("label1_15")
        self.timelayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label1_15)
        self.check1_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_15.setText("")
        self.check1_15.setObjectName("check1_15")
        self.timelayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.check1_15)
        self.label1_16 = QtWidgets.QLabel(self.centralwidget)
        self.label1_16.setObjectName("label1_16")
        self.timelayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label1_16)
        self.check1_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_16.setText("")
        self.check1_16.setObjectName("check1_16")
        self.timelayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.check1_16)
        self.label1_17 = QtWidgets.QLabel(self.centralwidget)
        self.label1_17.setObjectName("label1_17")
        self.timelayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label1_17)
        self.check1_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.check1_17.setText("")
        self.check1_17.setObjectName("check1_17")
        self.timelayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.check1_17)
        self.gridLayout.addLayout(self.timelayout, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(250, -1, 20, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.retrive = QtWidgets.QPushButton(self.centralwidget)
        self.retrive.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.retrive.setObjectName("retrive")
        self.verticalLayout.addWidget(self.retrive)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "choose time "))
        self.label_24.setText(_translate("MainWindow", "Choose a Time"))
        self.label1_1.setText(_translate("MainWindow", "TextLabel"))
        self.label1_2.setText(_translate("MainWindow", "TextLabel"))
        self.label1_3.setText(_translate("MainWindow", "TextLabel"))
        self.label1_4.setText(_translate("MainWindow", "TextLabel"))
        self.label1_5.setText(_translate("MainWindow", "TextLabel"))
        self.label1_6.setText(_translate("MainWindow", "TextLabel"))
        self.label1_7.setText(_translate("MainWindow", "TextLabel"))
        self.label1_8.setText(_translate("MainWindow", "TextLabel"))
        self.label1_9.setText(_translate("MainWindow", "TextLabel"))
        self.label1_10.setText(_translate("MainWindow", "TextLabel"))
        self.label1_11.setText(_translate("MainWindow", "TextLabel"))
        self.label1_12.setText(_translate("MainWindow", "TextLabel"))
        self.label1_13.setText(_translate("MainWindow", "TextLabel"))
        self.label1_14.setText(_translate("MainWindow", "TextLabel"))
        self.label1_15.setText(_translate("MainWindow", "TextLabel"))
        self.label1_16.setText(_translate("MainWindow", "TextLabel"))
        self.label1_17.setText(_translate("MainWindow", "TextLabel"))
        self.retrive.setText(_translate("MainWindow", "Retrive"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = timewindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
