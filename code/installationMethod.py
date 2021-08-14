from installation import *
import mysql.connector





class installationMethod(installation):
    def __init__ (self, MainWindow):
        super(installationMethod, self).setupUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        
        # dd = QtCore.QDate(1992, 6, 12)
        # self.warrantyStartDate.setDate(dd)
        # print(type(dd))
        # self.warrantyStartDate.setDate(QtCore.QDate(1992, 6, 12))
        # self.warrantyEndDate.set
        # self.supplierContactNO.setText('15')
        

        # configration for tab 2
        # make list of all checkbox
        self.tab2CheckboxList=[self.check1_1,self.check1_2,self.check1_3, self.check2_1,self.check2_2,self.check2_3,self.check3_1,self.check3_2,self.check3_3,
                            self.check4_1,self.check4_2,self.check4_3,self.check5_1,self.check5_2,self.check5_3,self.check6_1,self.check6_2,self.check6_3,
                            self.check7_1,self.check7_2,self.check7_3]
        # make list of buttongroups
        self.buttongroup1,self.buttongroup2,self.buttongroup3,self.buttongroup4,self.buttongroup5,self.buttongroup6,self.buttongroup7 =QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup()
       
        self.tab2ButtongroupList = [self.buttongroup1,self.buttongroup2,self.buttongroup3,self.buttongroup4,self.buttongroup5,self.buttongroup6,self.buttongroup7]
        # make all element in tab2ButtongroupList as QButtonGroup and set it to be exclusive
        for i in range(len(self.tab2ButtongroupList)):
            self.tab2ButtongroupList[i].setExclusive(True)  
        self.nextGroup =0       # an addition element
        # attach the row check box to its buttongroup 
        for i in range(len(self.tab2ButtongroupList)):
            for g in range(3):
                self.tab2ButtongroupList[i].addButton(self.tab2CheckboxList[g+self.nextGroup],g)
            self.nextGroup +=3
        
        
          # configration for tab4

        # make list of all checkbox
        self.tab3CheckboxList=[self.inspectionDone,self.inspectionNOTDone,self.accepted,self.notAccepted]
        # make list of buttongroups
        self.tab3buttongroup1,self.tab3buttongroup2 =QtWidgets.QButtonGroup(),QtWidgets.QButtonGroup()
        self.tab3ButtongroupList = [self.tab3buttongroup1,self.tab3buttongroup2]
        # make all element in tab3ButtongroupList as QButtonGroup and set it to be exclusive
        for i in range(len(self.tab3ButtongroupList)):
            self.tab3ButtongroupList[i].setExclusive(True)  
        self.nextGroup =0       # an addition element
        # attach the row check box to its buttongroup 
        for i in range(len(self.tab3ButtongroupList)):
            for g in range(2):
                self.tab3ButtongroupList[i].addButton(self.tab3CheckboxList[g+self.nextGroup],g)
            self.nextGroup +=2

        #buttons
        self.tab0Next.clicked.connect(self.tab1form)
        self.tab1Next.clicked.connect(self.tab2form)
        self.tab2Next.clicked.connect(self.tab3form)
        self.tab1Back.clicked.connect(self.tab0form)
        self.tab2Back.clicked.connect(self.tab1form)
        self.tab3Back.clicked.connect(self.tab2form)
        self.tab4Save.clicked.connect(self.save)

        # itemes iQoens
        self.itemParameters = [self.serialNumber ,self.name ,self.model ,self.brand ,self.manufacturer ,
                                self.riskClassification ,self.description ,self.department]

        self.purchaseParameters = [self.supplier,self.supplierAddress,self.supplierContactPerson,self.supplierContactNO,
                                    self.authorised,self.authorisedAddress,self.authorisedContactPerson,self.authorisedContactNO,
                                    self.localPurchaseOrderNO,self.purchaseDate,self.warrantyStartDate,self.purchasePrice,self.deliveryNO,self.warrantyEndDate]

        self.physicalInspectionParameters = [self.batchSize ,self.sampleSize ,self.defectsCount ,self.buttongroup1 ,self.buttongroup2 ,self.buttongroup3 ,self.buttongroup4 ,
                                               self.buttongroup5 ,self.buttongroup6 ,self.buttongroup7 ,self.problem,self.remarks,self.suggestion,self.serialNumber ]

                                               
        self.conclusionParameters = [self.tab3buttongroup1,self.tab3buttongroup2,self.acceptedWithReservation,self.remark ,
                                    self.supplierName ,self.supplierDesignation ,self.supplierDate ,self.hospitalRepresentativeName ,
                                    self.hospitalRepresentativeDesignation ,self.hospitalRepresentativeDate ,self.serialNumber ]

    def tab0form (self):
        self.tabs.setCurrentIndex(0)
        
    def tab1form (self):
        print(self.department.currentIndex())
        
        #saving eq data
        self.itemDetails = [self.serialNumber.text(),self.name.text(),self.model.text(),self.brand.text(),self.manufacturer.text(),
                            self.riskClassification.text(),self.description.text(),self.department.currentIndex()]





        #set configration of tab1
        self.tabs.setCurrentIndex(1)
        self.tabs.setTabEnabled(1,True)

        self.localPurchaseOrderNO.setValidator(QtGui.QDoubleValidator())
        self.supplierContactNO.setValidator(QtGui.QDoubleValidator())
        self.authorisedContactNO.setValidator(QtGui.QDoubleValidator())
        self.purchasePrice.setValidator(QtGui.QDoubleValidator())
        self.deliveryNO.setValidator(QtGui.QDoubleValidator())
        
        

    def tab2form (self):
        self.tabs.setCurrentIndex(2)
        self.tabs.setTabEnabled(2,True)
        
        #saving tab1 data
        self.purchaseDetailsDataEnter = [self.supplier.text(),self.supplierAddress.text(),self.supplierContactPerson.text(),self.supplierContactNO.text(),
                                    self.authorised.text(),self.authorisedAddress.text(),self.authorisedContactPerson.text(),self.authorisedContactNO.text(),
                                    self.localPurchaseOrderNO.text(),self.purchaseDate.text(),self.warrantyStartDate.text(),self.purchasePrice.text(),self.deliveryNO.text(),self.warrantyEndDate.text(),self.serialNumber.text()]

        

        self.batchSize.setValidator(QtGui.QDoubleValidator())
        self.sampleSize.setValidator(QtGui.QDoubleValidator())
        self.defectsCount.setValidator(QtGui.QDoubleValidator())
        
        
        
        
        
        
        
    
    def tab3form (self):
        self.tabs.setCurrentIndex(3)
        self.tabs.setTabEnabled(3,True)
        self.acceptedWithReservation.setChecked(0)
        # saveing tab2 data 
        self.physicalInspectionDataEnter = [self.batchSize.text(),self.sampleSize.text(),self.defectsCount.text(),self.buttongroup1.checkedId(),self.buttongroup2.checkedId(),self.buttongroup3.checkedId(),self.buttongroup4.checkedId(),
                                self.buttongroup5.checkedId(),self.buttongroup6.checkedId(),self.buttongroup7.checkedId(),self.problem.toPlainText(),self.remarks.toPlainText(),self.suggestion.toPlainText(),self.serialNumber.text()]
        


    def save(self):
        # save the eq data
        connect = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="mysql",
                            db= "Hospital"
                            )
        cursor = connect.cursor()
        query = """INSERT INTO equipment( serialNumber, name , model, brand ,manufacturer,
                        riskClassification ,  description ,  department)
         VALUES
         (%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,self.itemDetails)
        connect.commit()
        #############

        #seve the purchase data 
        query = """INSERT INTO purchase(supplier, supplierAddress, supplierContactPerson, supplierContactNO,
                                     authorised, authorisedAddress, authorisedContactPerson, authorisedContactNO,
                                     localPurchaseOrderNO, purchaseDate, warrantyStartDate, purchasePrice, deliveryNO, warrantyEndDate,EqSN)
         VALUES
         (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,self.purchaseDetailsDataEnter)
        connect.commit()
        ############

        #save physical inspection data 
        query = """INSERT INTO `physical inspection`(  batchSize ,  sampleSize ,  defectsCount ,  buttongroup1 ,  buttongroup2 ,  buttongroup3 ,  buttongroup4 ,  buttongroup5 ,
                                                      buttongroup6 ,  buttongroup7 ,  problem ,  remarks ,  suggestion ,  EqSN)
         VALUES
         (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,self.physicalInspectionDataEnter)
        connect.commit()
        ############

        #save conclusion data
        self.conclusionDataEnter = [self.buttongroup1.checkedId(),self.buttongroup2.checkedId(),self.acceptedWithReservation.isChecked(),self.remark.text(),
                                    self.supplierName.text(),self.supplierDesignation.text(),self.supplierDate.text(),self.hospitalRepresentativeName.text(),
                                    self.hospitalRepresentativeDesignation.text(),self.hospitalRepresentativeDate.text(),self.serialNumber.text()]

        query = """INSERT INTO `conclusion`(`inspectoinOrNot`, `acceptanceOrNot`, `acceptedWithReservation`, `remark`, `supplierName`,
                                             `supplierDesignation`, `supplierDate`, `hospitalRepresentativeName`, `hospitalRepresentativeDesignation`,
                                              `hospitalRepresentativeDate`, `EqSN`)
         VALUES
         (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,self.conclusionDataEnter)
        connect.commit()

        
        cursor.close()
        connect.close()


    def dataBack(self):
        # print(self.warrantyStartDate.text())
        connect = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="mysql",
                            db= "Hospital"
                            )
        cursor = connect.cursor()
        query = """SELECT supplier, supplierAddress, supplierContactPerson, supplierContactNO,
                                     authorised, authorisedAddress, authorisedContactPerson, authorisedContactNO,
                                     localPurchaseOrderNO, purchaseDate, warrantyStartDate, purchasePrice, deliveryNO, warrantyEndDate
        FROM purchase
        WHERE 
        inst= %s"""
        cursor.execute(query,(self.lineEnter.text(),))
        next = 0      
        for i in cursor.fetchall():
            for g in i:
                print(type(g))
                print(g)
                if g != None:
                    if type(g) == int or type(g) == str:
                        self.purchaseDetailsDataBack[next].setText(str(g))  
                    else:
                        self.purchaseDetailsDataBack[next].setDate(g)          
                    next +=1
                    
                    



       