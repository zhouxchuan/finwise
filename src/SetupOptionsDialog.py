from PySide6.QtWidgets import QDialog
from ui.SetupOptionsDialog_ui import Ui_SetupOptionsDialog
from utils.mysqldb import MySQLDatabase as MySQLDB
import json


class SetupOptionsDialog(QDialog, Ui_SetupOptionsDialog):
    '''
     设置基金账户项类
    '''

    def __init__(self, parent=None):
        super(SetupOptionsDialog, self).__init__(parent)
        self.setupUi(self)

        self.config = {}

        try:
            with open("finwise-config.json") as json_file:
                self.config = json.load(json_file)
        except:
            self.msgLabel.setText('读取配置文件失败')
            return

        config_database = self.config.get('database', None)
        if config_database:
            self.hostLineEdit.setText(config_database.get('host', ''))
            self.portLineEdit.setText(str(config_database.get('port', 3306)))
            self.databaseLineEdit.setText(config_database.get('database', ''))
            self.userLineEdit.setText(config_database.get('user', ''))
            self.passwordLineEdit.setText(config_database.get('password', ''))

    def onTestButtonClicked(self):
        config = {
            'host': self.hostLineEdit.text(),
            'port': int(self.portLineEdit.text()),
            'database': self.databaseLineEdit.text(),
            'user': self.userLineEdit.text(),
            'password': self.passwordLineEdit.text()
        }
        res = MySQLDB.initialize(config)
        if res:
            self.msgLabel.setText('数据库连接成功')
        else:
            self.msgLabel.setText('数据库连接失败')

    def onOkButtonClicked(self):
        self.config['database'] = {
            'host': self.hostLineEdit.text(),
            'port': int(self.portLineEdit.text()),
            'database': self.databaseLineEdit.text(),
            'user': self.userLineEdit.text(),
            'password': self.passwordLineEdit.text()
        }

        with open("finwise-config.json", "w") as json_file:
            json.dump(self.config, json_file, indent=4)

        super().accept()
