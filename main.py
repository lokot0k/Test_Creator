from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from main_ui import Ui_MainWindow
from dialog_test import Ui_Dialog
from warning_dialog import Ui_WarninDialog
from create_ans import Ui_Question
from acc_dialog import Ui_Form
from test_parser import ParserCfg
import sys
import csv


class AccCfg:
    def __init__(self):
        self.name = None
        self.path = None
        self.row = []
        self.count = None
        self.quests = None
        self.answs = None
        self.result = None


accInf = AccCfg()


class AccSett(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(600, 400)
        self.test_choose.clicked.connect(self.reciever)
        self.test_start.clicked.connect(self.start)

    def reciever(self):
        accInf.path = QFileDialog.getOpenFileName(self, 'Выберите тест: ', '')[0]
        self.path_label.setText('Выбранный файл: ' + accInf.path)

    def start(self):
        try:
            accInf.name = self.lineEdit.text()
            if '.tstx' not in accInf.path:
                raise WarningException
            if accInf.name == '':
                raise WarningException
            self.close()
            parser = ParserCfg(accInf.path)
            accInf.quests, accInf.answs = parser.parse()
        except WarningException as e:
            self.e = e
            self.e.warning.show()


class WarningException(Exception):
    def __init__(self):
        self.warning = WarningDialog()
        self.warning.setFixedSize(600, 350)


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
        self.writer = None
        self.curr = 0


inform = TestInfoStruct()


class QuestCreator(QWidget, Ui_Question):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.next_push.clicked.connect(self.reciever)
        inform.curr += 1
        self.setWindowTitle("Вопрос №" + str(inform.curr))
        if inform.curr == inform.count:
            self.next_push.setText('Завершить')

    def reciever(self):
        inform.f.write(
            str(self.curr) + '.' + self.quest_value.toPlainText() +
            " @@@" + self.ans_value.toPlainText() + "\n-----\n")
        if inform.curr < inform.count:
            self.close()
            self.__init__()
        else:
            self.close()
            inform.__init__()


class DialogTest(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.reciever)
        self.setFixedSize(650, 300)
        self.quest = None

    def accept(self):
        inform.name = self.name_input.text()
        inform.count = int(self.spinBox.text())
        try:
            if '.' in inform.name:
                raise WarningException
            if inform.count == 0:
                raise WarningException
            inform.f = open(inform.path + '/' + inform.name + '.tstx', mode='w', encoding='utf-8')
            inform.csv_doc = open(inform.path + '/' + inform.name + '.csv', mode='w', encoding='utf-8')
            inform.writer = csv.writer(inform.csv_doc, delimiter=';', quotechar='"')
            a = ['Name']
            for i in range(inform.count):
                a.append(str(i + 1))
            a.append('Result')
            inform.writer.writerow(a)
            inform.csv_doc.close()

            self.close()
            self.quest = QuestCreator()
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
        self.close()
        self.acc_sett = AccSett()
        self.acc_sett.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
