import os

def go_in(new_directory):
	os.chdir(os.getcwd()+'\\'+new_directory)
def go_up():
	start_position = os.getcwd()
	while 1:
		if start_position[-1] != '\\':
			start_position = start_position[:-1]
		else:
			break
	os.chdir(start_position)
def start_detour():
        listd = os.listdir()
        for i in range(len(listd)):
                cur = os.getcwd()+'\\'+listd[i]
                if os.path.isdir(cur):
                        go_in(listd[i])
                        start_detour()
                        go_up()
                else:
                        print(listd[i])
