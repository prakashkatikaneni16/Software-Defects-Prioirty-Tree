import sys
from bugdtls import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
con = sqlite3.connect('abat1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        bid = str(self.ui.lineEdit_3.text())
        descr = str(self.ui.lineEdit_4.text())
        seve = str(self.ui.lineEdit_5.text())
        fncaff = str(self.ui.lineEdit_6.text())
        workf = str(self.ui.lineEdit.text())	
        endcs = str(self.ui.lineEdit_2.text())
        btype = str(self.ui.lineEdit_7.text())
        cur.execute('INSERT INTO bugdtls VALUES(?,?,?,?,?,?,?)',(bid,btype,descr,seve,fncaff,workf,endcs))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


