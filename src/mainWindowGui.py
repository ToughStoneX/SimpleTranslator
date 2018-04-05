# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_mainWindowGui import Ui_MainWindow
from googleTranslator import TranslateByGoogle

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_textEdit_textChanged(self):
        """
        Slot documentation goes here.
        """
#         print(u'textEdit edited')
        str = self.textEdit.toPlainText()
        str = str.replace('\n',  ' ')
        translated_text = TranslateByGoogle(unicode(str))
        self.textEdit_2.setPlainText(translated_text)
        # print(str)
    
    @pyqtSignature("")
    def on_textEdit_2_textChanged(self):
        """
        Slot documentation goes here.
        """
#         print(u'textEdit_2 edited')

#         str = self.textEdit_2.toPlainText()
#         print(unicode(str))
        pass
        
        
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     ui = MainWindow()
#     ui.show()
#     sys.exit(app.exec_())
