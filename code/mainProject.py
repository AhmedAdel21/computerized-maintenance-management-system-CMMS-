
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from department import *
import mysql.connector
from installationMethod import installationMethod
from equipmentMethod import equipmentMethod
from dialyInspectionMethod import dialyInspectionMethod
from scrappingMethod import scrappingnMethod
from timewindowMethod import timewindowMethod




class ApplicationWindow(Ui_MainWindow):
    def __init__ (self, MainWindow):
        super(ApplicationWindow, self).setupUi(MainWindow)

        self.window = QtWidgets.QMainWindow()
        self.window2 = QtWidgets.QMainWindow()
        self.window3 = QtWidgets.QMainWindow()
        self.timewindowMethod = timewindowMethod(self.window3)
        self.timewindowMethod.retrive.clicked.connect(self.dialyInspectionData)
        self.ui = equipmentMethod(self.window)
        self.ui.retrive.clicked.connect(self.retriveData)
        self.ui.make.clicked.connect(self.makeReport)

        self.addNewEquipment.clicked.connect(self.open)
        self.surgery.clicked.connect(lambda:self.report(2))
        self.cardiology.clicked.connect(lambda:self.report(1))
        self.emergency.clicked.connect(lambda:self.report(0))
        
        self.serialNumberSelected=[]
        self.timeSelected = []
        self.errorMesg = ["there is no recorded report for this instrument"]

    def report(self,departmentNumber):
        self.window.show()
        self.departmentSelected = departmentNumber
        self.ui.hideAllWidgets()
        connect = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="mysql",
                                db= "Hospital"
                                )
        cursor = connect.cursor()

        query = """SELECT serialNumber , `name`
        FROM equipment
        WHERE 
        department= %s"""
        cursor.execute(query,(str(departmentNumber),))
        nextrow = 0
        for i in cursor.fetchall():
            for g in i:
                # print(g)
                if type(g) == int:
                    self.serialNumberSelected.append(g)
                self.ui.reportLables[nextrow].show()
                self.ui.reportCheckbox[nextrow].show()
                self.ui.reportLables[nextrow].setText(str(g))
            nextrow +=1
        # print("serial number = "+ str(self.serialNumberSelected))
        
        # MainWindow.hide()

    def dialyInspectionData(self):
        self.dialyInspectionWindow = dialyInspectionMethod(self.window2) 
        # self.dialyInspectionWindow.serial = self.serial
        
        time = self.timeSelected[self.timewindowMethod.buttongroup.checkedId()]
        # self.departmentSelected = departmentNumber
        print(time)
        connect = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="mysql",
                                db= "Hospital"
                                )
        cursor = connect.cursor()

        query = """SELECT row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15,row16,row17,row18,row19
                FROM dialy_inspection
                WHERE 
                time = %s"""
        cursor.execute(query,(str(time),))
        for i in cursor.fetchall():
            nextrow=0
            for g in i:
                print(g)
                if g != -1:
                    self.dialyInspectionWindow.buttongroupList[nextrow].button(g).setChecked(True)
                nextrow+=1
        # print("serial number = "+ str(self.serialNumberSelected))
        # MainWindow.hide()
        self.window2.show()

    def makeReport(self):
        if self.ui.buttongroup.checkedId() != -1:
            self.serial = self.serialNumberSelected[self.ui.buttongroup.checkedId()]
            if self.ui.chooseReport.currentIndex() == 0:
                self.dialyInspectionWindow = dialyInspectionMethod(self.window2) 
                self.dialyInspectionWindow.serial = self.serial
                self.window2.show()

            if self.ui.chooseReport.currentIndex() == 1:
                self.scrappingWindow = scrappingnMethod(self.window2)
                self.window2.show()
                self.scrappingWindow.serialNumber.setText(str(self.serial))
                if self.departmentSelected == 2:
                    self.scrappingWindow.department.setText("Surgery")
                elif self.departmentSelected == 1:
                    self.scrappingWindow.department.setText("cardiology")
                else:
                    self.scrappingWindow.department.setText("emergency")
            
    def showMessage(self,type):
        '''
        popup a specific error message depend on type sent
        '''
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(self.errorMesg[type])
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()


    def retriveData(self):
        # print(self.ui.buttongroup.checkedId())
        if self.ui.buttongroup.checkedId() != -1:
            connect = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="mysql",
                                db= "Hospital"
                                )
            cursor = connect.cursor()
            
            if self.ui.chooseReport.currentIndex() == 0:

                self.timewindowMethod.cleanWidget()
                serial = self.serialNumberSelected[self.ui.buttongroup.checkedId()]
                
                query = """SELECT time
                FROM dialy_inspection
                WHERE 
                ins= %s"""
                cursor.execute(query,(str(serial),))
                nextrow=0
                for i in cursor.fetchall():
                    for g in i:                    
                        self.timeSelected.append(g)     
                        self.timewindowMethod.checkList[nextrow].show()
                        self.timewindowMethod.textList[nextrow].show()
                        self.timewindowMethod.textList[nextrow].setText(str(g))
                    nextrow+=1
                self.window3.show()
                # print(self.timeSelected)
                # self.ui = equipmentMethod(self.window)

            if self.ui.chooseReport.currentIndex() == 1:
                self.scrappingWindow = scrappingnMethod(self.window2)
                serial = self.serialNumberSelected[self.ui.buttongroup.checkedId()]
                query = """SELECT `Date`, `Requested By`, `Department`, `Reasons for Disposition`, `Serial Number`
                FROM
                `scrapping`
                WHERE `Serial Number` =%s"""
                cursor.execute(query,(str(serial),))
                for i in cursor.fetchall():
                    nextrow=0
                    self.window2.show()
                    for g in i:
                        if nextrow == 0:
                            self.scrappingWindow.scrappingParameters[nextrow].setDate(g)
                        else:
                            self.scrappingWindow.scrappingParameters[nextrow].setText(str(g))
                        nextrow+=1

            if self.ui.chooseReport.currentIndex() == 2:
                serial = self.serialNumberSelected[self.ui.buttongroup.checkedId()]
                self.reportInstallationWindow = installationMethod(self.window2)
                self.window2.show()
                self.reportInstallationWindow.tab1.setEnabled(False)

                query = """SELECT  `serialNumber`,`name`, `model`, `brand`, `manufacturer`,
                            `riskClassification`, `description`, `department`
                FROM `equipment`
                WHERE 
                `serialNumber`= %s"""
                
                # print(serial)
                cursor.execute(query,(str(serial),))
                for i in cursor.fetchall():
                    nextrow=0
                    for g in i:
                        if nextrow == 7:
                            self.reportInstallationWindow.itemParameters[nextrow].setCurrentIndex(g)
                        else:
                            self.reportInstallationWindow.itemParameters[nextrow].setText(str(g))
                        nextrow+=1

                query = """SELECT supplier, supplierAddress, supplierContactPerson, supplierContactNO,
                                        authorised, authorisedAddress, authorisedContactPerson, authorisedContactNO,
                                        localPurchaseOrderNO, purchaseDate, warrantyStartDate, purchasePrice, deliveryNO, warrantyEndDate
                FROM purchase
                WHERE 
                EqSN= %s"""
                cursor.execute(query,(str(serial),))
                next = 0      
                for i in cursor.fetchall():
                    for g in i:
                        if g != None:
                            if type(g) == int or type(g) == str:
                                self.reportInstallationWindow.purchaseParameters[next].setText(str(g))  
                            else:
                                self.reportInstallationWindow.purchaseParameters[next].setDate(g)          
                            next +=1

                query = """SELECT `batchSize`, `sampleSize`, `defectsCount`, `buttongroup1`, `buttongroup2`,
                            `buttongroup3`, `buttongroup4`, `buttongroup5`, `buttongroup6`, `buttongroup7`,
                            `problem`, `remarks`, `suggestion`
                FROM `physical inspection`
                WHERE 
                EqSN= %s"""
                cursor.execute(query,(str(serial),))
                nextrow = 0      
                for i in cursor.fetchall():
                    for g in i:
                        if g != None:
                            if nextrow <3:
                                self.reportInstallationWindow.physicalInspectionParameters[nextrow].setText(str(g))  
                            elif nextrow <10:
                                if g !=-1:
                                    self.reportInstallationWindow.physicalInspectionParameters[nextrow].button(g).setChecked(True)
                            else:
                                self.reportInstallationWindow.physicalInspectionParameters[nextrow].setText(str(g))
                            nextrow +=1

                query = """SELECT `inspectoinOrNot`, `acceptanceOrNot`, `acceptedWithReservation`, `remark`, `supplierName`,
                                `supplierDesignation`, `supplierDate`, `hospitalRepresentativeName`, `hospitalRepresentativeDesignation`,
                                `hospitalRepresentativeDate`
                FROM `conclusion`
                WHERE 
                EqSN= %s"""
                cursor.execute(query,(str(serial),))
                nextrow = 0      
                for i in cursor.fetchall():
                    for g in i:
                        if g != None :
                            if nextrow <2:
                                self.reportInstallationWindow.conclusionParameters[nextrow].button(g).setChecked(True)
                            elif nextrow ==2:
                                if g != -1:
                                    self.reportInstallationWindow.conclusionParameters[nextrow].setChecked(g)
                            else:
                                if type(g) == int or type(g) == str:
                                    self.reportInstallationWindow.conclusionParameters[nextrow].setText(str(g))
                                else:
                                    self.reportInstallationWindow.conclusionParameters[nextrow].setDate(g)
                            nextrow +=1

            

            
                    
            

    def open(self):
        self.ui = installationMethod(self.window) 
        self.window.show()
        MainWindow.hide()
        
        
        
        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ApplicationWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())