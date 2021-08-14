

from timewindow import *

import mysql.connector



class timewindowMethod(timewindow):
    def __init__ (self, MainWindow):
        super(timewindowMethod, self).setupUi(MainWindow)
        self.textList = [self.label1_1,self.label1_2,self.label1_3,self.label1_4,self.label1_5,self.label1_6,
                        self.label1_7,self.label1_8,self.label1_9,self.label1_10,self.label1_11,self.label1_12,
                        self.label1_13,self.label1_14,self.label1_15,self.label1_16,self.label1_17]

        self.checkList = [self.check1_1,self.check1_2,self.check1_3,self.check1_4,self.check1_5,self.check1_6,self.check1_7,
                        self.check1_8,self.check1_9,self.check1_10,self.check1_11,self.check1_12,self.check1_13,self.check1_14,
                        self.check1_15,self.check1_16,self.check1_17] 
        self.buttongroup = QtWidgets.QButtonGroup()
        for i in range(len(self.checkList)):
            self.buttongroup.addButton(self.checkList[i],i)
        self.buttongroup.setExclusive(True)
        self.cleanWidget()

    def cleanWidget(self):
        for i in range(len(self.checkList)):
            self.checkList[i].hide()
            self.textList[i].hide()