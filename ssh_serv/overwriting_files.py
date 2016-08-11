import os
import os.path
import variables as var
# import stack_commands as sc
from ssh_client import glob_is_dir
import ssh_client as ssc
transport = ssc.connect_transport()
ftp = ssc.connect_ftp(transport)
# import changes_in_local as chinlc


def push(local_stack,global_stack,project_name):
	temp_stack = []
	print(local_stack[-1]["user"])
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
			cur =var.users_destination+username+"/"+path
			if changes[path][0] == "-":
				if os.path.isdir(cur):
					try:
						ftp.chdir(var.global_destination)
						ftp.rmdir(ftp.global_destination+path)	
					except:
						continue
				else:
					try:
						ftp.remove(var.global_destination + "/" + path)
					except:
						pass
			elif changes[path][0] == "+":
				if os.path.isdir(cur):
					try:
						ftp.chdir(var.global_destination)
						ftp.mkdir(path)	
					except:
						continue
				else:		
					write_file(var.global_destination + "/" + path,changes[path][-1],ftp)	
			elif changes[path][0] == "...":
				overwrite_file(var.users_destination+"/"+username+"/"+path,var.global_destination + path,changes[path][-1],1)				
				
	ssc.dump_g(project_name,global_stack)





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





"""
def pull(local_stack,global_stack,username,project_name):
	temp_stack = []
	for element in reversed(global_stack):
		if element not in local_stack:
			temp_stack.append(element)
		else:
			break
	while temp_stack:
		element = temp_stack.pop()
		local_stack.append(element)
		changes = element["changes"]
		for path in changes.keys():
			cur =var.global_destination+"/"+path
			if changes[path][0] == "...":
				overwrite_file(var.global_destination+"/"+path,var.users_destination+"/"+username+"/"+path,changes[path][-1])
			elif changes[path][0] == "+":
				if os.path.isdir(cur):
					try:
						os.chdir(var.users_destination+username)
						os.mkdir(path)	
					except:
						continue
				else:
					write_file(var.users_destination+"/"+username+"/"+path,changes[path][-1])
			elif changes[path][0] == "-":
				if os.path.isdir(var.users_destination+username+path):
					try:
						os.chdir(var.var.users_destination+username)
						os.rmdir(path)	
					except:
						continue
				else:
					try:
						os.remove(var.users_destination+"/"+username+"/"+path)
					except:
						pass
"""

# >>>>>>> Stashed changes
def write_file(path,changes,ftp):
	if ftp == 0:
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
		f.close()
	else:
		try:
			f = ftp.file(path,"w")
		except:
			path2 = "/"+"/".join(path.split("/")[:-1])+"/"
			ftp.normalize(path2)
			f = open(path,"w")
			
		for i in changes.keys():
			f.write(changes[i][-1])
		f.close()


def overwrite_file(path1,path2,ftp,glob):
	if glob == 1:
		ftp.get(path1,path2)
	else:
		ftp.put(path1,path2)
	

	# f = open(path,"w")
	# for num in sorted(temp.keys()):
	# 	f.write(temp[num])
		# print(num,temp[num],sep = "===")
	# f.close()
	# f = open(path,"r")
	# for line in f:
		# print(line)
