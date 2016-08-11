import ssh_client as ssc
import pickle
import getpass
import os
import variables as var
import hashlib as hl
import user_commands as uc
import overwriting_files as of
transport = ssc.connect_transport()
ftp = ssc.connect_ftp(transport)
users = ssc.download_users(ftp)
ssc.exit_ftp(ftp)
ssc.exit_transport(transport)



def registration_form():
	new_username = input("введите имя нового пользователя: ")
	while 1:
	
		password = getpass.getpass("введите пароль для нового пользователя: ")
		if password == getpass.getpass("введите пароль повторно: "):
			break
		else:
			print("пароли не совпадают, введите заново\n")
	users[new_username] = hl.md5(password.encode()).hexdigest()
	os.mkdir(var.users_destination+"/"+new_username)
	ssc.upload_users(ftp,users)
	ssc.exit_ftp(ftp)
	ssc.exit_transport(transport)




def login():
	while 1:
		
		current_username = input("введите имя пользователя: ")
		if current_username not in users.keys():
			print("пользователь </"+current_username+ "/> еще не был  зарегистрирован")
			if input("хотите ли зарегистрировать нового пользователя?(д/н)\n").lower() in ["yes","да","y","д"]:
				registration_form()
		else:
			break
	while 1:
		current_password = hl.md5(getpass.getpass("введите пароль: ").encode()).hexdigest()
		if current_password == users[current_username]:
			try:
				os.chdir(var.users_destination + "/"+current_username+"/")
			except:
				os.mkdir(var.users_destination + "/"+current_username+"/")
				os.chdir(var.users_destination + "/"+current_username+"/")
			print(os.getcwd())
			print("ok")
			break
	return current_username
user = login()
project_name = input("введите название проекта\n")
uc.make_project(user,project_name)
# print("hey")
print("введите команду")
while 1:
	print(">>",end = "")
	inp = input()
	if inp == "commit":
		uc.commit(user,project_name)
	elif inp == "push":
		print()
		local_stack = ssc.load_l(user,project_name)
		global_stack = ssc.load_g(project_name)
		of.push(local_stack,global_stack,project_name)
	elif inp == "exit":
		break

# uc.commit(user,project_name)
# local_stack = ssc.load_l(user,project_name)
# global_stack = ssc.load_g(project_name,ftp)
# of.push(local_stack,global_stack,project_name)



