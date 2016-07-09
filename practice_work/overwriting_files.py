import os
import variables as var
def push(local_stack,global_stack):
	temp_stack = []
	for element in reversed(local_stack):
		if element not in global_stack:
			temp_stack.append(element)
		else:
			break
	for element in temp_stack:
		changes = element["changes"]
		for path in changes.keys():
			if changes[path][0] == "...":
				overwrite_file(var.global_destination+"/"+path,changes[path][-1])
			elif changes[path][0] == "+":
				write_file(var.global_destination+"/"+path,changes[path][-1])
			elif changes[path][0] == "-":
				os.remove(global_destination+"/"+path)
def pull(local_stack,global_stack,username):
	temp_stack = []
	for element in reversed(global_stack):
		if element not in local_stack:
			temp_stack.append(element)
		else:
			break
	for element in temp_stack:
		changes = element["changes"]
		for path in changes.keys():
			if changes[path][0] == "...":
				overwrite_file(var.users_destination+"/"+username+"/"+path,changes[path][-1])
			elif changes[path][0] == "+":
				write_file(var.users_destination+"/"+path,changes[path][-1])
			elif changes[path][0] == "-":
				os.remove(path)
def write_file(path,changes):
	f = open(path,"w")
	for i in changes.keys():
		f.write(changes[i][-1])

def overwrite_file(path,changes):
	f = open(path,"r")
	mass = [line for line in f]
	temp = {i:mass[i] for i in range(len(mass))}
	for num in changes.keys():
		if changes[num][0] == "...":
			temp[num] = changes[num][-1]
		elif changes[num][0] == "+":
			temp[num] = changes[num][-1]
		elif changes[num][0] == "-":
			temp[num] = "\n"
	os.remove(path)
	f = open(path,"w")
	for num in temp.keys():
		f.write(temp[num])
	f.close()
