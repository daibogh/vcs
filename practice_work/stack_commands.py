import pickle
import variables as var
def load_stack():
	f = open(var.global_destination+"version_control.txt","rb")
	global_version_control = pickle.load(f)
	f.close()
	return global_version_control
def dump_stack(stack):
	f = open(var.global_destination+"version_control.txt","wb")
	pickle.dump(stack,f)
	f.close()