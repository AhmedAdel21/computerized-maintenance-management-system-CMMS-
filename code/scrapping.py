# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrap.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class scrapping(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 594)
        MainWindow.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(157, 157, 157);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.scrappingDate = QtWidgets.QDateEdit(self.centralwidget)
        self.scrappingDate.setObjectName("scrappingDate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.scrappingDate)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.requestedBy = QtWidgets.QLineEdit(self.centralwidget)
        self.requestedBy.setObjectName("requestedBy")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.requestedBy)
        self.reasonsForDisposition = QtWidgets.QTextEdit(self.centralwidget)
        self.reasonsForDisposition.setObjectName("reasonsForDisposition")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reasonsForDisposition)
        self.department = QtWidgets.QLabel(self.centralwidget)
        self.department.setObjectName("department")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.department)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.serialNumber = QtWidgets.QLabel(self.centralwidget)
        self.serialNumber.setObjectName("serialNumber")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.serialNumber)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.scrappingSave = QtWidgets.QPushButton(self.centralwidget)
        self.scrappingSave.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scrappingSave.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.scrappingSave.setObjectName("scrappingSave")
        self.gridLayout_2.addWidget(self.scrappingSave, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scrapping Report"))
        self.label.setText(_translate("MainWindow", "Scrapping Report"))
        self.label_2.setText(_translate("MainWindow", "Date"))
        self.scrappingDate.setDisplayFormat(_translate("MainWindow", "yyyy-M-d"))
        self.label_3.setText(_translate("MainWindow", "Requested By"))
        self.label_4.setText(_translate("MainWindow", "Department"))
        self.label_5.setText(_translate("MainWindow", "Reasons for Disposition"))
        self.department.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Serial Number"))
        self.serialNumber.setText(_translate("MainWindow", "Serial Number"))
        self.scrappingSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = scrapping()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
