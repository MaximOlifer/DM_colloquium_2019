# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\P_modules_Window_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PModulesWindow2(object):
    def setupUi(self, PModulesWindow2):
        PModulesWindow2.setObjectName("PModulesWindow2")
        PModulesWindow2.resize(400, 336)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PModulesWindow2.sizePolicy().hasHeightForWidth())
        PModulesWindow2.setSizePolicy(sizePolicy)
        self.frame = QtWidgets.QFrame(PModulesWindow2)
        self.frame.setGeometry(QtCore.QRect(0, 20, 401, 311))
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
        self.operation = QtWidgets.QComboBox(self.frame)
        self.operation.setGeometry(QtCore.QRect(70, 160, 281, 31))
        self.operation.setStyleSheet("color: white; background-color: #0D66FF;")
        self.operation.setObjectName("operation")
        self.operation.addItem("")
        self.operation.addItem("")
        self.operation.addItem("")
        self.operation.addItem("")
        self.operation.addItem("")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 110, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.result = QtWidgets.QLabel(self.frame)
        self.result.setGeometry(QtCore.QRect(10, 240, 371, 31))
        self.result.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result.setStyleSheet("color: white; background-color: #0D66FF;")
        self.result.setFrameShape(QtWidgets.QFrame.Box)
        self.result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result.setObjectName("result")
        self.pushButton_inputp = QtWidgets.QPushButton(self.frame)
        self.pushButton_inputp.setGeometry(QtCore.QRect(330, 60, 51, 28))
        self.pushButton_inputp.setStyleSheet("color: white; background-color: #0D66FF;")
        self.pushButton_inputp.setObjectName("pushButton_inputp")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(30, 50, 301, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(39, 42))
        self.scrollArea.setMaximumSize(QtCore.QSize(311, 51))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setStyleSheet("color: #0D66FF; background-color: white;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 301, 51))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.polinomial = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polinomial.sizePolicy().hasHeightForWidth())
        self.polinomial.setSizePolicy(sizePolicy)
        self.polinomial.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.polinomial.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.polinomial.setStyleSheet("color: white; background-color: #0D66FF;")
        self.polinomial.setFrameShape(QtWidgets.QFrame.Box)
        self.polinomial.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.polinomial.setObjectName("polinomial")
        self.horizontalLayout.addWidget(self.polinomial)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_return = QtWidgets.QToolButton(PModulesWindow2)
        self.pushButton_return.setGeometry(QtCore.QRect(0, 0, 27, 22))
        self.pushButton_return.setStyleSheet("color: white; background-color: #0D66FF;")
        self.pushButton_return.setObjectName("pushButton_return")

        self.retranslateUi(PModulesWindow2)
        QtCore.QMetaObject.connectSlotsByName(PModulesWindow2)

    def retranslateUi(self, PModulesWindow2):
        _translate = QtCore.QCoreApplication.translate
        PModulesWindow2.setWindowTitle(_translate("PModulesWindow2", "Преобразования многочлена"))
        self.label_3.setText(_translate("PModulesWindow2", "Введите многочлен:"))
        self.operation.setItemText(0, _translate("PModulesWindow2", "Старший коэффициент многочлена"))
        self.operation.setItemText(1, _translate("PModulesWindow2", "Степень многочлена"))
        self.operation.setItemText(2, _translate("PModulesWindow2", "НОК знаменателей коэффициентов и НОД числителей"))
        self.operation.setItemText(3, _translate("PModulesWindow2", "Производная многочлена"))
        self.operation.setItemText(4, _translate("PModulesWindow2", "Преобразование многочлена — кратные корни в простые"))
        self.label.setText(_translate("PModulesWindow2", "Выберите действие:"))
        self.label_2.setText(_translate("PModulesWindow2", "Результат:"))
        self.result.setText(_translate("PModulesWindow2", "0"))
        self.pushButton_inputp.setText(_translate("PModulesWindow2", "Ввести"))
        self.polinomial.setText(_translate("PModulesWindow2", "0"))
        self.pushButton_return.setText(_translate("PModulesWindow2", "<-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PModulesWindow2 = QtWidgets.QDialog()
    ui = Ui_PModulesWindow2()
    ui.setupUi(PModulesWindow2)
    PModulesWindow2.show()
    sys.exit(app.exec_())

