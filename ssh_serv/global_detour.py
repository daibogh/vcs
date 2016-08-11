import os
import ssh_client as ssc
from ssh_client import glob_is_dir
transport = ssc.connect_transport()
ftp = ssc.connect_ftp(transport)
def main():
	ret_det()

def go_in(new_directory):
	ftp.chdir(ftp.getcwd()+'/'+new_directory)
def go_up():
	start_position = ftp.getcwd()
	while 1:
		if start_position[-1] != '/':
			start_position = start_position[:-1]
		else:
			break
	ftp.chdir(start_position)
def start_detour(path):
	ftp.chdir(path)
	mass_files=[]
	for i in ftp.listdir():
		cur = ftp.getcwd()+'/'+i
		if glob_is_dir(ftp,cur):
			mass_files.append(i)
			go_in(i)
			new_mass=start_detour()
			for ind in range(len(new_mass)):
				new_mass[ind]=i+"/"+new_mass[ind]
			mass_files.extend(new_mass)
			go_up()
		else:
			mass_files.append(i)
	return mass_files

def ret_det():
	list=start_detour()
	return list

if __name__ == "__main__":
	main()
