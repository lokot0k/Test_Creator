from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from main_ui import Ui_MainWindow
from dialog_test import Ui_Dialog
import sys


class TestInfoStruct:
    def __init__(self):
        self.name = None
        self.count = None
        self.path = None


inform = TestInfoStruct()


class DialogTest(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.reciever)

    def accept(self):
        inform.name = self.name_input.text()
        inform.count = int(self.spinBox.text())

    def reject(self):
        self.close()

    def reciever(self):
        self.path = QFileDialog.getExistingDirectory(self, 'Выберите папку: ', '')
        self.choose.setText('Директория для сохранения файлов: ' + self.path)


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
        print('pass')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
