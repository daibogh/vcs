import stack_commands as sc
import os
import variables as var
import pickle
# def check_updates(username):
# 	for





def commit(username):
	stack = get_stack()
	stack.append(updates)
	f = open("version_control.txt","wb")
	pickle.dump(stack,f)
	f.close()



def push(username):
	check = check_updates()
	if check:
		f = open(var.global_destination+project_name+"/global_control_version.txt","rb")
		global_stack = pickle.load(f)
		f.close()
		f = open()



def make_project(username,project_name):
	os.mkdir(var.global_destination+project_name+'/')
	os.chdir(var.global_destination+project_name+'/')
	global_stack = sc.make_stack(username,project_name)
	f = open("global_stack.txt","wb")
	pickle.dump(global_stack,f)
	f.close()
	local_stack = global_stack
	os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/")
	os.chdir(var.users_destination+"/"+username+"/"+project_name+"/")
	f = open("local_stack.txt","wb")
	pickle.dump(local_stack,f)
	f.close()


