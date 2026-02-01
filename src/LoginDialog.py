from PySide6.QtWidgets import QDialog
from ui.LoginDialog_ui import Ui_loginDialog
from utils.mysqldb import MySQLDB

class LoginDialog(QDialog, Ui_loginDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.userid = ''
        self.password = ''
        
    def onLoginButtonClicked(self):
        self.userid = self.accountText.text()
        self.password = self.passwordText.text()
        
        if self.userid == '' or self.password == '':
            self.messageLabel.setText('请输入用户名和密码')
            return
        
        if MySQLDB.checkLogin(self.userid, self.password):
            self.messageLabel.setText('')
            self.accept()
        else:
            self.messageLabel.setText('登录失败,请检查用户名和密码')
      
    def onCancelButtonClicked(self):
        self.reject()
    