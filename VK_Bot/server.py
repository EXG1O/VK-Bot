# -*- coding: utf-8 -*-

# GUI
from message_box import MessageBox

# Другие
import config as Config
import requests
import json

def get_bot_settings():
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/bot_settings/get', json = {
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			return server_answer_text['Bot_Settings']
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')

def update_bot_settings(bot_settings):
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/bot_settings/update', json = {
				'Bot_Settings': bot_settings,
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		if server_answer.status_code == 400:
			server_answer_text = json.loads(server_answer.text)
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')

def get_user_commands():
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/user_commands/get', json = {
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			return server_answer_text['User_Commands']
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')

def update_user_commands(user_commands):
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/user_commands/update', json = {
				'User_Commands': user_commands,
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		if server_answer.status_code == 400:
			server_answer_text = json.loads(server_answer.text)
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')

def get_log():
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/log/get', json = {
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			return server_answer_text['Log']
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')

def update_log(log):
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/log/update', json = {
				'Log': log,
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		if server_answer.status_code == 400:
			server_answer_text = json.loads(server_answer.text)
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')

def find_in_database(sqlite3_command):
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/database/find', json = {
				'SQLite3_Command': sqlite3_command,
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			return server_answer_text['Result']
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')

def find_all_in_database(sqlite3_command):
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/database/find_all', json = {
				'SQLite3_Command': sqlite3_command,
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			return server_answer_text['Result']
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')

def edit_database(sqlite3_command, values = ()):
	try:
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/files/database/edit_database', json = {
				'SQLite3_Command': sqlite3_command,
				'Values': values,
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			} if values != () else {
				'SQLite3_Command': sqlite3_command,
				'Password': Config.PASSWORD,
				'Unique_Key': Config.UNIQUE_KEY
			}
		)
		if server_answer.status_code == 400:
			server_answer_text = json.loads(server_answer.text)
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
	except requests.exceptions.ConnectionError:
		MessageBox(text = 'Отсутствует подключение к интернету', button_2 = 'Окей')