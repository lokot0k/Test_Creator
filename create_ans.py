# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_ans.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Question(object):
    def setupUi(self, Question):
        Question.setObjectName("Question")
        Question.resize(642, 526)
        self.verticalLayoutWidget = QtWidgets.QWidget(Question)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 524))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.quest_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.quest_text.setFont(font)
        self.quest_text.setObjectName("quest_text")
        self.verticalLayout.addWidget(self.quest_text)
        self.quest_value = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.quest_value.setFont(font)
        self.quest_value.setObjectName("quest_value")
        self.verticalLayout.addWidget(self.quest_value)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ans_value = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ans_value.setFont(font)
        self.ans_value.setObjectName("ans_value")
        self.verticalLayout.addWidget(self.ans_value)
        self.next_push = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.next_push.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.next_push.setFont(font)
        self.next_push.setObjectName("next_push")
        self.verticalLayout.addWidget(self.next_push)

        self.retranslateUi(Question)
        QtCore.QMetaObject.connectSlotsByName(Question)

    def retranslateUi(self, Question):
        _translate = QtCore.QCoreApplication.translate
        Question.setWindowTitle(_translate("Question", "Form"))
        self.quest_text.setText(_translate("Question", "Введите вопрос: "))
        self.quest_value.setPlainText(_translate("Question", ""))
        self.label.setText(_translate("Question", "Введите ответ: "))
        self.ans_value.setPlainText(_translate("Question", ""))
        self.next_push.setText(_translate("Question", "Следующий вопрос"))