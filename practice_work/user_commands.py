import shutil
import stack_commands as sc
import os
import variables as var
import pickle
# def check_updates(username):
# 	for





def commit(username):
	stack = get_stack()
	stack.append(updates)
	f = open("stack.txt","wb")
	pickle.dump(stack,f)
	f.close()



def push(username):
	check = check_updates()
	if check:
		f = open(var.global_destination+project_name+"/stack.txt","rb")
		global_stack = pickle.load(f)
		f.close()
		f = open()



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
						shutil.rmtree(var.users_destination+"/"+username+"/"+project_name)
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
	return 0


