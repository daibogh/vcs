import variables as var
import stack_commands as sc
from datetime import datetime
def pre_log(project_name):
	if input().split()[0] == "log":
		log(" ".join(input().split()[1:]))

def log(project_name, argument, branch_name):
	global_stack  = sc.load_g(project_name, branch_name)
	if argument == "--simple":
		print("</"+branch_name+"/>")
		for commit in global_stack:
			print("#####################################################################")
			print(commit["date-time"])
			print("</"+commit["user"]+"/>")
			for element in commit["changes"].keys():
				print("["+commit["changes"][element][0]+"]",element,":",sep = " --- ")
				if commit["changes"][element][0]=="...":
					for lines in commit["changes"][element][1].keys():
						if commit["changes"][element][1][lines][0]=="...":
							print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1]+" -> "+commit["changes"][element][1][lines][2][:-1])
						else:
							print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1])
			print("#####################################################################")
	elif argument == "--name-only":
		print("</"+branch_name+"/>")
		for commit in global_stack:
			print("#####################################################################")
			print(commit["date-time"])
			for element in commit["changes"].keys():
				print("["+commit["changes"][element][0]+"]",element,sep = " --- ")
			print("#####################################################################")
	elif argument == "--reverse":
		print("</"+branch_name+"/>")
		for commit in reversed(global_stack):
			print("#####################################################################")
			print(commit["date-time"])
			print("</"+commit["user"]+"/>")
			for element in commit["changes"].keys():
				print("["+commit["changes"][element][0]+"]",element,":",sep = " --- ")
				if commit["changes"][element][0]=="...":
					for lines in commit["changes"][element][1].keys():
						if commit["changes"][element][1][lines][0]=="...":
							print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1]+" -> "+commit["changes"][element][1][lines][2][:-1])
						else:
							print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1])
			print("#####################################################################")
	elif argument.split()[0] == "--after":
		print("</"+branch_name+"/>")
		if len(argument.split())<=1:
			print("Вы не ввели дату-время. Наберите help, чтобы посмотреть образец.")
			return
		for commit in global_stack:
			if argument.split()[1] == "all":
				com_time=datetime.time(commit["date-time"])
				try:
					required_time=datetime.time(datetime.strptime(' '.join(argument.split()[2:]), "%H:%M"))
				except:
					print("Нарушен формат дата-время. Наберите help, чтобы посмотреть образец.")
					return	
			else:
				com_time=commit["date-time"]
				try:
					required_time=datetime.strptime(' '.join(argument.split()[1:]), "%Y/%m/%d %H:%M")
				except:
					try:
						required_time=datetime.combine(datetime.date(datetime.today()),datetime.time(datetime.strptime(' '.join(argument.split()[1:]), "%H:%M")))
					except:
						try:
							required_time=datetime.strptime(' '.join(argument.split()[1:]), "%Y/%m/%d")
						except:			
							print("Нарушен формат дата-время. Наберите help, чтобы посмотреть образец.")
							return
			if com_time>required_time:
				print("#####################################################################")
				print(commit["date-time"])
				print("</"+commit["user"]+"/>")
				for element in commit["changes"].keys():
					print("["+commit["changes"][element][0]+"]",element,":",sep = " --- ")
					if commit["changes"][element][0]=="...":
						for lines in commit["changes"][element][1].keys():
							if commit["changes"][element][1][lines][0]=="...":
								print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1]+" -> "+commit["changes"][element][1][lines][2][:-1])
							else:
								print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1])
				print("#####################################################################")
	elif argument.split()[0] == "--before":
		print("</"+branch_name+"/>")
		if len(argument.split())<=1:
			print("Вы не ввели дату-время. Наберите help, чтобы посмотреть образец.")
			return
		for commit in global_stack:
			if argument.split()[1] == "all":
				com_time=datetime.time(commit["date-time"])
				try:
					required_time=datetime.time(datetime.strptime(' '.join(argument.split()[2:]), "%H:%M"))
				except:
					print("Нарушен формат дата-время. Наберите help, чтобы посмотреть образец.")
					return	
			else:
				com_time=commit["date-time"]
				try:
					required_time=datetime.strptime(' '.join(argument.split()[1:]), "%Y/%m/%d %H:%M")
				except:
					try:
						required_time=datetime.combine(datetime.date(datetime.today()),datetime.time(datetime.strptime(' '.join(argument.split()[1:]), "%H:%M")))
					except:
						try:
							required_time=datetime.strptime(' '.join(argument.split()[1:]), "%Y/%m/%d")
						except:			
							print("Нарушен формат дата-время. Наберите help, чтобы посмотреть образец.")
							return			
			if com_time<required_time:
				print("#####################################################################")
				print(commit["date-time"])
				print("</"+commit["user"]+"/>")
				for element in commit["changes"].keys():
					print("["+commit["changes"][element][0]+"]",element,":",sep = " --- ")
					if commit["changes"][element][0]=="...":
						for lines in commit["changes"][element][1].keys():
							if commit["changes"][element][1][lines][0]=="...":
								print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1]+" -> "+commit["changes"][element][1][lines][2][:-1])
							else:
								print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1])
				print("#####################################################################")
	elif argument.split()[0] == "--author":
		print("</"+branch_name+"/>")
		if len(argument.split())<=1:
			print("Вы не ввели имя юзера. Наберите help, чтобы посмотреть образец.")
			return
		for commit in global_stack:
			if commit["user"] == argument.split()[1]:
				print("#####################################################################")
				print(commit["date-time"])
				print("</"+commit["user"]+"/>")
				for element in commit["changes"].keys():
					print("["+commit["changes"][element][0]+"]",element,":",sep = " --- ")
					if commit["changes"][element][0]=="...":
						for lines in commit["changes"][element][1].keys():
							if commit["changes"][element][1][lines][0]=="...":
								print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1]+" -> "+commit["changes"][element][1][lines][2][:-1])
							else:
								print("\t"+str(lines)+") "+"["+commit["changes"][element][1][lines][0]+"]"+": "+commit["changes"][element][1][lines][1][:-1])
				print("#####################################################################")
	else:
		print('Такой команды нет. Наберите help, чтобы посмотреть образец.')		

def main():
	log("n","--name-only")

if "__name__" == "__main__":
	main()

