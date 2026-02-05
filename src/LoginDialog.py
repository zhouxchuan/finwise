from PySide6.QtWidgets import QDialog
from ui.LoginDialog_ui import Ui_loginDialog
from utils.mysqldb import MySQLDatabase as MySQLDB
import json


class LoginDialog(QDialog, Ui_loginDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)

        self.userid = 'admin'
        self.password = '123'

        self.accountText.setText(self.userid)
        self.passwordText.setText(self.password)

    def onLoginButtonClicked(self):

        try:
            with open("finwise-config.json") as json_file:
                config = json.load(json_file)
        except FileNotFoundError as e:
            self.msgLabel.setText(f'读取配置文件失败:{e}')
            return
        if 'database' not in config:
            self.msgLabel.setText('配置文件错误，请检查数据库配置')
            return

        config_database = config.get('database', None)

        res = MySQLDB.initialize(config_database)
        if not res:
            self.messageLabel.setText('数据库连接失败')
            return

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
