# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail_confirmation_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 221)
        self.Window = QtWidgets.QFrame(Form)
        self.Window.setGeometry(QtCore.QRect(10, 10, 521, 201))
        self.Window.setStyleSheet("QFrame{\n"
"    border-radius: 7px;\n"
"    background-color: #1B1D23;\n"
"}")
        self.Window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Window.setObjectName("Window")
        self.WindowFrame = QtWidgets.QFrame(self.Window)
        self.WindowFrame.setGeometry(QtCore.QRect(0, 0, 521, 31))
        self.WindowFrame.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"}")
        self.WindowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WindowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WindowFrame.setObjectName("WindowFrame")
        self.CloseWindowButton = QtWidgets.QPushButton(self.WindowFrame)
        self.CloseWindowButton.setGeometry(QtCore.QRect(480, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CloseWindowButton.setFont(font)
        self.CloseWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseWindowButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.CloseWindowButton.setObjectName("CloseWindowButton")
        self.MinimizeWindowButton = QtWidgets.QPushButton(self.WindowFrame)
        self.MinimizeWindowButton.setGeometry(QtCore.QRect(439, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MinimizeWindowButton.setFont(font)
        self.MinimizeWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MinimizeWindowButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.MinimizeWindowButton.setDefault(False)
        self.MinimizeWindowButton.setObjectName("MinimizeWindowButton")
        self.Label = QtWidgets.QLabel(self.Window)
        self.Label.setGeometry(QtCore.QRect(20, 34, 481, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label.sizePolicy().hasHeightForWidth())
        self.Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Label.setFont(font)
        self.Label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("Label")
        self.QuniqueCodeLineEdit = QtWidgets.QLineEdit(self.Window)
        self.QuniqueCodeLineEdit.setGeometry(QtCore.QRect(20, 90, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QuniqueCodeLineEdit.setFont(font)
        self.QuniqueCodeLineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius: 12px;\n"
"}")
        self.QuniqueCodeLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.QuniqueCodeLineEdit.setInputMask("")
        self.QuniqueCodeLineEdit.setText("")
        self.QuniqueCodeLineEdit.setFrame(False)
        self.QuniqueCodeLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.QuniqueCodeLineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.QuniqueCodeLineEdit.setObjectName("QuniqueCodeLineEdit")
        self.MailConfirmationButton = QtWidgets.QPushButton(self.Window)
        self.MailConfirmationButton.setGeometry(QtCore.QRect(150, 140, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MailConfirmationButton.setFont(font)
        self.MailConfirmationButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MailConfirmationButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.MailConfirmationButton.setObjectName("MailConfirmationButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CloseWindowButton.setText(_translate("Form", "X"))
        self.MinimizeWindowButton.setText(_translate("Form", "_"))
        self.Label.setText(_translate("Form", "Подтверждения почты"))
        self.QuniqueCodeLineEdit.setPlaceholderText(_translate("Form", "Введите код, который пришёл вам на почту"))
        self.MailConfirmationButton.setText(_translate("Form", "Подтвердить почту"))
