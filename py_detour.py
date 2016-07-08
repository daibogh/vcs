import os

def go_in(new_directory):
	os.chdir(os.getcwd()+'/'+new_directory)
def go_up():
	start_position = os.getcwd()
	while 1:
		if start_position[-1] != '/':
			start_position = start_position[:-1]
		else:
			break
	os.chdir(start_position)
def start_detour():
	mass_files=[]
	for i in os.listdir():
		cur = os.getcwd()+'/'+i
		if os.path.isdir(cur):
			go_in(i)
			new_mass=start_detour()
			for ind in range(len(new_mass)):
				new_mass[ind]=i+"/"+new_mass[ind]
			mass_files.extend(new_mass)
			go_up()
		else:
			mass_files.append(i)
	return mass_files

