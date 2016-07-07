import pickle
import variables as var
from datetime import datetime


def make_stack(username,project_name):
	stack = []
	element ={}
	element["user"] = username
	element["date-time"] = datetime.now()
	path_to_stack = "/"+"/".join([project_name,"stack.txt"])
	element["changes"] = {path_to_stack:"added"}
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