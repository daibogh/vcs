import variables as var
import user_commands as uc
import overwriting_files as of
import stack_commands as sc
import os
import log
import pickle
import py_detour as py_dtour
import find_changes as find_ch
import changes_in_global as chingl
from datetime import datetime
def helpme():
	f = open(var.global_destination + '/bin/help.txt', 'r')
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
def commit(username,project_name):
	if not have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	check = uc.check_updates(username,project_name)
	if check:
		element = {}
		element["user"] = username
		element["date-time"] = datetime.now()
		element["changes"]=chingl.global_changes(username,project_name)
		if element["changes"]=={}:
			print("Не было внесено никаких изменений")
			return
		path_to_stack = var.users_destination+username+"/"+project_name+"/"+"stack.txt"
		f = open(path_to_stack,"rb")
		stack = pickle.load(f)
		stack.append(element)
		f = open(path_to_stack,"wb")
		pickle.dump(stack,f)
		f.close()
	else:
		print("Ваша версия устарела, обновите проект (update)")
			
def what_to_commit(username, project_name):
    if not have_user_some_lvl_of_rights(username,project_name):
        print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
        return
    commit(username, project_name)
    os.chdir(var.users_destination + username + '/' + project_name)
    f = open('stack.txt','rb')
    stack = pickle.load(f)
    f.close()
    print('Список изменённых файлов')
    kk = 1
    for changed_file in stack[-1]['changes'].keys():
        k = 0
        for i in reversed(changed_file):  # reversed(changed_file):
            k -= 1
            if i == '/':
                print(str(kk)+':',changed_file[(k+1):], '\tпуть:', changed_file)
                kk += 1
                break
    print('Введите через пробел номера файлов, которые вы хотите закоммитить:')
    file_numbers = [int(i) for i in input('> ').split()]
    print('Ваш выбор:')
    k = 0
    for changed_file in stack[-1]['changes'].keys():
        k += 1
        if k in file_numbers:
            print(changed_file)
    print('Введите 1 для продолжения, или 0 для отмены: ', end='')
    choice = int(input())
    if choice:
        m = 0
        k = 0
        for changed_file in stack[-1]['changes'].keys():
            k += 1
            print('k = ',k,'\tfile_n = ',file_numbers ,'\t k not in file_numbers = ' , k not in file_numbers)
            if k not in file_numbers:
                file_to_del_from_stack = changed_file
                print('to del', file_to_del_from_stack)
                del (stack[-1]['changes'][file_to_del_from_stack])
                break
        #
        f = open('stack.txt', 'wb')
        pickle.dump(stack, f)
        f.close()
        print('Добавление коммита было успешно завершено')
    else:
        del_last_commit(username, project_name)
        print('Добавление коммита было прервано')
        return
def del_last_commit(username, project_name):
    if not have_user_some_lvl_of_rights(username,project_name):
        print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
        return
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

def pre_push(username,project_name):
	if not have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	local_stack = sc.load_l(username,project_name)
	global_stack = sc.load_g(project_name)
	of.push(local_stack,global_stack,project_name)
def pre_pull(username,project_name):
	if not have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	local_stack = sc.load_l(username,project_name)
	global_stack = sc.load_g(project_name)
	of.pull(local_stack,global_stack,username,project_name)


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
def show_projects(username):
	os.chdir(var.users_destination+username+"/")
	print("список доступных вам проектов:  \n")
	for project in os.listdir():
		print(project+'\n')
	print("End-############################\n")
def interface(username):
	while 1:
		if not os.path.exist(var.administration + 'users_requests.txt'):
			base_struct = {}
			f = open('users_requests.txt','wb')
			pickle.dump(base_struct, f)
			f.close()
		if not os.path.exist(var.administration + 'users_rights_for_projects.txt'):
			base_struct = {}
			f = open('users_rights_for_projects.txt','wb')
			pickle.dump(base_struct, f)
			f.close()
		print("Вы можете выбрать свой проект(сhoose)")
		print("создать новый(make)")
		print("загрузить проект из глобальной директории(load)")
		print("или выйти(exit)")
		command=input(">> ")
		if command == "choose":
			print("Выберите проект")
			show_projects(username)
			project_name=input(">> ")
			os.chdir(var.users_destination+"/"+username+"/")
			prj_list = os.listdir()
			if project_name in prj_list:
				break
			else:
				print("у вас нет такого проекта")
				if input("Вы хотите создать проект?(д/н) ").lower() in ["да", "д", "yes", "y"]:
					project_name=mk_prjct(username)
					break
		elif command == "make":
			project_name=mk_prjct(username)
			break
		elif command == "load":
			print("Выберите проект")
			show_global_projects()
			project_name=input(">> ")
			if uc.make_project_local(username, project_name) != 0:
				pre_pull(username,project_name)
				break
		elif command == "exit":
			if exit(username):
				return
		else:
			print("Такой команды нет.")		

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
			choice = input("Вы хотите закоммитить весь проект?(д/н) ").lower()
			if choice in ["да", "д", "yes", "y"]:
				commit(username,project_name)
			elif choice in ['нет', 'н', 'no', 'n']:
				what_to_commit(username, project_name)
			else:
				print('Ошибка! Для выбора ответа можно использовать: да, д, yes, y, нет, н, no, n')

		elif command == "show projects":
			show_projects(username)


		elif command == "push":
			pre_push(username,project_name)





		elif command == "update":
			pre_pull(username,project_name)




		elif "log" in command:
			if len(command.split()) > 1:
				log.log(project_name," ".join(command.split()[1:]))
			else:
				log.log(project_name,"--simple")





		elif 'del_last_commit' in command:
			del_last_commit(username, project_name)






		elif command == 'add_users_to_prj':
			uc.add_users_to_prj(username, project_name)






		elif command == 'del_users_to_prj':
			uc.del_users_to_prj(username, project_name)






		elif dict_command.get(command) != None and command != 'exit' and command != "help":
			dict_command[command](username)




		elif command == 'exit':
			if dict_command[command](username):
				return




		elif command == "help":
			dict_command[command]()




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

