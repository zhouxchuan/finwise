import json
from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt
from ui.FundBasicInfoDialog_ui import Ui_FundBasicInfoDialog


class FundBasicInfoDialog(QDialog, Ui_FundBasicInfoDialog):
    def __init__(self, parent=None, params={'code': None, 'name': None, 'basic_info': None}):
        super(FundBasicInfoDialog, self).__init__(parent)
        self.setupUi(self)
        self.code = params['code']
        self.name = params['name']
        self.basic_info = params['basic_info']

        basic_info = json.loads(self.basic_info)

        for key, value in basic_info.items():
            if value is None:
                value = ''
            self.plainTextEdit.appendPlainText(f'【{key}】')
            self.plainTextEdit.appendPlainText(f'    {value}')
            self.plainTextEdit.appendPlainText('')

    def showEvent(self, event):
        self.plainTextEdit.verticalScrollBar().setSliderPosition(0)
        return super().showEvent(event)
