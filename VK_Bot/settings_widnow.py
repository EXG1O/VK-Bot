# -*- coding: utf-8 -*-

# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# GUI
import Main_Window.Settings_Window.settings_widnow as settings_widnow
from message_box import MessageBox

# Другое
import server as Server

# Окно настроек бота
class SettingsWindow(QtWidgets.QMainWindow):
	def __init__(self, parent = None):
		super().__init__(parent, QtCore.Qt.Window)
		self.ui = settings_widnow.Ui_Form()
		self.ui.setupUi(self)
		self.setWindowModality(2)

		# Отключаем стандартные границы окна программы
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.center()

		# Все нужные переменные
		self.automati_save_log_button_status = False

		# Запуск потоков
		self.widget_settings_theard = WidgetSettingsTheard()
		self.widget_settings_theard.signalWidgetSettings.connect(self.widget_settings)
		self.widget_settings_theard.start()

		# Обработчики кнопок с панели
		self.ui.CloseWindowButton.clicked.connect(self.close_window_button)
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
	def automati_save_log_button(self):
		if self.automati_save_log_button_status == True:
			self.automati_save_log_button_status = False

			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/Off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.AutomatiSaveLogButton.setIcon(icon)
		else:
			self.automati_save_log_button_status = True

			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/On.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.AutomatiSaveLogButton.setIcon(icon)

	def signalButton(self, message_box, text):
		message_box.close()
		if text == 'Да':
			self.save_bot_settings()

	def close_window_button(self):
		different_settings = False
		if self.bot_settings['Automati_Save_Log'] != self.automati_save_log_button_status:
			different_settings = True
		elif self.bot_settings['VK_Token'] != self.ui.VKTokenLineEdit.text():
			different_settings = True
		elif self.bot_settings['Group_ID'] != self.ui.IDBotLineEdit.text():
			different_settings = True

		if different_settings == True:
			message_box = MessageBox(text = 'Вы изменили настройки, хотите их сохранить?', button_1 = 'Да', button_2 = 'нет')
			message_box.message_box.signalButton.connect(lambda text: self.signalButton(message_box.message_box, text))

		self.close()

	def show_vk_token_button(self):
		if self.ui.VKTokenLineEdit.echoMode() == 2:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/eyeOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.ShowVKTokenButton.setIcon(icon)
			self.ui.VKTokenLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
		else:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/eyeOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.ShowVKTokenButton.setIcon(icon)
			self.ui.VKTokenLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

	def save_bot_settings_button(self):
		self.bot_settings = {
			'Automati_Save_Log': self.automati_save_log_button_status,
			'VK_Token': self.ui.VKTokenLineEdit.text(),
			'Group_ID': self.ui.IDBotLineEdit.text()
		}
		Server.update_bot_settings(self.bot_settings)

		MessageBox(text = 'Успешное сохранение настроек бота', button_2 = 'Окей')
	# ==================================================================

	# Обычные функции
	# ==================================================================
	def widget_settings(self, bot_settings):
		# Настройка виджетов
		self.bot_settings = bot_settings
		self.ui.VKTokenLineEdit.setText(self.bot_settings['VK_Token'])
		self.ui.IDBotLineEdit.setText(self.bot_settings['Group_ID'])

		if self.bot_settings['Automati_Save_Log'] == True:
			self.automati_save_log_button_status = True
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/On.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.AutomatiSaveLogButton.setIcon(icon)

		# Обработчики основных кнопок
		self.ui.ShowVKTokenButton.clicked.connect(self.show_vk_token_button)
		self.ui.AutomatiSaveLogButton.clicked.connect(self.automati_save_log_button)
		self.ui.SaveBotSettingsButton.clicked.connect(self.save_bot_settings_button)
	# ==================================================================

# Поток для настрйоки виджетов
class WidgetSettingsTheard(QtCore.QThread):
	signalWidgetSettings = QtCore.pyqtSignal(dict)

	def __init__(self):
		QtCore.QThread.__init__(self)

	def run(self):
		bot_settings = Server.get_bot_settings()
		self.signalWidgetSettings.emit(bot_settings)