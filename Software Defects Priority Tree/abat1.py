import sys
import os
from abat import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.bgdtls)
     self.ui.pushButton_2.clicked.connect(self.igtta)
     self.ui.pushButton_3.clicked.connect(self.tdtls)
     self.ui.pushButton_5.clicked.connect(self.igfta)
     self.ui.pushButton_6.clicked.connect(self.ptdot)
     self.ui.pushButton_7.clicked.connect(self.ptpdf)

  def bgdtls(self):
    os.system("python bugdtls1.py")       

  def igtta(self):
    os.system("python anal2.py")

  def tdtls(self):
    os.system("python tester1.py")

  def igfta(self):
    os.system("python anal4.py")

  def ptdot(self):
    os.system("python anal3.py")
	
  def ptpdf(self):
    os.system("python anal5.py")
     
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
