import os
import os.path
import variables as var
import stack_commands as sc
def push(local_stack,global_stack,project_name):
	temp_stack = []
	for element in reversed(local_stack):
		if element not in global_stack:
			temp_stack.append(element)
		else:
			break
	while temp_stack:
		element = temp_stack.pop()
		changes = element["changes"]
		for path in changes.keys():
			if changes[path][0] == "...":
				overwrite_file(var.global_destination + path,changes[path][-1])
			elif changes[path][0] == "+":
				write_file(var.global_destination + "/" + path,changes[path][-1])
			elif changes[path][0] == "-":
				os.remove(var.global_destination + "/" + path)
	sc.dump_g(project_name,global_stack)
def pull(local_stack,global_stack,username,project_name):
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
				os.remove(var.users_destination+"/"+path)
def write_file(path,changes):
	try:
		f = open(path,"w")
	except:
		temp = path.split("/")[:-1]
		_dir2 = ""
		for _dir in temp:
			_dir2 += "/"+_dir+"/"
			if os.path.exists(_dir2):
				pass
			else:
				os.mkdir(_dir2)
		f = open(path,"w")
		
	for i in changes.keys():
		f.write(changes[i][-1])

def overwrite_file(path,changes):
	print(changes)
	print("path",path)
	try:
		g = open(path,"r")
	except:
		temp = path.split("/")[:-1]
		_dir2 = ""
		for _dir in temp:
			_dir2 += "/"+_dir+"/"
			if os.path.exists(_dir2):
				pass
			else:
				os.mkdir(_dir2)
		g = open(path,"r")
	# g = open(path,"r")
	mass = [line for line in g]
	g.close()
	temp = {i:mass[i] for i in range(len(mass))}
	for num in changes.keys():
		if changes[num][0] == "...":
			temp[num] = changes[num][-1]
		elif changes[num][0] == "+":
			temp[num] = changes[num][-1]
		elif changes[num][0] == "-":
			temp[num] = "\n"
	print(temp)
	os.remove(path)
	f = open(path,"w")
	f.seek(0)
	f.truncate()
	f.seek(0)
	f.close()
	f = open(path,"w")
	for num in sorted(temp.keys()):
		f.write(temp[num])
		# print(num,temp[num],sep = "===")
	f.close()
	f = open(path,"r")
	for line in f:
		print(line)
