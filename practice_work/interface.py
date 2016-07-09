def help():
	f = open('help().txt','r')
	for line in f:
		print(line)
def show_prjs():
def set_prj():
def add_prj():
def set_ver():
def set_file():
def add():
def commit():
def del_in_index():
def del_file():
def get_status():
def exit():

dict_command = {
	'help':help,
	'show_prjs':show_prjs,
	'set_prj':set_prj,
	'add_prj':add_prj,
	'set_ver':set_ver,
	'set_file':set_file,
	'add':add,
	'commit':commit,
	'del_in_index':del_in_index,
	'del_file':del_file,
	'get_status':get_status,
	'exit':exit
}

#import commands
# def interface(user):
# 	print("выберите команду(чтобы узнать список команд, наберите help)")
# 	print('>>', end=' ')
# 	while True:
# 		command = input()
# 		if dict_command.get(command) != None:
# 			dict_command[command]()
# 		else:
# 			print('Такой команды нет. Пожалуйста, повторите ввод.')
# 			help()
# 		if command == 'exit':
# 			break
# 		print('>>', end=' ')
