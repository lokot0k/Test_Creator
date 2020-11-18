from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CreateTest.clicked.connect(self.create_test)
        self.PassTest.clicked.connect(self.pass_test)

    def create_test(self):
        print('create')

    def pass_test(self):
        print('pass')
