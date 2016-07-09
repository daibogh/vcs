import variables as var
import user_commands as uc
import overwriting_files as of
import stack_commands as sc
import os
def helpme():
	f = open(var.global_destination+'/bin/help.txt','r')
	for line in f:
		print(line)
	f.close()	
	return		
def show_prjs():
	return
def set_prj():
	return
def add_prj():
	return
def set_ver():
	return
def set_file():
	return
def add():
	return
commit = uc.commit
def del_in_index():
	return
def del_file():
	return
def get_status():
	return
def mk_prjct(username):
	uc.make_project(username,input("введите название создаваемого проекта\n"))
def logout(username):
	if input("Вы уверены, что хотите выйти из текущей сессии пользователя </"+username+"/>?(д/н) ").lower() in ["yes","да","y","д"]:
		return True
	else:
		return False

dict_command = {
	'help':helpme,
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
	'logout':logout,
	"make project":mk_prjct,
	"push":of.push
}
def pre_push(username,project_name):
	local_stack = sc.load_l(username,project_name)
	global_stack = sc.load_g(project_name)
	of.push(local_stack,global_stack)

def interface(username):
	print("выберите команду(чтобы узнать список команд, наберите help)")
	while 1:
		command = input(">> ")
		if command == "make project":
			mk_prjct(username)
		elif command == "set project":
			project_name = input("введите название проекта\n")
			os.chdir(var.users_destination+"/"+username+"/")
			prj_list = os.listdir()
			if project_name in prj_list:
				pass
			else:
				print("у вас нет такого проекта")
		elif command == "commit":
			commit(username,project_name)
		elif command == "push":
			pre_push(username,project_name)
		elif dict_command.get(command) != None and command != 'logout':
			dict_command[command](username)
		elif command == 'logout':
			if dict_command[command](username):
				return	
		else:
			print('Такой команды нет. Пожалуйста, повторите ввод.')
			helpme()

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

