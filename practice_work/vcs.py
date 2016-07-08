
import os
import pickle
import getpass
import variables as var
import signing_in as sign
# import interface
import user_commands as uc

def main():
	print("hello world!")
	current_user = sign.login()
	uc.make_project(current_user,"my_new_project")



if __name__ == "__main__":
    main()
