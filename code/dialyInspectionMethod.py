from dialyInspection import dialyInspection
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets





class dialyInspectionMethod(dialyInspection):
    def __init__ (self, MainWindow):
        super(dialyInspectionMethod, self).setupUi(MainWindow)
        # make list of all checkbox
        self.serial = ''
        self.checkboxList=[self.check1_1,self.check1_2,self.check1_3, self.check2_1,self.check2_2,self.check2_3,self.check3_1,self.check3_2,self.check3_3,
                            self.check4_1,self.check4_2,self.check4_3,self.check5_1,self.check5_2,self.check5_3,self.check6_1,self.check6_2,self.check6_3,
                            self.check7_1,self.check7_2,self.check7_3,self.check8_1,self.check8_2,self.check8_3,self.check9_1,self.check9_2,self.check9_3,
                            self.check10_1,self.check10_2,self.check10_3,self.check11_1,self.check11_2,self.check11_3,self.check12_1,self.check12_2,self.check12_3,
                            self.check13_1,self.check13_2,self.check13_3,self.check14_1,self.check14_2,self.check14_3,self.check15_1,self.check15_2,self.check15_3,
                            self.check16_1,self.check16_2,self.check16_3,self.check17_1,self.check17_2,self.check17_3,self.check18_1,self.check18_2,self.check18_3,
                            self.check19_1,self.check19_2,self.check19_3]
        # make list of buttongroups
        self.buttongroup1,self.buttongroup2,self.buttongroup3,self.buttongroup4,self.buttongroup5,self.buttongroup6,self.buttongroup7,self.buttongroup8,self.buttongroup9 =QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup()
        self.buttongroup10,self.buttongroup11,self.buttongroup12,self.buttongroup13,self.buttongroup14,self.buttongroup15,self.buttongroup16,self.buttongroup17,self.buttongroup18,self.buttongroup19 =QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup()
        self.buttongroupList = [self.buttongroup1,self.buttongroup2,self.buttongroup3,self.buttongroup4,self.buttongroup5,self.buttongroup6,self.buttongroup7,self.buttongroup8,self.buttongroup9,
                                self.buttongroup10,self.buttongroup11,self.buttongroup12,self.buttongroup13,self.buttongroup14,self.buttongroup15,self.buttongroup16,self.buttongroup17,self.buttongroup18,self.buttongroup19]
        # make all element in buttongroupList as QButtonGroup and set it to be exclusive
        for i in range(len(self.buttongroupList)):
            self.buttongroupList[i].setExclusive(True) 
        # print(self.buttongroupList[1]) 
        self.nextGroup =0       # an addition element
        # attach the row check box to its buttongroup 
        for i in range(len(self.buttongroupList)):
            for g in range(3):
                self.buttongroupList[i].addButton(self.checkboxList[g+self.nextGroup],g)
            self.nextGroup +=3
        self.save.clicked.connect(self.enterData)
        # self.report.clicked.connect(self.retrive)
                                


    def enterData(self):
        self.buttonClickedList=[self.buttongroup1.checkedId(),self.buttongroup2.checkedId(),self.buttongroup3.checkedId(),self.buttongroup4.checkedId(),self.buttongroup5.checkedId(),self.buttongroup6.checkedId(),self.buttongroup7.checkedId(),self.buttongroup8.checkedId(),self.buttongroup9.checkedId(),
                                self.buttongroup10.checkedId(),self.buttongroup11.checkedId(),self.buttongroup12.checkedId(),self.buttongroup13.checkedId(),self.buttongroup14.checkedId(),self.buttongroup15.checkedId(),self.buttongroup16.checkedId(),
                                self.buttongroup17.checkedId(),self.buttongroup18.checkedId(),self.buttongroup19.checkedId(),str(self.serial)]

        print(self.buttonClickedList)
        connect = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="mysql",
                            db= "Hospital"
                            )
        cursor = connect.cursor()
        query = """INSERT INTO dialy_inspection (row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15,row16,row17,row18,row19,ins)
         VALUES
         (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,self.buttonClickedList)
        connect.commit()


        






