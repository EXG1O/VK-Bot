# -*- coding: utf-8 -*-

# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# GUI
import Registration_Window.registration_window as registration_window
import Authorization_Window.authorization_window as authorization_window
import Warning_Window.warning_window as warning_window
from main_window import MainWindow
from message_box import MessageBox

# Другое
import config as Config
import requests
import json
import sys

# Глобальные функции
# ==================================================================
def show_password(self): # Функция для показа пароля в текстовом поле для пароля
	if self.ui.PasswordLineEdit.echoMode() == 2:
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../Icons/eyeOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.ShowPasswordButton.setIcon(icon)
		self.ui.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
	else:
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../Icons/eyeOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.ShowPasswordButton.setIcon(icon)
		self.ui.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
# ==================================================================

# Графический интерфейс программы
# ==================================================================
class RegistrationWindow(QtWidgets.QMainWindow): # Окно регистрации
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = registration_window.Ui_MainWindow()
		self.ui.setupUi(self)

		# Отключаем стандартные границы окна программы
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.center()

		# Обработчики основных кнопок
		self.ui.ShowPasswordButton.clicked.connect(lambda: show_password(self))
		self.ui.CreateAccountButton.clicked.connect(self.create_account)
		self.ui.LoginLineEdit.returnPressed.connect(self.create_account)
		self.ui.PasswordLineEdit.returnPressed.connect(self.create_account)
		self.ui.AskButton.clicked.connect(self.authorization_window)

		# Обработчики кнопок с панели
		self.ui.CloseWindowButton.clicked.connect(lambda: self.close())
		self.ui.MinimizeWindowButton.clicked.connect(lambda: self.showMinimized())

	# Перетаскивание безрамочного окна
	# ==================================================================
	def center(self):
		qr = self.frameGeometry()
		cp = QtWidgets.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QtCore.QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except AttributeError:
			pass
	# ==================================================================

	# Логика основных кнопок
	# ==================================================================
	def create_account(self):
		data = {
			'Login': self.ui.LoginLineEdit.text(),
			'Password': self.ui.PasswordLineEdit.text()
		}
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/registration', json = data)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')

			auth = AuthorizationWindow()
			self.close()
			auth.show()
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')

	def authorization_window(self):
		auth = AuthorizationWindow()
		self.close()
		auth.show()
	# ==================================================================

class AuthorizationWindow(QtWidgets.QMainWindow): # Окно авторизации
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = authorization_window.Ui_MainWindow()
		self.ui.setupUi(self)

		# Отключаем стандартные границы окна программы
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.center()

		# Обработчики основных кнопок
		self.ui.ShowPasswordButton.clicked.connect(lambda: show_password(self))
		self.ui.AuthorizationButton.clicked.connect(self.authorization)
		self.ui.LoginLineEdit.returnPressed.connect(self.authorization)
		self.ui.PasswordLineEdit.returnPressed.connect(self.authorization)
		self.ui.AskButton.clicked.connect(self.registration_window)

		# Обработчики кнопок с панели
		self.ui.CloseWindowButton.clicked.connect(lambda: self.close())
		self.ui.MinimizeWindowButton.clicked.connect(lambda: self.showMinimized())

	# Перетаскивание безрамочного окна
	# ==================================================================
	def center(self):
		qr = self.frameGeometry()
		cp = QtWidgets.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QtCore.QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except AttributeError:
			pass
	# ==================================================================

	# Логика основных кнопок
	# ==================================================================
	def authorization(self):
		data = {
			'Login': self.ui.LoginLineEdit.text(),
			'Password': self.ui.PasswordLineEdit.text()
		}
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/authorization', json = data)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
			Config.UNIQUE_KEY = server_answer_text['Unique_Key']
			bot_panel = MainWindow()
			self.close()
			bot_panel.show()
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')

	def registration_window(self):
		reg = RegistrationWindow()
		self.close()
		reg.show()
	# ==================================================================

class WarningWindow(QtWidgets.QMainWindow): # Окно предупреждения
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = warning_window.Ui_MainWindow()
		self.ui.setupUi(self)

		# Отключаем стандартные границы окна программы
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.center()

		# Обработчики основных кнопок
		self.ui.YesButton.clicked.connect(self.yes_button)
		self.ui.NoButton.clicked.connect(lambda: self.close())

		# Обработчики кнопок с панели
		self.ui.CloseWindowButton.clicked.connect(lambda: self.close())
		self.ui.MinimizeWindowButton.clicked.connect(lambda: self.showMinimized())

	# Перетаскивание безрамочного окна
	# ==================================================================
	def center(self):
		qr = self.frameGeometry()
		cp = QtWidgets.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QtCore.QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except AttributeError:
			pass
	# ==================================================================

	# Логика основных кнопок
	# ==================================================================
	def yes_button(self):
		authorization_window = AuthorizationWindow()
		self.close()
		authorization_window.show()
	# ==================================================================
# ==================================================================

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = WarningWindow()
	myapp.show()
	sys.exit(app.exec_())