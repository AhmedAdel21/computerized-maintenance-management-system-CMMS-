

from equipment import *
import mysql.connector
from dialyInspectionMethod import dialyInspectionMethod


class equipmentMethod(equipment):
    def __init__ (self, MainWindow):
        super(equipmentMethod, self).setupUi(MainWindow)
        self.buttongroup = QtWidgets.QButtonGroup() # make a buttongroup to contain all checkboxes
        
        # list of all checkboxes 
        self.reportCheckbox = [self.checkBox_1,self.checkBox_2,self.checkBox_3, self.checkBox_4,self.checkBox_5,
                                self.checkBox_6,self.checkBox_7,self.checkBox_8,self.checkBox_9,self.checkBox_10,
                                self.checkBox_11,self.checkBox_12,self.checkBox_13, self.checkBox_14,self.checkBox_15,
                                self.checkBox_16,self.checkBox_17,self.checkBox_18,self.checkBox_19,self.checkBox_20,
                                self.checkBox_21,self.checkBox_22,self.checkBox_23, self.checkBox_24,self.checkBox_25,
                                self.checkBox_26,self.checkBox_27,self.checkBox_28,self.checkBox_29,self.checkBox_30]
        
        # list of all lables
        self.reportLables = [self.label_1,self.label_2,self.label_3,self.label_4,self.label_5,
                            self.label_6,self.label_7,self.label_8,self.label_9,self.label_10,
                            self.label_11,self.label_12,self.label_13,self.label_14,self.label_15,
                            self.label_16,self.label_17,self.label_18,self.label_19,self.label_20,
                            self.label_21,self.label_22,self.label_23,self.label_24,self.label_25,
                            self.label_26,self.label_27,self.label_28,self.label_29,self.label_30]

        # attach all checkbox to the buttongroup tha we were created                   
        for i in range(len(self.reportCheckbox)):
            self.buttongroup.addButton(self.reportCheckbox[i],i)
        self.buttongroup.setExclusive(True)

        self.hideAllWidgets()

    def hideAllWidgets(self):
        # hide all labels and checkboxes
        for i in range(len(self.reportCheckbox)):
            self.reportCheckbox[i].hide()
            self.reportLables[i].hide()








