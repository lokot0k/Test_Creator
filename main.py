from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from main_ui import Ui_MainWindow
from dialog_test import Ui_Dialog
from warning_dialog import Ui_WarninDialog
import sys


class WarningException(Exception):
    def __init__(self):
        self.warning = WarningDialog()


class WarningDialog(QWidget, Ui_WarninDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.reciever)

    def reciever(self):
        self.close()


class TestInfoStruct:
    def __init__(self):
        self.name = None
        self.count = None
        self.path = None
        self.f = None


inform = TestInfoStruct()


class DialogTest(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.reciever)
        self.setFixedSize(650, 300)

    def accept(self):
        inform.name = self.name_input.text()
        inform.count = int(self.spinBox.text())
        try:
            if '.' in inform.name:
                raise WarningException
            if inform.count == 0:
                raise WarningException
            inform.f = open(inform.path + '/' + inform.name + '.tstx', mode='w', encoding='utf-8')
            self.close()
        except WarningException as e:
            self.e = e
            self.e.warning.show()

    def reject(self):
        global inform
        inform.__init__()
        self.close()

    def reciever(self):
        inform.path = QFileDialog.getExistingDirectory(self, 'Выберите папку: ', '')
        self.choose.setText('Директория для сохранения файлов: \n' + inform.path)


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CreateTest.clicked.connect(self.create_test)
        self.PassTest.clicked.connect(self.pass_test)
        self.setFixedSize(800, 500)

    def create_test(self):
        self.test_dialog = DialogTest()
        self.test_dialog.show()

    def pass_test(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
