import os
import os.path
import variables as var
import stack_commands as sc
import changes_in_local as chinlc
def push(local_stack,global_stack,project_name):
	temp_stack = []
	username = local_stack[-1]["user"]
	for element in reversed(local_stack):
		if element not in global_stack:
			temp_stack.append(element)
		else:
			break
	while temp_stack:
		element = temp_stack.pop()
		global_stack.append(element)
		changes = element["changes"]
		for path in changes.keys():
			if os.path.isdir(path):
				continue
			if changes[path][0] == "...":
				overwrite_file(var.users_destination+"/"+username+"/"+path,var.global_destination + path,changes[path][-1])
			elif changes[path][0] == "+":
				write_file(var.global_destination + "/" + path,changes[path][-1])
			elif changes[path][0] == "-":
				try:
					os.remove(var.global_destination + "/" + path)
				except:
					pass
	sc.dump_g(project_name,global_stack)





# <<<<<<< Updated upstream
			
# def pull(username,project_name):
# 	changes={}
# 	changes = chinlc.local_changes(username,project_name)
# 	for path in changes.keys():
# 		if changes[path][0] == "...":
# 			overwrite_file(var.users_destination+"/"+username+"/"+ path,changes[path][-1])
# 		elif changes[path][0] == "+":
# 			write_file(var.users_destination+"/"+username+"/"+ path,changes[path][-1])
# 		elif changes[path][0] == "-":
# 			os.remove(var.users_destination+"/"+username+"/"+ project_name+"/"+ path)
# =======





def pull(local_stack,global_stack,username,project_name):
	temp_stack = []
	for element in reversed(global_stack):
		if element not in local_stack:
			temp_stack.append(element)
		else:
			break
	for element in temp_stack:
		local_stack.append(element)
		changes = element["changes"]
		for path in changes.keys():
			if os.path.isdir(path):
				continue
			if changes[path][0] == "...":
				overwrite_file(var.global_destination+"/"+path,var.users_destination+"/"+username+"/"+path,changes[path][-1])
			elif changes[path][0] == "+":
				write_file(var.users_destination+"/"+path,changes[path][-1])
			elif changes[path][0] == "-":
				os.remove(var.users_destination+"/"+username+"/"+path)




# >>>>>>> Stashed changes
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

def overwrite_file(path1,path2,changes):
	# print(changes)
	# print("path",path)
	if '.DS_Store' in path1:
		return
	try:
		g = open(path1,"r")
	except:
		temp = path2.split("/")[:-1]
		_dir2 = ""
		for _dir in temp:
			_dir2 += "/"+_dir+"/"
			if os.path2.exists(_dir2):
				pass
			else:
				os.mkdir(_dir2)
		g = open(path1,"r")
	# g = open(path,"r")
	mass = [line for line in g]
	g.close()
	# temp = {i:mass[i] for i in range(len(mass))}
	# for num in changes.keys():
	# 	if changes[num][0] == "...":
	# 		temp[num] = changes[num][-1]
	# 	elif changes[num][0] == "+":
	# 		temp[num] = changes[num][-1]
	# 	elif changes[num][0] == "-":
	# 		temp[num] = "\n"
	# print(temp)
	try:
		os.remove(path2)
	except FileNotFoundError:
		pass
	# print(os.listdir())
	try:
		f = open(path2,"w")
		for line in mass:
			f.write(line)
	# f.seek(0)
	# f.truncate()
	# f.seek(0)
		f.close()
	except:
		temp = path2.split("/")[:-1]
		_dir2 = ""
		for _dir in temp:
			_dir2 += "/"+_dir+"/"
			if os.path2.exists(_dir2):
				pass
			else:
				os.mkdir(_dir2)
		f = open(path2,"w")
		for line in mass:
			f.write(line)
	# f.seek(0)
	# f.truncate()
	# f.seek(0)
		f.close()


	# f = open(path,"w")
	# for num in sorted(temp.keys()):
	# 	f.write(temp[num])
		# print(num,temp[num],sep = "===")
	# f.close()
	# f = open(path,"r")
	# for line in f:
		# print(line)
