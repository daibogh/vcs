import os
def do_changes(stack1,stack2):
	temp_stack = []
	for element in reversed(stack1):
		if element not in stack2:
			temp_stack.append(element)
		else:
			break
	for element in temp_stack:
		changes = element["changes"]
			for path in changes.keys():
				if changes[path][0] == "...":
					overwrite_file(path,changes[path][-1])
				elif changes[path][0] == "+":
					write_file(path,changes[path][-1])
				elif changes[path][0] == "-":
					os.remove(path)
def write_file(path,changes):
	f = open(path,"w")
	for i in changes.keys():
		f.write(changes[i][-1])

def overwrite_file(path,changes):
	f = open(path,"r")
	mass = [line for line in f]
	temp = {i:mass[i] for i in range(len(mass))}
	for num in changes.keys():
		if changes[num][0] == "...":
			temp[num] = changes[num][-1]
		elif changes[num][0] == "+"
			temp[num] = changes[num][-1]
		elif changes[num][0] = "-":
			temp[num] = "\n"
	os.remove(path)
	f = open(path,"w")
	for num in temp.keys():
		f.write(temp[num])
	f.close()
