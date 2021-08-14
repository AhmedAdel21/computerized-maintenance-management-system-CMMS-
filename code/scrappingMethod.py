

from scrapping import *

import mysql.connector



class scrappingnMethod(scrapping):
    def __init__ (self, MainWindow):
        super(scrappingnMethod, self).setupUi(MainWindow)
        self.scrappingParameters = [self.scrappingDate,self.requestedBy,self.department,self.reasonsForDisposition,self.serialNumber]
        self.scrappingSave.clicked.connect(self.scrappingDateEnter)


    def scrappingDateEnter(self):
        self.scrappingDateDetails = [self.scrappingDate.text(),self.requestedBy.text(),self.department.text(),self.reasonsForDisposition.toPlainText(),self.serialNumber.text()]

        connect = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="mysql",
                            db= "Hospital"
                            )
        cursor = connect.cursor()
        query = """INSERT INTO `scrapping`(`Date`, `Requested By`, `Department`, `Reasons for Disposition`, `Serial Number`)
         VALUES
         (%s,%s,%s,%s,%s)"""
        cursor.execute(query,self.scrappingDateDetails)
        connect.commit()

