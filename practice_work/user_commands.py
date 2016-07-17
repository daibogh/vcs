import os
import pickle
import shutil
import variables as var
import stack_commands as sc
import py_detour as py_dtour
import find_changes as find_ch
import changes_in_global as chingl
import overwriting_files as ovf
from datetime import datetime
import interface as intf
import create_necessary_files as cnf
# def commit(username):
# 	stack = get_stack()
# 	stack.append(updates)
# 	f = open("stack.txt","wb")
# 	pickle.dump(stack,f)
# 	f.close()
# 
#def commit(username,project_name):
	# check = check_updates(username,project_name)
#	element = {}
#	element["user"] = username
#	element["date-time"] = datetime.now()
#	element["changes"]=chingl.global_changes(username,project_name)
#	if element["changes"]=={}:
#		print("Не было внесено никаких изменений")
#		return
#	path_to_stack = var.users_destination+username+"/"+project_name+"/"+"stack.txt"
#	f = open(path_to_stack,"rb")
#	stack = pickle.load(f)
#	stack.append(element)
#	f = open(path_to_stack,"wb")
#	pickle.dump(stack,f)
#	f.close()

def check_updates(username,project_name,branch_name):
	global_stack = sc.load_g(project_name,branch_name)
	
	local_stack = sc.load_l(username,project_name,branch_name)
	if len(global_stack)>len(local_stack):
		return False
	elif global_stack[-1] in local_stack:
		return True
	else:
		return False




#def push(username,project_name):
#	check = check_updates()
#	if check:
#		global_stack = sc.load_g(project_name)
#		local_stack = sc.load_l(username,project_name)
#
#
#
#		list_of_changes = []
#		for stack_element in reversed(local_stack):
#			if stack_element not in global_stack:
#				list_of_changes.append(stack_element)
#			else:
#				break
#		while len(list_of_changes)!=0:
#			global_stack.append(list_of_changes.pop())
#		f = open(var.global_destination+project_name+"/stack.txt","wb")
#		pickle.dump(global_stack,f)
#		f.close()


def del_last_commit(username,project_name,branch_name):
	global_stack = sc.load_g(project_name,branch_name)
	local_stack = sc.load_l(username, project_name,branch_name,branch_name)
	if local_stack in global_stack:
		print("невозможно удалить последний коммит, обратитесь к администратору")
		return
	else:
		print("вы уверены, что хотите удалить последний коммит?(д/н)")
		if input().lower() in ["да","д","yes","y"]:
			local_stack = local_stack[:-1]
			sc.dump_l(username,project_name,local_stack,branch_name)
			print("удаление прошло успешно")
			return 0




def make_project(username,project_name):
	try:
		os.mkdir(var.global_destination+project_name+'/')
	except:
		print("Такое название уже есть, назвать по-другому или удалить проект с данным именем?\n1-выбрать другое имя;\n2-создать заново;")
		while 1:
			if int(input(">> ")) == 1:
				new_project_name = input("введите новое название проекта\n")
				make_project(username,new_project_name)
				return 0
			elif int(input(">> ")) == 2:
				del_project(username, project_name)
				return 0			
	os.mkdir(var.global_destination+project_name+'/' + 'master')	
	os.chdir(var.global_destination+project_name+'/' + 'master')
	global_stack = sc.make_stack(username,project_name)
	f = open(".stack.txt","wb")
	pickle.dump(global_stack,f)
	f.close()
	local_stack = global_stack
	try:
		os.mkdir(var.users_destination+"/"+username+"/"+project_name+ '/')
	except:
		os.chdir(var.users_destination+"/"+username+"/")
		os.rename(project_name, project_name+"("+datetime.now().isoformat().split("T")[0]+"_"+datetime.now().isoformat().split("T")[1].split(".")[0]+")")
		os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/")

	os.mkdir(var.users_destination+"/"+username+"/"+project_name+ '/' + 'master')
	os.chdir(var.users_destination+"/"+username+"/"+project_name +'/' + 'master')
	f = open(".stack.txt","wb")
	pickle.dump(local_stack,f)
	f.close()
	#Добавление прав для пользователя
	os.chdir(var.administration)
	f = open('users_rights_for_projects.txt', 'rb')
	user_rights = pickle.load(f)
	f.close()
	users_for_add = {project_name:{'master':['admin', username]}}
	user_rights.update(users_for_add)
	f = open('users_rights_for_projects.txt', 'wb')
	pickle.dump(user_rights, f)
	f.close()
	'''
	#Добавление шаблона для запросов
	f = open('users_requests.txt', 'rb')
	user_requests = pickle.load(f)
	f.close()
	print(user_requests)
	user_requests.update({username:[]})
	print(user_requests)
	f = open('users_requests.txt', 'wb')
	pickle.dump(user_requests, f)
	f.close()
	'''
	return 0
    
def show_com_username(username, project_name, num):
	if not uc.have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	dirs_in_user = os.listdir(var.users_destination+username)
	isEmpty = True
	for dir_in_user in dirs_in_user:
		isEmpty = False
		if os.path.isdir(var.users_destination+username+'/'+dir_in_user+'/') == True and project_name == dir_in_user:
			path_to_project = var.users_destination + username + '/' + project_name + '/'
			os.chdir(path_to_project)
			f = open('stack.txt', 'rb')
			stack = pickle.load(f)
			print('Изменения в проекте', project_name, 'были сделаны пользователем', stack[num]['user'])
			f.close()
			return stack[num]['user']
	if isEmpty:
		print('В VCS ещё не зарегистрирован ни один пользователь')
		return
def show_com_date_time(username, project_name, num):
	if not uc.have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	dirs_in_user = os.listdir(var.users_destination+username)
	isEmpty = True
	for dir_in_user in dirs_in_user:
		isEmpty = False
		if os.path.isdir(var.users_destination+username+'/'+dir_in_user+'/') == True and project_name == dir_in_user:
			path_to_project = var.users_destination + username + '/' + project_name + '/'
			os.chdir(path_to_project)
			f = open('stack.txt', 'rb')
			stack = pickle.load(f)
			print('Проект ', project_name, 'был изменён', stack[num]['date-time'], 'пользователем', stack[num]['user'])
			f.close()
			return stack[num]['date-time']
	if isEmpty:
		print('В VCS ещё не зарегистрирован ни один пользователь')
		return
def show_commit(username, project_name, num):
	if not have_user_some_lvl_of_rights(username,project_name):
		print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		return
	dirs_in_user = os.listdir(var.users_destination + username)
	if os.path.exists(var.users_destination + username + '/' + project_name + '/'):
		path_to_project = var.users_destination + username + '/' + project_name + '/'
		os.chdir(path_to_project)
		f = open('stack.txt', 'rb')
		stack = pickle.load(f)
		f.close()
		if len(stack) < num:
			print('Коммита с таким номером нет!')
			return
		elif len(stack) == 1:
			print('Коммит пуст!')
			return
		print('Изменения в проекте', project_name, 'были сделаны ', stack[num]['date-time'])
		print()
		print('Изменения:')
		print()
		isSmthChange = False
		for change in stack[num]['changes']: # ['changes'][1:] -> Error: unhashable type: 'slice'
			isSmthChange = True
			print(stack[num]['changes'][change][0], change)
			if change[0] == '+' or change[0] == '...': # Если файл добавлен или изменён
				if stack[num]['changes'][change][0] == '+' or stack[num]['changes'][change][0] == '-':
					for line_in_change in stack[num]['changes'][change][1]:
						if line_in_change[0] == '+' or line_in_change[0] == '-':
							print('\t  ', stack[num]['changes'][change][0], stack[num]['changes'][change][1])
						else:
							print('\t  ', stack[num]['changes'][change][0], stack[num]['changes'][change][1],'->', stack[num]['changes'][change][2])
			else:	# Если файл удалён
				print('-', change)
	else:
		if not os.path.exists(var.users_destination + username + '/'):
			print('В VCS нет пользователя', username)
		else:
			print('У пользователя', username, 'нет проекта с именем', project_name)

		return

def show_not_pushed(username,project_name,branch_name):
	if not have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	global_stack = sc.load_g(project_name,branch_name)
	local_stack = sc.load_l(username,project_name,branch_name)
	list_of_changes = []
	for stack_element in reversed(local_stack):
		if stack_element not in global_stack:
			list_of_changes.append(stack_element)
		else:
			break
	print(list_of_changes)
	return list_of_changes

def del_couple_commits(username,project_name,branch_name):
	if not have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	local_stack = sc.load_l(username,project_name,branch_name)
	list_of_changes = show_not_pushed(username,project_name)
	pushed_commits = []
	for stack_element in reversed(local_stack):
		if stack_element not in list_of_changes:
			pushed_commits.append(stack_element)
	sc.dump_l(username,project_name,pushed_commits,branch_name)
################################################	КОММАНДЫ ДЛЯ ПРАВ	################################################	
def add_users_to_prj(username, project_name):
	if not have_user_high_lvl_of_rights(username, project_name, 'master'):
		print('Вы не обладаете достаточным уровнем доступа для выполнения этой команды')
		return
	os.chdir(var.administration)
	#############################
	while 1:
		print('Вы хотите добавить новых пользователей в весь проект? 1 - да; 2 - нет; 3 - выход')
		while 1:
			try:
				choice = int(input())
				if choice in [1, 2, 3]:
					break
				else:
					print('Такого варианта нет. Пожалуйста, повторите ввод.')
			except:
				print('Ошибка. Пожалуйста, повторите ввод.')
		if choice == 3:
			print('Программа добавления новых пользователей в проект', project_name, 'была завершена')
			return
		print('Список пользователей:')
		f = open('users.txt', 'rb')
		users = pickle.load(f)
		f.close()
		f = open('users_rights_for_projects.txt', 'rb')
		users_rights = pickle.load(f)
		f.close()
		if choice == 2:
			print('Ветки проекта', project_name + ':')
			for cur_branch in users_rights[project_name].keys():
				print('\t', cur_branch)
			while 1:
				print('Выберите ветку, в которую вы хотите добавить новых пользователей:')
				branch = input()
				if branch in users_rights[project_name].keys():
					print('Выбрана ветка', branch)
					break
		for user in users.keys():
			if user != 'admin' and user != username:
				print('\t' + user)
		if choice == 1:
			print('Введите через пробел имена пользователей, которых вы хотите добавить в проект', project_name+':')
			
		else:
			print('Введите через пробел имена пользователей, которых вы хотите добавить в ветку', branch, 'проекта', project_name+':')
		print('>', end=' ')
		users = input().split()  # users это ['Dima', 'Denis']
		for user in users:  # Удаляем повторяющихся юзеров
			if users.count(user) != 1:
				while users.count(user) != 1:
					users.remove(user)
		if 'admin' in users:
			users.remove('admin')
		if username in users:
				users.remove(username)
		f = open('users.txt', 'rb')
		registered_users = pickle.load(f)
		f.close()
		users_for_add = []		

		for user in users:
			if user in registered_users.keys():
				users_for_add.append(user)
			else:
				print('Пользователь ' + user + ' не зарегистрирован в vcs')

		#users_for_add [dima, denis]
		#users_for_add_choice_1 {username: { master: [ [project_owner1, prj_1], [project_owner22, prj_2] ]; branch1: [project3_owner, prj_3] }
		if choice == 1:
			users_for_add_choice_1 = {}
			isSomeoneForAdd = False
			for user in users_for_add:
				users_for_add_choice_1[user] = {}
				for cur_branch in users_rights[project_name].keys():
					users_for_add_choice_1[user][cur_branch] = []
					if  user not in users_rights[project_name][cur_branch]:
						#users_rights[cur_branch].append(user)
						users_for_add_choice_1[user][cur_branch].append([username, project_name])
						isSomeoneForAdd = True
			if not isSomeoneForAdd:
				print('Все введённые пользователи уже добавлены в проект ' + project_name)
				continue
			print('Вы собираетесь сделать следующие изменения в проекте:')
			for user in users_for_add:
				print('Добавить пользователя', user, 'в:')
				for cur_branch in users_for_add_choice_1[user].keys():
					print('\tВетка -', cur_branch)
			while 1:
				try:
					print('Для продолжения нажмите 1, для отмены - 2')
					choice = int(input())
					if choice == 1 or choice == 2:
						break
					else:
						print('Такого варианта нет. Пожалуйста, повторите ввод.')
				except:
					print('Ошибка. Пожалуйста, повторите ввод')
			if choice == 1:
				f = open('users_requests.txt', 'rb')
				users_rec = pickle.load(f)
				f.close()
				if user not in users_rec.keys():
					users_rec[user] = {}
				for user in users_for_add:
					for branch in users_for_add_choice_1[user].keys():
						if branch not in users_rec[user].keys():
							users_rec[user][branch] = []
						users_rec[user][branch].append( [username, project_name] )
				f = open('users_requests.txt', 'wb')
				pickle.dump(users_rec, f)
				f.close()
				print('Добавление было успешно завершено')
			else:
				print('Добавление было прервано')
		else:
			for user in users_for_add: 
				if user in users_rights[project_name][branch]:
					print('Пользователь', user, 'уже состоит в ветке', branch)
					users_for_add.remove(user)
			print('Ваш выбор:')
			for user in users_for_add:
				print('\t', user)
			while 1:
				try:
					print('Для продолжения нажмите 1, для отмены - 2')
					choice = int(input())
					if choice == 1 or choice == 2:
						break
					else:
						print('Такого варианта нет. Пожалуйста, повторите ввод.')
				except:
					print('Ошибка. Пожалуйста, повторите ввод')
			if choice == 1:
				f = open('users_requests.txt', 'rb')
				users_rec = pickle.load(f)
				f.close()
				for user in users_for_add:
					users_rec[user][branch].append([username, project_name])
				f = open('users_requests.txt', 'wb')
				pickle.dump(users_rec, f)
				f.close()
				print('Добавление было успешно завершено')
			else:
				print('Добавление было прервано')
				#{username: { master: [ [project_owner1, prj_1], [project_owner22, prj_2] ]; branch1: [project3_owner, prj_3] }
				#{project: { master: [ admin, ivan, dima ]; branch1: [admin, ivan] }
def del_users_from_prj(username, project_name):
	if not have_user_high_lvl_of_rights(username, project_name):
		print('Вы не обладаете достаточным уровнем доступа для выполнения этой команды')
		return
	os.chdir(var.administration)
	while 1:
		print('Вы хотите удалить пользователей из всего проекта? 1 - да; 2 - нет; 3 - выход')
		while 1:
			try:
				choice = int(input())
				if choice in [1, 2, 3]:
					break
				else:
					print('Такого варианта нет. Пожалуйста, повторите ввод.')
			except:
				print('Ошибка. Пожалуйста, повторите ввод.')
		if choice == 3:
			print('Программа удаления пользователей из проекта', project_name, 'была завершена')
			return
		f = open('users_rights_for_projects.txt','rb')
		users_rights = pickle.load(f)
		f.close()
		isSomeoneForDel = False
		for branch in users_rights[project_name].keys():
			if len(users_rights[project_name][branch]) > 2:
				isSomeoneForDel = True
		if not isSomeoneForDel:
			print('Вы являетесь единственным участником проекта. Команда удаления участников из проекта '+project_name+' была прервана.')
			continue
		print('Участники проекта:')
		list_with_users_in_prj = []
		for branch in users_rights[project_name].keys():
			for user in users_rights[project_name][branch]:
				if user not in list_with_users_in_prj:
					list_with_users_in_prj.append(user)
		for user in list_with_users_in_prj:
			print('\t', user)
		if choice == 1:
			print('Введите через пробел имена пользователей, которых вы хотите удалить из проекта', project_name+':')
			print('>', end=' ')
			users = input().split()  # users это ['Dima', 'Denis']
			for user in users:  # Удаляем повторяющихся юзеров
				if users.count(user) != 1:
					while users.count(user) != 1:
						users.remove(user)
			if 'admin' in users:
				users.remove('admin')
			if username in users:
				users.remove(username)
			f = open('users.txt', 'rb')
			registered_users = pickle.load(f)
			f.close()
			for user in users:
				if user not in registered_users.keys():
					print('Пользователь ' + user + ' не зарегистрирован в vcs')
					users.remove(user)
					continue
					isSomeoneForDel = False
					for branch in users_rights[project_name].keys():
						if user in users_rights[project_name][branch]:
							isSomeoneForDel = True
							break
					if not isSomeoneForDel:
						print('Пользователь', user, 'не является участником проекта', project_name)
						users.remove(user)
			print('Ваш выбор:')
			for user in users:
				print('\t', user)
			while 1:
				try:
					print('Для продолжения нажмите 1, для отмены - 2')
					choice = int(input())
					if choice == 1 or choice == 2:
						break
					else:
						print('Такого варианта нет. Пожалуйста, повторите ввод.')
				except:
					print('Ошибка. Пожалуйста, повторите ввод')
			if choice == 1:
				for branch in users_rights[project_name].keys():
					if user in users_rights[project_name][branch]:
						users_rights[project_name][branch].remove(user)
				f = open('users_rights_for_projects.txt', 'wb')
				pickle.dump(users_rights, f)
				f.close()
				print('Удаление прошло успешно')
			else:
				print('Удаление было прервано')
				continue
			#{username: { master: [ [project_owner1, prj_1], [project_owner22, prj_2] ]; branch1: [project3_owner, prj_3] }
			#{project: { master: [ admin, ivan, dima ]; branch1: [admin, ivan] }
		else:
			for branch in users_rights[project_name].keys():
				if len(users_rights[project_name][branch]) == 2:
					continue
				print('Ветка -', branch)
				for user in users_rights[project_name][branch][2:]:
					print('\t', user)
			while 1:
				print('Выберите ветку, из которой вы хотите удалить пользователей:')
				branch = input()
				if branch in users_rights[project_name].keys():
					print('Выбрана ветка', branch)
					break
			print('Введите через пробел имена пользователей, которых вы хотите удалить из ветки', branch, 'проекта', project_name+':')
			print('>', end=' ')
			users = input().split()  # users это ['Dima', 'Denis']
			for user in users:  # Удаляем повторяющихся юзеров
				if users.count(user) != 1:
					while users.count(user) != 1:
						users.remove(user)
			if 'admin' in users:
				users.remove('admin')
			if username in users:
				users.remove(username)
			f = open('users.txt', 'rb')
			registered_users = pickle.load(f)
			f.close()	
			for user in users:
				if user not in registered_users.keys():
					print('Пользователь ' + user + ' не зарегистрирован в vcs')
					users.remove(user)
					continue
				if user not in users_rights[project_name][branch]:
					print('Пользователь', user, 'не является участником ветки', branch)
					users.remove(user)
					continue
				users_rights[project_name][branch].remove(user)

			print('Ваш выбор:')
			for user in users:
				print('\tВетка -', branch, 'пользователь -', user)
			while 1:
				try:
					print('Для продолжения нажмите 1, для отмены - 2')
					choice = int(input())
					if choice == 1 or choice == 2:
						break
					else:
						print('Такого варианта нет. Пожалуйста, повторите ввод.')
				except:
					print('Ошибка. Пожалуйста, повторите ввод')
			if choice == 1:
				f = open('users_rights_for_projects.txt', 'wb')
				pickle.dump(users_rights, f)
				f.close()
				print('Удаление прошло успешно')
			else:
				print('Удаление было прервано')
				continue
				#{username: { master: [ [project_owner1, prj_1], [project_owner22, prj_2] ]; branch1: [project3_owner, prj_3] }
				#{project: { master: [ admin, ivan, dima ]; branch1: [admin, ivan] }
def check_users_requests(username):
	os.chdir(var.administration)
	#{username: { master: [ [project_owner1, prj_1], [project_owner22, prj_2] ]; branch1: [project3_owner, prj_3] }
	#{project: { master: [ admin, ivan, dima ]; branch1: [admin, ivan] }
	try:
		f = open('users_requests.txt', 'rb')
	except:
		cnf.create_necessary_files()
		f = open('users_requests.txt', 'rb')
	users_requests = pickle.load(f)
	f.close()
	if username in users_requests.keys():
		print('У вас есть новые приглашения в проект/проекты\n')
		counter = 0
		for branch in users_requests[username].keys():
			for requset in users_requests[username][branch]:
				counter += 1
				print('\t',str(counter)+':', requset[0], 'пригласил вас в проект', requset[1], 'в ветку', branch)
		while 1:
			try:
				answer = [int(i) for i in input('Введите через пробел номера проектов, в которые вы вступите(все остальные приглашения будут удалены)\n>').split()]
				break
			except:
				print('Ошибка ввода. Пожалуйста, введите корректные номера приглашений')
		for i in answer:
			if i < 1 or i > counter:
				answer.remove(i)
		counter = 0
		f = open('users_rights_for_projects.txt','rb')
		users_rights = pickle.load(f)
		f.close()
		print('Ваш выбор:')
		for branch in users_requests[username].keys():
			for request in users_requests[username][branch]:
				counter += 1
				if counter in answer:
					print('\tВладелец проекта:', request[0], '\tНазвание проекта:', request[1], '\tВетка:', branch)
		while 1:
			try:
				choice = int(input('Для продолжения нажмите 1, для отмены - 0\n>'))
				if choice in [0, 1]:
					break
				else:
					print('Такой команды нет. Пожалуйста, повторите ввод.')
			except:
				print('Ошибка ввода. Пожалуйста, повторите ввод ещё раз, следуя инструкциям.')
		if choice:
			counter = 0
			for branch in users_requests[username].keys():
				for request in users_requests[username][branch]:
					counter += 1
					print('request ==',requset)
					if counter in answer:
						users_rights[request[1]][branch].append(username)
			del(users_requests[username])
			f = open('users_requests.txt','wb')
			pickle.dump(users_requests, f)
			f.close()
			f = open('users_rights_for_projects.txt', 'wb')
			pickle.dump(users_rights, f)
			f.close()
			print('Обработка приглашений завершена')
		if make_project_local(username, request[1],branch) != 0:
				intf.pre_pull(username,request[1],branch)
	else:
		print('У вас нет новых приглашений в проекты')
def have_user_high_lvl_of_rights(username, project_name, branch):
	os.chdir(var.administration)
	f = open('users_rights_for_projects.txt', 'rb')
	obj = pickle.load(f)
	f.close()
	if branch == 'master':
		if obj[project_name]['master'][0] != username and obj[project_name]['master'][1] != username:
			print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
			return 0
		else:
			return 1
	else:
		if obj[project_name][branch][2] != username:
			print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
			return 0
		else:
			return 1
def have_user_some_lvl_of_rights(username, project_name, branch):
	#{project: { master: [ admin, ivan, dima ]; branch1: [admin, ivan] }
	os.chdir(var.administration)
	f = open('users_rights_for_projects.txt', 'rb')
	obj = pickle.load(f)
	f.close()
	print(obj)
	if username not in obj[project_name][branch]:
		print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		return 0
	else:
		return 1
########################################################################################################################
'''
def copy_from_GL_to_LC(username, project_name):
	os.mkdir(var.local_destination+username + '/' + project_name+'/')
	os.chdir(var.local_destination+username + '/' + project_name+'/')
	local_stack = sc.make_stack(username,project_name)
	f = open("stack.txt","wb")
	pickle.dump(local_stack,f)
	f.close()
	commit(username, project_name)
	pre_push(username, project_name)
'''

def make_project_local(username, project_name,branch_name):
	global_stack=sc.load_g(project_name,branch_name)
	if len(global_stack) == 0:
		return 0
	try:
		os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/")
	except:
		del_dir(var.users_destination+"/"+username+"/"+project_name)
		os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/")
	os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/"+branch_name+"/")	
	f = open(var.users_destination+username+"/"+project_name+"/"+branch_name+"/.stack.txt","wb")
	pickle.dump([global_stack[0]],f)
	f.close()
	return 

def make_branch(username,project_name,branch_name):
	stack_struct = sc.make_stack(username,project_name)
	gl_path = var.global_destination + '/' + project_name + '/' + branch_name
	try:
		os.mkdir(gl_path)
	except:
		print("такое название уже есть, назвать по-другому или удалить ветку с данным именем?\n1-выбрать другое имя;\n2-удалить ветку;")
		while 1:
			if int(input(">> ")) == 1:
				new_branch_name = input("введите новое название ветки\n")
				make_branch(username,project_name,new_branch_name)
				return 0
			elif int(input(">> ")) == 2:
				del_branch(username, project_name, branch_name)
	lc_path = var.users_destination + username + '/' + project_name+'/'+branch_name
	f = open(gl_path + '/' + '.stack.txt','wb')
	pickle.dump(stack_struct,f)
	f.close()
	try:			
		os.mkdir(lc_path)
	except:
		os.chdir(var.users_destination+"/"+username+"/"+project_name)
		os.rename(branch_name, branch_name+"("+datetime.now().isoformat().split("T")[0]+"_"+datetime.now().isoformat().split("T")[1].split(".")[0]+")")
		os.mkdir(lc_path)
	f = open(lc_path + '/' + '.stack.txt','wb')
	pickle.dump(stack_struct,f)
	f.close()
	os.chdir(var.administration)
	f = open('users_rights_for_projects.txt','rb') 
	st = pickle.load(f) 
	f.close() 
	st[project_name][branch_name] = ['admin', st[project_name]['master'][1], username] 
	f = open('users_rights_for_projects.txt', 'wb') 
	pickle.dump(st, f) 
	f.close()


def del_dir(_dir):
	os.chdir(_dir)
	py_dtour.go_up()
	directory = _dir.split("/")[-1]
	os.system("rm -Rf "+directory)


def del_project(username, project_name):
	if have_user_high_lvl_of_rights(username, project_name, "master"):
			print("Вы уверены, что хотите удалить проект </"+project_name+"/>?")
			if input(">> ").lower() in ["да", "д", "yes", "y"]:
				del_dir(var.global_destination+"/"+project_name)
			else: 
				return	


def del_branch(username, project_name, branch_name):
	if have_user_high_lvl_of_rights(username, project_name, branch_name):
			print("Вы уверены, что хотите удалить ветку </"+branch_name+"/> в проекте </"+project_name+"/>?")
			if input(">> ").lower() in ["да", "д", "yes", "y"]:
				del_dir(var.global_destination+"/"+project_name+"/"+branch_name)
			else: 
				return	

def merge(username,project_name,branch_name):
	br_dest = var.users_destination + username + '/' + project_name + '/' + branch_name
	master_dest = var.users_destination + username + '/' + project_name + '/' + 'master'
	changes = chingl.global_changes(username,project_name,branch_name,master_dest,br_dest)

	for path in changes.keys():
		element = path.split(branch_name)[-1]
		if changes[path][0] == "+":
			if os.path.isdir(br_dest + '/' + element):
				try:
					os.chdir(master_dest)
					os.mkdir(element)	
				except:
					continue
			else:		
				ovf.write_file(master_dest + "/" + element,changes[path][-1])	
		elif changes[path][0] == "...":
			f_new = open(master_dest + '/' + element[:-4] + '(branch_' + branch_name + ').txt','w')
				#(date_time_' + datetime.now().isoformat().split("T")[0]+"_"+datetime.now().isoformat().split("T")[1].split(".")[0] + ').txt','w')
			f_br = open(br_dest + element,'r')
			string = [line for line in f_br]
			f_mr = open(master_dest + element,'r')
			string_mr = [line for line in f_mr]
			flag = True
			num = 1
			for line in range(max(len(string),len(string_mr))):
				if line+1 not in changes[path][1].keys():
					f_new.write(string[line])
				elif (changes[path][1][line+1][0] == '+') or (changes[path][1][line+1][0] == '...' and changes[path][1][line+1][1] == '\n'):
					f_new.write(changes[path][1][line+1][2])
				else:
					f_new.write(changes[path][1][line+1][2])
					flag = False
			f_new.close()
			f_br.close()
			f_mr.close()
			if flag == True:
				os.remove(master_dest + "/" + element)	
				os.chdir(master_dest)
				os.rename(element[2:-4] + '(branch_' + branch_name + ').txt',element.split('/')[-1])
			
	intf.commit(username,project_name,'master')
	intf.pre_push(username,project_name,'master')
