import variables as var
import stack_commands as sc
def pre_log(project_name):
	if input().split()[0] == "log":
		log(" ".join(input().split()[1:]))

def log(project_name, argument):
	global_stack  = sc.load_g(project_name)
	if argument == "simple":
		for commit in global_stack:
			print("#####################################################################")
			print(commit["date-time"])
			for element in commit["changes"].keys():
				print("["+commit["changes"][element][0]+"]",element,sep = " --- ")
			print("#####################################################################")
	if argument == "--name-only":
		for commit in global_stack:
			print("#####################################################################")
			print(commit["date-time"])
			for element in commit["changes"].keys():
				print("["+commit["changes"][element][0]+"]",element,sep = " --- ")
			print("#####################################################################")
	elif argument == "--reverse":
		for commit in reversed(global_stack):
			print("#####################################################################")
			print(commit["date-time"])
			for element in commit["changes"].keys():
				print("["+commit["changes"][element][0]+"]",element,sep = " --- ")
			print("#####################################################################")
	elif argument.split()[0] == "--after":
		pass
		

def main():
	log("n","--name-only")

if "__name__" == "__main__":
	main()

