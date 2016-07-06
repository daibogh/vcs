import os

def go_in(new_directory):
	os.chdir(os.getcwd()+'/'+new_directory)
def pwd():
	print(os.getcwd())
def dir():
	for i in os.listdir():
		print(i)
def go_up():
	start_position = os.getcwd()
	while 1:
		if start_position[-1] != '/':
			start_position = start_position[:-1]
		else:
			break
	os.chdir(start_position)
def start_bash():
	while 1:
		p = os.getcwd()
		command = input(p+": py_bash_user$ ").split()
		if command[0] == "cd":
			if command[1] == "..":
				go_up()
			else:
				go_in(command[1])
		elif command[0] == "ls":
			dir()
		elif command[0] == "rep":
			rep()
		elif command[0] == "pwd":
			pwd()
		elif command[0] == "exit":
			break

