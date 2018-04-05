# -*- coding: utf-8 -*-

from Ui_mainWindowGui import Ui_MainWindow
from mainWindowGui import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
