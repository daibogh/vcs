import os
import py_detour as dt
import variables as var
import find_changes as fc

def global_changes(user_name, project_name):
	changes={}
	gl_dest=var.global_destination+"/"+user_name+"/"+project_name
	os.chdir(gl_dest)
	glob_files=dt.start_detour()
	lc_dest=var.local_destination+"/"+user_name+"/"+project_name
	os.chdir(lc_dest)
	loc_files=dt.start_detour()
	for i in range(len(glob_files)):
		if glob_files[i] not in loc_files:
			changes[glob_files[i]]=["-",]

	for i in range(len(loc_files)):
		if loc_files[i] not in glob_files:
			changes[loc_files[i]]=["+",]
		elif len(fc.changes_lines(gl_dest+"/"+loc_files[i], lc_dest+"/"+loc_files[i])):
				changes[loc_files[i]]=["...",fc.changes_lines(gl_dest+"/"+loc_files[i], lc_dest+"/"+loc_files[i])]
	print(changes)
			
global_changes("dima", "project1")


