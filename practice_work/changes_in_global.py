import os
import py_detour as dt
import variables as var
import find_changes as fc

def main():
	global_changes("dima", "project1",'master','G:\\Project\\global\\new\master\\','G:\\Project\\local\\dima\\new\\master\\')
	return 0

# def isdir(path):
	

def global_changes(user_name, project_name,branch_name,gl_dest,lc_dest):

	changes={}
	os.chdir(gl_dest)
	glob_files=dt.ret_det()
	os.chdir(lc_dest)
	loc_files=dt.ret_det()
	os.chdir(gl_dest)
	for i in range(len(glob_files)):
		if glob_files[i] not in loc_files:
			new_lines = {}
			print("glob",glob_files[i])
			if not os.path.isdir(glob_files[i]):
				f = open(glob_files[i],"r")
				j = 0
				for line in f:
					j+=1
					new_lines[j] = ["-",line,]
				f.close()
				path = project_name + '/' + branch_name + "/"+ os.getcwd().split(branch_name)[-1]
				changes[path+glob_files[i]]=["-f",new_lines]
			else:
				path = project_name + '/' + branch_name + "/"+ os.getcwd().split(branch_name)[-1]
				changes[path+glob_files[i]]=["-"]

	os.chdir(lc_dest)
	for i in range(len(loc_files)):
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
				changes[path+loc_files[i]]=["+f",new_lines]
			else:
				path = project_name + '/' + branch_name + "/"+ os.getcwd().split(branch_name)[-1]
				changes[path+loc_files[i]]=["+"]
		elif os.path.isdir(os.getcwd()+ "/"+ loc_files[i]):
			continue	
		elif len(fc.changes_lines(gl_dest+"/"+loc_files[i], lc_dest+"/"+loc_files[i])):
			path = project_name + '/' + branch_name + "/" + os.getcwd().split(branch_name)[-1]
			changes[path+"/"+loc_files[i]]=["...",fc.changes_lines(gl_dest+"/"+loc_files[i], lc_dest+"/"+loc_files[i])]
	return(changes)
			
if __name__ == "__main__":
	main()
