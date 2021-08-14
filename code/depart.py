# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'depart.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 100)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.surgery = QtWidgets.QPushButton(self.centralwidget)
        self.surgery.setObjectName("surgery")
        self.gridLayout.addWidget(self.surgery, 2, 2, 1, 1)
        self.cardiology = QtWidgets.QPushButton(self.centralwidget)
        self.cardiology.setObjectName("cardiology")
        self.gridLayout.addWidget(self.cardiology, 2, 1, 1, 1)
        self.emergency = QtWidgets.QPushButton(self.centralwidget)
        self.emergency.setObjectName("emergency")
        self.gridLayout.addWidget(self.emergency, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.addNewEquipment = QtWidgets.QPushButton(self.centralwidget)
        self.addNewEquipment.setObjectName("addNewEquipment")
        self.gridLayout.addWidget(self.addNewEquipment, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("image: url(:/newPrefix/Cardiac-Surgery.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("image: url(:/newPrefix/surgical setting teaser.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("image: url(:/newPrefix/08_OVHD-Emergency.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 26))
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
        self.surgery.setText(_translate("MainWindow", "Surgery"))
        self.cardiology.setText(_translate("MainWindow", "Cardiology"))
        self.emergency.setText(_translate("MainWindow", "Emergency"))
        self.addNewEquipment.setText(_translate("MainWindow", "Add new Equipment"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
