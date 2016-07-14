import os
import pickle
import variables as var
import stack_commands as sc
import py_detour as py_dtour
import find_changes as find_ch
import changes_in_global as chingl
from datetime import datetime
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

def check_updates(username,project_name):
	global_stack = sc.load_g(project_name)
	
	local_stack = sc.load_l(username,project_name)
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


def del_last_commit(username,project_name):
	global_stack = sc.load_g(project_name)
	local_stack = sc.load_l(username, project_name)
	if local_stack in global_stack:
		print("невозможно удалить последний коммит, обратитесь к администратору")
		return
	else:
		print("вы уверены, что хотите удалить последний коммит?(д/н)")
		if input().lower() in ["да","д","yes","y"]:
			local_stack = local_stack[:-1]
			sc.dump_l(username,project_name,local_stack)
			print("удаление прошло успешно")
			return 0




def make_project(username,project_name):
	try:
		os.mkdir(var.global_destination+project_name+'/')
	except:
		print("такое название уже есть, назвать по-другому или создать заново проект с данным именем?\n1-выбрать другое имя;\n2-создать заново;")
		while 1:
			print("ha")
			try:
				if int(input()) == 1:
					new_project_name = input("введите новое название проекта\n")
					make_project(username,new_project_name)
					return 0
				elif int(input()) == 2:
					# shutil.rmtree('/folder_name')
					shutil.rmtree(var.global_destination+project_name)
					try:
						shutil.rmtree(var.users_destination+"/"+username+"/"+project_name+"/")
						make_project(username,project_name)
						return 0
					except:
						print("error!")
						return 1
						pass
					break
			except:
				pass

	os.chdir(var.global_destination+project_name+'/')
	global_stack = sc.make_stack(username,project_name)
	f = open("stack.txt","wb")
	pickle.dump(global_stack,f)
	f.close()
	local_stack = global_stack
	try:
		os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/")
	except:
		shutil.rmtree(var.users_destination+"/"+username+"/"+project_name+"/")
	os.chdir(var.users_destination+"/"+username+"/"+project_name+"/")
	f = open("stack.txt","wb")
	pickle.dump(local_stack,f)
	f.close()
	#Добавление прав для пользователя
	os.chdir(var.administration)
	f = open('users_rights_for_projects.txt', 'rb')
	user_rights = pickle.load(f)
	f.close()
	users_for_add = {project_name:['admin', username]}
	user_rights.update(users_for_add)
	f = open('users_rights_for_projects.txt', 'wb')
	pickle.dump(user_rights, f)
	f.close()
	f = open('users_rights_for_projects.txt', 'wb')
	pickle.dump(user_rights, f)
	f.close()
	#Добавление шаблона для запросов
	f = open('users_requests.txt', 'rb')
	user_requests = pickle.load(f)
	f.close()
	user_requests.update({username:[]})
	f = open('users_requests.txt', 'rb')
	pickle.dump(user_requests, f)
	f.close()
	return 0
    
def show_com_username(username, project_name, num):
	if not have_user_some_lvl_of_rights(username,project_name):
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
	if not have_user_some_lvl_of_rights(username,project_name):
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

def show_not_pushed(username,project_name):
	if not have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	global_stack = sc.load_g(project_name)
	local_stack = sc.load_l(username,project_name)
	list_of_changes = []
	for stack_element in reversed(local_stack):
		if stack_element not in global_stack:
			list_of_changes.append(stack_element)
		else:
			break
	print(list_of_changes)
	return list_of_changes

def del_couple_commits(username,project_name):
	if not have_user_some_lvl_of_rights(username,project_name):
		 print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		 return
	local_stack = sc.load_l(username,project_name)
	list_of_changes = show_not_pushed(username,project_name)
	pushed_commits = []
	for stack_element in reversed(local_stack):
		if stack_element not in list_of_changes:
			pushed_commits.append(stack_element)
	sc.dump_l(username,project_name,pushed_commits)
################################################	КОММАНДЫ ДЛЯ ПРАВ	################################################	
def add_users_to_prj(username, project_name):
	if not have_user_high_lvl_of_rights(username, project_name):
		print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		return
	os.chdir(var.administration)
	print('Список пользователей:')
	f = open('users.txt', 'rb')
	users = pickle.load(f)
	f.close()
	for user in users.keys():
		if user != 'admin' and user != username:
			print('\t' + user)
	print('Введите через пробел имена пользователей, которых вы хотите добавить в проект:')
	print('>', end=' ')
	users = input().split()  # users это ['Dima', 'Denis']
	for user in users:  # Удаляем повторяющихся юзеров
		if users.count(user) != 1:
			while users.count(user) != 1:
				users.remove(user)
	if 'admin' in users:
		users.remove('admin')
	f = open('users.txt', 'rb')
	registered_users = pickle.load(f)
	f.close()
	users_for_add = []
	for user in users:
		if user in registered_users.keys():
			users_for_add.append(user)
		else:
			print('Пользователь ' + user + ' не зарегистрирован в vcs')
	if len(users_for_add) == 0:
		print('Ни один, из введённых пользователей, не может быть добавлен в проект ' + project_name)
		return
	print('Список пользователей для добавления в проект:')
	for user in users:
		print('\t', user, end=' ')
	print()
	print('Для окончательного добавления нажмите 1, для отмены - 0')
	choice = int(input())
	if choice:
		f = open('users_requests.txt', 'rb')
		requests = pickle.load(f)
		f.close()
		for user in users_for_add:
			if user not in requests.keys():
				requests[user] = []
			if project_name not in requests[user]:
				requests[user].append([username, project_name])
			else:
				print('Вы уже отправляли приглашение пользователю', user, 'на присоединение к проекту')
		f = open('users_requests.txt', 'wb')
		requests = pickle.dump(requests, f)
		f.close()
	else:
		print('Запрос на приглашение новых пользователей был отменён')
		return
def del_users_from_prj(username, project_name):
    if not have_user_high_lvl_of_rights(username, project_name):
        print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
        return
    f = open('users_rights_for_projects.txt','rb')
    list_with_users_in_prj = pickle.load(f)
    f.close()
    if len(list_with_users_in_prj[project_name]) == 2:
        print('Вы являетесь единственным участником проекта. Команда удаления участников из проекта '+project_name+' была прервана.')
        return
    print('Текущий список участников проекта:')
    for user in list_with_users_in_prj[project_name][2:]:
        print('\t', user)
    print('Введите через пробел имена пользователей, которых вы хотите удалить из проекта:')
    print('>', end=' ')
    users = input().split() # users это ['Dima', 'Denis']
    for user in users: # Удаляем повторяющихся юзеров
        if users.count(user) != 1:
            while users.count(user) != 1:
                users.remove(user)
    if 'admin' in users:
        users.remove('admin')
    if username in users:
        users.remove(username)
    users_for_del = []
    for user in users:
        if user in list_with_users_in_prj[project_name]:
            users_for_del.append(user)
        else:
            print('Пользователь ' + user + ' не зарегистрирован в vcs')
    if len(users_for_del) == 0:
        print('Ни один, из введённых пользователей, не может быть удалён из проекта '+project_name)
        return
    print('Список пользователей для удаления из проекта:')
    for user in users:
        print('\t',user, end=' ')
    print('\nДля окончательного удаления нажмите 1, для отмены - 0')
    choice = int(input())
    if choice:
        for user in list_with_users_in_prj[project_name]:
            if user in users_for_del:
                list_with_users_in_prj[project_name].remove(user)
    else:
        print('Запрос на удаление пользователей был отменён')
        return
    f = open('users_rights_for_projects.txt','wb')
    pickle.dump(list_with_users_in_prj, f)
    f.close()
    print('Удаление пользователей прошло успешно')
def check_users_requests(username):
    os.chdir(var.administration)
    f = open('users_requests.txt', 'rb')
    users_requests = pickle.load(f)
    f.close()
    if username in users_requests.keys():
        print('У вас есть новые приглашения в проект/проекты\n')
        counter = 0
        for requset in users_requests[username]:
            counter += 1
            print('\t',str(counter)+':', requset[0], 'пригласил вас в проект', requset[1])
        while 1:
            try:
                answer = [int(i) for i in input('Введите через пробел номера проектов, в которые вы вступите(все остальные приглашения будут удалены)\n>').split()]
                break
            except:
                print('Ошибка ввода. Пожалуйста, введите корректные номера проектов')
        for i in answer:
            if i < 1 or i > counter:
                answer.remove(i)
        counter = 0
        f = open('users_rights_for_projects.txt','rb')
        users_rights = pickle.load(f)
        f.close()
        print('Ваш выбор:')
        for requset in users_requests[username]:
            counter += 1
            if counter in answer:
                print('\tВладелец проекта:', requset[0], '\tНазвание проекта:', requset[1])
        while 1:
            try:
                choice = int(input('Для продолжения нажмите 1, для отмены - 0\n>'))
                break
            except:
                print('Ошибка ввода. Пожалуйста, повторите ввод ещё раз, следуя инструкциям.')
        if choice:
            counter = 0
            for requset in users_requests[username]:
                counter += 1
                print('request ==',requset)
                if counter in answer:
                    users_rights[requset[1]].append(username)
                    users_requests[username].remove(requset)
            print(users_requests)
            f = open('users_requests.txt','wb')
            pickle.dump(users_requests, f)
            f.close()
            f = open('users_rights_for_projects.txt', 'wb')
            pickle.dump(users_rights, f)
            f.close()
            print('Обработка приглашений завершена')
        ################################################### вставить сюда ф-цию клпирования проекта из глобала в локал
    else:
        print('У вас нет новых приглашений в проекты')
def have_user_high_lvl_of_rights(username, project_name):
	os.chdir(var.administration)
	f = open('users_rights_for_projects.txt', 'rb')
	obj = pickle.load(f)
	f.close()
	if obj[project_name][0] != username and obj[project_name][1] != username:
		print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
		return 0
	else:
		return 1
def have_user_some_lvl_of_rights(username, project_name):
    os.chdir(var.administration)
    f = open('users_rights_for_projects.txt', 'rb')
    obj = pickle.load(f)
    f.close()
    if username not in obj[project_name]:
        print('Этот пользователь не обладает достаточным уровнем доступа для выполнения этой команды')
        return 0
    else:
        return 1
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

def make_project_local(username, project_name):
	global_stack=sc.load_g(project_name)
	if global_stack == 0:
		return 0
	try:
		os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/")
	except:
		return
	f = open(var.users_destination+username+"/"+project_name+"/stack.txt","wb")
	pickle.dump([global_stack[0]],f)
	f.close()
	return 
