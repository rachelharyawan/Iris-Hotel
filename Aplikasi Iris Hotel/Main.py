from Login_View import Ui_Login
from PyQt4 import QtCore, QtGui
import sys

class Main:
    def run(self):
        app = QtGui.QApplication(sys.argv)
        ui = Ui_Login()
        sys.exit(app.exec_())

if __name__ == "__main__":
    startapp = Main()
    startapp.run()
