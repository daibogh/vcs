import os
import pickle
import sys

def writing_variables(installing_directory):
	while 1:
		global_destination = input("введите адрес, где будет папка global\n")
		if os.path.exists(global_destination):
			os.chdir(global_destination)
			try:
				os.mkdir("global")
			except FileExistsError:
				print("папка global уже присутствует, нужно удалить")
				print("удалить?д/н")
				choose = input()
				if choose.lower() in ["yes","y","да","д"]:
					os.system("rm -Rf global")
					os.mkdir("global")
				else:
					sys.exit()
			os.chdir(global_destination+"/global/")
			global_destination = os.getcwd()+"/"
			os.mkdir("bin")
			os.chdir(global_destination+"bin")
			administration = os.getcwd()+"/"
			break
		else:
			print("такой директории не существует, введите заново")
	while 1:
		local_destination = input("введите адрес, где будет папка local\n")
		if os.path.exists(local_destination):
			os.chdir(local_destination)
			try:
				os.mkdir("local")
			except FileExistsError:
				print("папка local уже присутствует, нужно удалить")
				print("удалить?д/н")
				choose = input()
				if choose.lower() in ["yes","y","да","д"]:
					os.system("rm -Rf local")
					os.mkdir("local")
				else:
					sys.exit()
			os.chdir(local_destination+"/local/")
			local_destination = os.getcwd()+"/"
			break
		else:
			print("такой директории не существует, введите заново")	
	f = open(installing_directory+"/variables.py","w")
	f.write("global_destination = \""+global_destination+"\"\n")
	f.write("users_destination = \""+local_destination+"\"\n")
	f.write("administration = \""+administration+"\"\n")
	f.close()
	os.chdir(installing_directory)
	return administration
def main():
	f = open("bin_file.txt","rb")
	s = pickle.load(f)
	mass = s[-1]
	_help = s[0]
	f.close()
	while 1:
		installing_directory = input("введите адрес директории, куда устанавливать программу\n")
		if os.path.exists(installing_directory):
			os.chdir(installing_directory)
			path = writing_variables(installing_directory)
			for file_obj in mass:
				# print(file_obj.keys())
				f = open(list(file_obj.keys())[0],"wb")
				f.write(list(file_obj.values())[0])
				f.close()
			os.chdir(path)
			f = open("help.txt","wb")
			f.write(_help)
			f.close()
			break

		else:
			print("такой директории не существует, введите заново")

if __name__ == "__main__":
	main()

# os.mkdir("vcs")
# os.chdir(os.getcwd()+"/vcs")
