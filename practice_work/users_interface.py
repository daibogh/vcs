import sys
import variables as var
import signing_in as si
import interface as intf

def users_interface():
	print("Добро пожаловать в наш VCS.")
	while 1:
		username=si.login()
		print("Вы авторизировались как </"+username+"/>.")
		intf.interface(username)
		if input("Вы хотите сменить пользователя?(д/н) ").lower() in ["yes","да","y","д"]:
			continue
		elif input("Вы хотите выйти из системы?(д/н) ").lower() in ["yes","да","y","д"]:
			sys.exit()

def main():
	users_interface()


if "__name__" == "__main__":
	main()