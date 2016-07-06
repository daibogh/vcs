import pickle
import getpass
import os
import variables as var
try:
	f = open("users.txt",'rb')
	users = pickle.load(f)
	f.close()
except:
	users = {"admin":"admin"}
	pass

def registration_form():
	new_username = input("введите имя нового пользователя: ")
	while 1:
	
		password = getpass.getpass("введите пароль для нового пользователя: ")
		if password == getpass.getpass("введите пароль повторно: "):
			break
		else:
			print("пароли не совпадают, введите заново\n")
	users[new_username] = password
	f = open("users.txt","wb")
	pickle.dump(users,f)
	f.close()




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
		current_password = getpass.getpass("введите пароль: ")
		if current_password == users[current_username]:
			try:
				os.chdir(var.destination + current_username+"/")
			except:
				os.mkdir(var.destination + current_username+"/")
				os.chdir(var.destination + current_username+"/")
			print(os.getcwd())
			print("ok")
			break
	return current_username

