import pickle
import variables as var
from datetime import datetime
import changes_in_global as chingl

def make_stack(username,project_name):
	stack = []
	element ={}
	element["user"] = username
	element["date-time"] = datetime.now()
	path_to_stack = "/"+"/".join([project_name,"stack.txt"])
	element["changes"] = {path_to_stack:"+"}
	stack.append(element)
	return stack

def load_stack():
	f = open(var.global_destination+"version_control.txt","rb")
	global_version_control = pickle.load(f)
	f.close()
	return global_version_control

def dump_stack(stack):
	f = open(var.global_destination+"version_control.txt","wb")
	pickle.dump(stack,f)
	f.close()

def add_commit(username,project_name):
	element = {}
	element["user"] = username
	element["date-time"] = datetime.now()
	element["changes"]=chingl.global_changes(username,project_name)
	if element["changes"]=={}:
		print("Не было внесено никаких изменений")
		return
	path_to_stack = var.users_destination+"stack.txt"
	f = open(path_to_stack,"rb")
	stack = pickle.load(f)
	stack.append(element)
	pickle.dump(stack,f)
	f.close()