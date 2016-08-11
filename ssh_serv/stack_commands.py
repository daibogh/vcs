import pickle
import variables as var
from datetime import datetime

def make_stack(username,project_name):
	stack = []
	element ={}
	element["user"] = username
	element["date-time"] = datetime.now()
	path_to_stack = "/"+"/".join([project_name,"stack.txt"])
	element["changes"] = {path_to_stack:"+"}
	stack.append(element)
	return stack



# def load_g(project_name):
# 	f = open(var.global_destination+project_name+"/stack.txt","rb")
# 	global_stack = pickle.load(f)
# 	f.close()
# 	return global_stack

# def load_l(username,project_name):
# 	f = open(var.users_destination+username+"/"+project_name+"/stack.txt","rb")
# 	local_stack = pickle.load(f)
# 	f.close()
# 	return local_stack

# def dump_l(username,project_name,stack):
# 	f = open(var.users_destination+username+"/"+project_name+"/stack.txt","wb")
# 	pickle.dump(stack,f)
# 	f.close()
# 	return 0
# def dump_g(project_name,stack):
# 	f = open(var.global_destination+project_name+"/stack.txt","wb")
# 	pickle.dump(stack,f)
# 	f.close()
# 	return 0


# def load_stack():
# 	f = open(var.global_destination+"version_control.txt","rb")
# 	global_version_control = pickle.load(f)
# 	f.close()
# 	return global_version_control

# def dump_stack(stack):
# 	f = open(var.global_destination+"version_control.txt","wb")
# 	pickle.dump(stack,f)
# 	f.close()
