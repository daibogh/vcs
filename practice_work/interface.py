'''
Команды для интерфейса:
	help
	set_prj
	set_file
	set_ver   выбрать версию 
	show_prjs

	commit
	get_status

	exit

	push
	add_prj
	можно добавить команду клонирования в выбранный каталог
'''
def help():
	''Можно сделать вывод из файла''
	print('\t\tСписок команд:\n')
	print('\thelp - Вывести список команд')
	print('\tshow_prjs - Вывести список всех проектов')
	print('\tset_prj - Выбрать проект')
	print('\tadd_prj - Добавить существующий проект')
	print('\tset_ver - Выбрать версию проекта (по умолчанию стоит последняя версия)')
	print('\tset_file - Выбрать файл проекта')
	print()
	print('\tadd - Выбрать файлы для добавления в финальную версию проекта (проиндексировать файл)')
	print('\tcommit - Добавить выбранные файлы в финальную версию проекта')
	print('\tpush - Добавить последние изменения на сервер')
	print('\tdel_in_index - Удалить файл из индекса (отслеживаемых файлов)')
	print('\tdel_file - Удалить файл из системы')
	#print('\t\push - Добавить ваши изменения в финальную версию проекта')
	print('\tget_status - Вывести текущее состояние всех файлов')
	print('\texit')

def execute_query(command):
	if command == 'help':
		help()
	elif command == 'show_prjs':
		/
	elif command == 'set_prj':
		/
	elif command == 'add_prj':
		/
	elif command == 'set_ver':
		/
	elif command == 'set_file':
		/
	elif command == 'add':
		/
	elif command == 'commit':
		/
	elif command == 'del_in_index':
		/
	elif command == 'del_file':
		/
	elif command == 'get_status':
		/
	elif command == 'exit':
		/
	else:
		print('Такой команды нет. Пожалуйста, повторите ввод.')
		help()

import commands
def interface(user):
	print("выберите команду(чтобы узнать список команд, наберите help)")
	print('>>', end=' ')
	while (command = import()) != 'exit':
		execute_query(command)
		print('>>', end=' ')


