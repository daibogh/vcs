import pickle
def load_local_information(user):
	try:
		f = open(destination+user+"version_control.txt","rb")
		local_version_control = pickle.load(f)
		f.close()
	except:
		first_time_use()
	return local_version_control