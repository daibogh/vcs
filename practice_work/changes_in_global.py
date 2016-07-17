import os
import py_detour as dt
import variables as var
import find_changes as fc

def main():
	global_changes("dima", "project1")
	return 0

def global_changes(user_name, project_name,branch_name,gl_dest,lc_dest):

	changes={}
	os.chdir(gl_dest)
	glob_files=dt.ret_det()
	os.chdir(lc_dest)
	print(lc_dest)
	loc_files=dt.ret_det()
	for i in range(len(glob_files)):
		if glob_files[i] not in loc_files:
			path = project_name + '/' + branch_name + "/"+ os.getcwd().split(branch_name)[-1]
			changes[path+glob_files[i]]=["-",]

	for i in range(len(loc_files)):
		print("loc_files[i] = ",loc_files[i])
		if loc_files[i] in [ ".DS_Store",".stack.txt"]:
			continue
		if loc_files[i] not in glob_files:
			new_lines = {}
			if os.path.isfile(loc_files[i]):
				f = open(loc_files[i],"r")
				j = 0
				for line in f:
					j+=1
					new_lines[j] = ["+",line,]
				f.close()
			path = project_name + '/' + branch_name + "/"+ os.getcwd().split(branch_name)[-1]
			changes[path+loc_files[i]]=["+",new_lines]
		elif os.path.isdir(os.getcwd()+ "/"+ loc_files[i]):
			continue	
		elif len(fc.changes_lines(gl_dest+"/"+loc_files[i], lc_dest+"/"+loc_files[i])):
			path = project_name + '/' + branch_name + "/" + os.getcwd().split(branch_name)[-1]
			changes[path+"/"+loc_files[i]]=["...",fc.changes_lines(gl_dest+"/"+loc_files[i], lc_dest+"/"+loc_files[i])]
	print(changes)
	return(changes)
			
if "__name__" == "__main__":
	main()
