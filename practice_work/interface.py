import variables as var
import user_commands as uc
import overwriting_files as of
import stack_commands as sc
import os
import log
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
	prj_name=input("введите название создаваемого проекта\n>> ")
	uc.make_project(username,prj_name)
	return prj_name
def exit(username):
	if input("Вы уверены, что хотите выйти из текущей сессии пользователя </"+username+"/>?(д/н) ").lower() in ["yes","да","y","д"]:
		return True
	else:
		return False
<<<<<<< HEAD
=======
def del_last_commit(username, project_name):
    global_stack = sc.load_g(project_name)
    local_stack = sc.load_l(username, project_name)
    if local_stack in global_stack:
        print("невозможно удалить последний коммит, обратитесь к администратору")
        return
    else:
        print("вы уверены, что хотите удалить последний коммит?(д/н)")
        if input().lower() in ["да", "д", "yes", "y"]:
            local_stack = local_stack[:-1]
            sc.dump_l(username, project_name, local_stack)
            print("удаление прошло успешно")
            return 0


dict_command = {
	'help':helpme,
	'show_prjs':show_prjs,
	'set_prj':set_prj,
	'add_prj':add_prj,
	'set_ver':set_ver,
	'set_file':set_file,
	'add':add,
	'commit':commit,
	'del_last_commit':del_last_commit,
	'del_in_index':del_in_index,
	'del_file':del_file,
	'get_status':get_status,
	'exit':logout,
	"make project":mk_prjct,
	"push":of.push
}
>>>>>>> origin/master
def pre_push(username,project_name):
	local_stack = sc.load_l(username,project_name)
	global_stack = sc.load_g(project_name)
	of.push(local_stack,global_stack,project_name)
<<<<<<< HEAD
def del_last_commit(username, project_name):
    global_stack = sc.load_g(project_name)
    local_stack = sc.load_l(username, project_name)
    if local_stack in global_stack:
        print("невозможно удалить последний коммит, обратитесь к администратору")
        return
    else:
        print("вы уверены, что хотите удалить последний коммит?(д/н)")
        if input().lower() in ["да", "д", "yes", "y"]:
            local_stack = local_stack[:-1]
            sc.dump_l(username, project_name, local_stack)
            print("удаление прошло успешно")
            return 0

dict_command = {
	'help':helpme,
	'show_prjs':show_prjs,
	'set_prj':set_prj,
	'add_prj':add_prj,
	'set_ver':set_ver,
	'set_file':set_file,
	'add':add,
	'commit':commit,
	'del_last_commit':del_last_commit,
	'del_in_index':del_in_index,
	'del_file':del_file,
	'get_status':get_status,
	'exit':exit,
	"make project":mk_prjct,
	"push":of.push
}
=======
>>>>>>> origin/master

def interface(username):
	print("Выберите команду(чтобы узнать список команд, наберите help)")
	print("Для начала выберите проект или создайте новый")
	while 1:
		command=input("введите название проекта\n>> ")
		if command != "exit":
			project_name=command
			os.chdir(var.users_destination+"/"+username+"/")
			prj_list = os.listdir()
			if project_name in prj_list:
				break
			else:
				print("у вас нет такого проекта")
				if input("Вы хотите создать проект?(д/н) ").lower() in ["да", "д", "yes", "y"]:
					project_name=mk_prjct(username)
					break
		elif command == 'exit':
			if dict_command[command](username):
				return
	print("Вы выбрали проект </"+project_name+"/>")		
	print("Выберите команду(чтобы узнать список команд, наберите help)")				
	while 1:
		command = input(">> ")
		if command == "make project":
			project_name=mk_prjct(username)
			print("Вы выбрали проект </"+project_name+"/>")	
		elif command == "set project":
			project_name = input("введите название проекта\n")
			os.chdir(var.users_destination+"/"+username+"/")
			prj_list = os.listdir()
			if project_name in prj_list:
				print("Вы выбрали проект </"+project_name+"/>")	
			else:
				print("у вас нет такого проекта")
				if input("Вы хотите создать проект?(д/н) ").lower() in ["да", "д", "yes", "y"]:
					project_name=mk_prjct(username)	
					print("Вы выбрали проект </"+project_name+"/>")		
		elif command == "commit":
			commit(username,project_name)
		elif command == "push":
			pre_push(username,project_name)

		elif "log" in command:
			if len(command.split()) > 1:
				log.log(project_name," ".join(command.split()[1:]))
			else:
				log.log(project_name,"simple")
		elif 'del_last_commit' in command:
			del_last_commit(username, project_name)
		elif dict_command.get(command) != None and command != 'exit':
			dict_command[command](username)
		elif command == 'exit':
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

