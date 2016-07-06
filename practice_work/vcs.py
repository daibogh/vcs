
import os
import pickle
import getpass
import variables as var
import signing_in as sign
import interface

def main():
	print("hello world!")
	current_user = sign.login()
	interface.interface(current_user)
	



if __name__ == "__main__":
    main()
