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

def mk_prjct(username):
	prj_name=input("введите название создаваемого проекта\n>> ")
	uc.make_project(username,prj_name)
	return prj_name
def exit(username):
	if input("Вы уверены, что хотите выйти из текущей сессии пользователя </"+username+"/>?(д/н)\n>> ").lower() in ["yes","да","y","д"]:
		return True
	else:
		return False

def commit(username,project_name,branch_name):
	if not uc.have_user_some_lvl_of_rights(username,project_name,branch_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	check = uc.check_updates(username,project_name,branch_name)
	if check:
		element = {}
		element["user"] = username
		element["date-time"] = datetime.now()
		gl_dest=var.global_destination+"/"+project_name + '/' + branch_name + '/'
		lc_dest=var.users_destination+"/"+username+"/"+project_name + '/' + branch_name + '/'
		element["changes"]=chingl.global_changes(username,project_name,branch_name,gl_dest,lc_dest)
		if element["changes"]=={}:
			print("Не было внесено никаких изменений")
			return
		path_to_stack = var.users_destination+username+"/"+project_name+'/'+branch_name+"/"+".stack.txt"
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
        del_last_commit(username, project_name,branch_name)
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


def pre_push(username,project_name,branch_name):
	if not uc.have_user_some_lvl_of_rights(username,project_name,branch_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	local_stack = sc.load_l(username,project_name,branch_name)
	global_stack = sc.load_g(project_name,branch_name)
	of.push(local_stack,global_stack,project_name,branch_name)


def pre_pull(username,project_name,branch_name):
	if not uc.have_user_some_lvl_of_rights(username,project_name,branch_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	local_stack = sc.load_l(username,project_name,branch_name)
	global_stack = sc.load_g(project_name,branch_name)
	of.pull(local_stack,global_stack,username,project_name,branch_name)



def show_projects(username):
	count=0
	os.chdir(var.administration)
	f = open('users_rights_for_projects.txt', 'rb')
	obj = pickle.load(f)
	f.close()
	print("Cписок доступных вам проектов для загрузки:  \n")
	for project in obj.keys():
		for branch in obj[project].keys():
			if username in obj[project][branch]:
				print("Проект: "+project+", ветка: "+branch+"\n")
				count+=1
	if count==0:
		return 0
	else:
		return 1						

def show_loc_projects(username):
	count=0
	os.chdir(var.users_destination+"/"+username)
	prj_list=os.listdir()
	os.chdir(var.administration)
	f = open('users_rights_for_projects.txt', 'rb')
	obj = pickle.load(f)
	f.close()
	print("Cписок доступных вам проектов:  \n")
	for project in obj.keys():
		for branch in obj[project].keys():
			if username in obj[project][branch] and project in prj_list:
				print("Проект: "+project+", ветка: "+branch+"\n")
				count+=1
	if count==0:
		return 0
	else:
		return 1					


def interface(username):
	while 1:
		print("Вы можете:\n-Выбрать свой проект(сhoose)")
		print("-Создать новый(make)")
		print("-Загрузить проект из глобальной директории(load)")
		print("-Или выйти(exit)")
		command=input(">> ")
		if command == "choose":
			print("Выберите проект")
			if not show_loc_projects(username):
				print("У вас нет доступных проектов.\n")
				continue
			project_name=input(">> ")
			print("Выберите ветвь")
			branch_name=input(">> ")
			os.chdir(var.users_destination+"/"+username+"/")
			prj_list = os.listdir()
			if project_name in prj_list:
				os.chdir(var.users_destination+"/"+username+"/"+project_name)
				branch_list=os.listdir()
				if branch_name in branch_list:
					if uc.have_user_some_lvl_of_rights(username, project_name, branch_name):
						break
				else:
					print("В вашей копии проекта нет такой ветки, попробуйте загрузить её или выберите другую.\n")		
			else:
				print("В вашей локальной папке нет данного проекта, попробуйте загрузить его или создать новый, или выберите другой.\n")

		elif command == "make":
			project_name=mk_prjct(username)
			branch_name="master"
			break
		elif command == "load":
			print("Выберите проект")
			if not show_projects(username):
				print("У вас нет доступных для загрузки проектов.\n")
				continue
			project_name=input(">> ")
			print("Выберите ветку")
			branch_name=input(">> ")
			if uc.make_project_local(username, project_name,branch_name) != 0:
				pre_pull(username,project_name,branch_name)
				break
			else: 
				print("Такого проекта или ветки не существует. Попробуйте создать его.\n")	
		elif command == "exit":
			if exit(username):
				return
		else:
			print("Такой команды нет.")
	print("Вы выбрали проект </"+project_name+"/>\nВетвь </"+branch_name+"/>")			

	print("Выберите команду(чтобы узнать список команд, наберите help)")
	while 1:
		command = input(">> ")
		if command == "make_project":
			project_name=mk_prjct(username)
			branch_name="master"
			print("Вы выбрали проект </"+project_name+"/>\nВетвь </"+branch_name+"/>")
		elif command == "set_project":
			print("Выберите проект")
			if not show_loc_projects(username):
				print("У вас нет доступных проектов.\n")
			project_name=input(">> ")
			print("Выберите ветвь")
			branch_name=input(">> ")
			os.chdir(var.users_destination+"/"+username+"/")
			prj_list = os.listdir()
			if project_name in prj_list:
				os.chdir(var.users_destination+"/"+username+"/"+project_name)
				branch_list=os.listdir()
				if branch_name in branch_list:
					if uc.have_user_some_lvl_of_rights(username, project_name, branch_name):
						print("Вы выбрали проект </"+project_name+"/>\nВетвь </"+branch_name+"/>")
				else:
					print("В вашей копии проекта нет такой ветки, попробуйте загрузить её или выберите другую.\n")		
			else:
				print("В вашей локальной папке нет данного проекта, попробуйте загрузить его или создать новый, или выберите другой.\n")




		elif command == "commit":
			choice = input("Вы хотите закоммитить весь проект?(д/н)\n>> ").lower()
			if choice in ["да", "д", "yes", "y"]:
				try:
					commit(username,project_name,branch_name)
				except UnboundLocalError:
					print("у вас еще не выбрана ветка, в которой вы будете работать")
					# commit(username,project_name,"master")
					os.chdir(var.users_destination+"/"+username+"/"+project_name)
					print("доступны такие ветки:")
					mass_of_br = os.listdir()
					for i in mass_of_br:
						print(i)
					print("Пожалуйста, выберите одну из предоставленных веток")
					while 1:
						branch_name = input(">> ")
						if branch_name in mass_of_br:
							commit(username,project_name,branch_name)
							break
						else:
							print("такой ветки нет!")
					# while 1:

						# try:
						# 	commit(username,project_name,input())
						# except:
						# 	print("такой ветки не существует, попробуйте еще раз")
				print("commit успешно выполнен.")		
			elif choice in ['нет', 'н', 'no', 'n']:
				what_to_commit(username, project_name)
			else:
				print('Ошибка! Для выбора ответа можно использовать: да, д, yes, y, нет, н, no, n')

		elif command == "show_projects":
			show_projects(username)


		elif command == "push":
			pre_push(username,project_name,branch_name)
			print("push успешно выполнен.")



		elif command == "update":
			pre_pull(username,project_name,branch_name)
			print("update успешно выполнен.")




		elif "log" in command:
			if len(command.split()) > 1:
				log.log(project_name," ".join(command.split()[1:]), branch_name)
			else:
				log.log(project_name,"--simple", branch_name)





		elif 'del_last_commit' in command:
			del_last_commit(username, project_name)
			print("del_last_commit успешно выполнен.")






		elif command == 'add_users_to_prj':
			uc.add_users_to_prj(username, project_name)




		elif command == 'del_users_from_prj':
			uc.del_users_from_prj(username, project_name)




		elif command == 'exit':
			if dict_command[command](username):
				return




		elif command == "help":
			dict_command[command]()

		elif command=="del_project":
			if uc.del_project(username, project_name):
				break

		elif command=="del_branch":
			if uc.del_branch(username, project_name, branch_name):
				break


			
		elif command == 'make_branch':
			print("Введите название ветки")
			branch_name=input(">> ")
			uc.make_branch(username,project_name,branch_name)
			print("Вы выбрали ветку </"+branch_name+"/>")

		elif command == "change_branch":
			print("Введите название ветки")
			branch_name=input(">> ")
			os.chdir(var.users_destination+"/"+username+"/"+project_name+'/')
			br_list = os.listdir()
			if branch_name in br_list:
				print("Вы выбрали ветку </"+branch_name+"/>")
			else:
				print("у вас нету такой ветки")
				if input("Вы хотите создать ветку?(д/н)\n>> ").lower() in ["да", "д", "yes", "y"]:
					branch_name=uc.make_branch(username,project_name,branch_name)
					print("Вы выбрали ветку </"+branch_name+"/>")


		elif command == 'merge':
			uc.merge(username,project_name,branch_name)
			print("merge успешно выполнен.")


		else:
			print('Такой команды нет. Пожалуйста, повторите ввод.')
			helpme()

	interface(username)					


