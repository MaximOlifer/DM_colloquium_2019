# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Q_modules_Window_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QModulesWindow1(object):
    def setupUi(self, QModulesWindow1):
        QModulesWindow1.setObjectName("QModulesWindow1")
        QModulesWindow1.resize(400, 310)
        QModulesWindow1.setStyleSheet("background-color: white")
        self.frame = QtWidgets.QFrame(QModulesWindow1)
        self.frame.setGeometry(QtCore.QRect(0, 20, 401, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line_q1m = QtWidgets.QLineEdit(self.frame)
        self.line_q1m.setGeometry(QtCore.QRect(40, 50, 151, 22))
        self.line_q1m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_q1m.setStyleSheet("color: white; background-color: #E80C94;")
        self.line_q1m.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_q1m.setObjectName("line_q1m")
        self.line_q2m = QtWidgets.QLineEdit(self.frame)
        self.line_q2m.setGeometry(QtCore.QRect(220, 50, 151, 22))
        self.line_q2m.setStyleSheet("color: white; background-color: #E80C94;")
        self.line_q2m.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_q2m.setObjectName("line_q2m")
        self.operation = QtWidgets.QComboBox(self.frame)
        self.operation.setGeometry(QtCore.QRect(70, 160, 281, 31))
        self.operation.setStyleSheet("color: white; background-color: #E80C94;")
        self.operation.setObjectName("operation")
        self.operation.addItem("")
        self.operation.addItem("")
        self.operation.addItem("")
        self.operation.addItem("")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 110, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.result = QtWidgets.QLabel(self.frame)
        self.result.setGeometry(QtCore.QRect(10, 240, 371, 31))
        self.result.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result.setStyleSheet("color: white; background-color: #E80C94;")
        self.result.setFrameShape(QtWidgets.QFrame.Box)
        self.result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result.setObjectName("result")
        self.line_q1n = QtWidgets.QLineEdit(self.frame)
        self.line_q1n.setGeometry(QtCore.QRect(40, 80, 151, 22))
        self.line_q1n.setStyleSheet("color: white; background-color: #E80C94;")
        self.line_q1n.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_q1n.setObjectName("line_q1n")
        self.line_q2n = QtWidgets.QLineEdit(self.frame)
        self.line_q2n.setGeometry(QtCore.QRect(220, 80, 151, 22))
        self.line_q2n.setStyleSheet("color: white; background-color: #E80C94;")
        self.line_q2n.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_q2n.setObjectName("line_q2n")
        self.pushButton_return = QtWidgets.QToolButton(QModulesWindow1)
        self.pushButton_return.setGeometry(QtCore.QRect(0, 0, 27, 22))
        self.pushButton_return.setStyleSheet("background-color:#E80C94; color: white")
        self.pushButton_return.setObjectName("pushButton_return")

        self.retranslateUi(QModulesWindow1)
        QtCore.QMetaObject.connectSlotsByName(QModulesWindow1)

    def retranslateUi(self, QModulesWindow1):
        _translate = QtCore.QCoreApplication.translate
        QModulesWindow1.setWindowTitle(_translate("QModulesWindow1", "Прочие действия"))
        self.label_3.setText(_translate("QModulesWindow1", "Введите 2 рациональных числа:"))
        self.line_q1m.setText(_translate("QModulesWindow1", "0"))
        self.line_q2m.setText(_translate("QModulesWindow1", "0"))
        self.operation.setItemText(0, _translate("QModulesWindow1", "Сумма"))
        self.operation.setItemText(1, _translate("QModulesWindow1", "Разность"))
        self.operation.setItemText(2, _translate("QModulesWindow1", "Произведение"))
        self.operation.setItemText(3, _translate("QModulesWindow1", "Деление"))
        self.label.setText(_translate("QModulesWindow1", "Выберите действие:"))
        self.label_2.setText(_translate("QModulesWindow1", "Результат:"))
        self.result.setText(_translate("QModulesWindow1", "0"))
        self.line_q1n.setText(_translate("QModulesWindow1", "1"))
        self.line_q2n.setText(_translate("QModulesWindow1", "1"))
        self.pushButton_return.setText(_translate("QModulesWindow1", "<-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QModulesWindow1 = QtWidgets.QDialog()
    ui = Ui_QModulesWindow1()
    ui.setupUi(QModulesWindow1)
    QModulesWindow1.show()
    sys.exit(app.exec_())

