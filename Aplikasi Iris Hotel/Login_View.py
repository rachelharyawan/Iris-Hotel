from PyQt4 import QtCore, QtGui
from AdminPage_View import Ui_AdminPage
from ReceptionistPage_View import Ui_ReceptionistPage
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def __init__(self):
        Login = QtGui.QMainWindow()
        self.setupUi(Login)
        Login.show()
        
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(705, 576)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Login.setPalette(palette)
        self.centralwidget = QtGui.QWidget(Login)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.welcome = QtGui.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(250, 0, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.welcome.setFont(font)
        self.welcome.setObjectName(_fromUtf8("welcome"))
        self.irishotel = QtGui.QLabel(self.centralwidget)
        self.irishotel.setGeometry(QtCore.QRect(270, 50, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.irishotel.setFont(font)
        self.irishotel.setObjectName(_fromUtf8("irishotel"))
        self.username = QtGui.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(220, 190, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username.setFont(font)
        self.username.setObjectName(_fromUtf8("username"))
        self.loginbutton = QtGui.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(290, 460, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.loginbutton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginbutton.setFont(font)
        self.loginbutton.setObjectName(_fromUtf8("loginbutton"))
        self.password = QtGui.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(220, 280, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setObjectName(_fromUtf8("password"))
        self.usernameinput = QtGui.QLineEdit(self.centralwidget)
        self.usernameinput.setGeometry(QtCore.QRect(210, 220, 271, 31))
        self.usernameinput.setObjectName(_fromUtf8("usernameinput"))
        self.passinput = QtGui.QLineEdit(self.centralwidget)
        self.passinput.setGeometry(QtCore.QRect(210, 310, 271, 31))
        self.passinput.setObjectName(_fromUtf8("passinput"))
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Login.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Login)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "MainWindow", None))
        self.welcome.setText(_translate("Login", "Welcome to", None))
        self.irishotel.setText(_translate("Login", "Iris Hotel", None))
        self.username.setText(_translate("Login", "Username", None))
        self.loginbutton.setText(_translate("Login", "Login", None))
        self.loginbutton.clicked.connect(lambda: self.logincheck(Login))
        self.password.setText(_translate("Login", "Password", None))

    def logincheck(self, Login):
        username = self.usernameinput.text()
        password = self.passinput.text()
        if username == "admin" and password == "admin":
            self.loginadmin = Ui_AdminPage()
            Login.close()
        elif username == "receptionist" and password == "receptionist":
            self.loginreceptionist = Ui_ReceptionistPage()
            Login.close()
        else:
            print("Login gagal")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Login()
    sys.exit(app.exec_())
