import pickle
destination = "/Users/DaiBogh/practice/"
global_destination = "/Users/DaiBogh/practice/global/"
f = open(global_destination+"version_control.txt","rb")
global_version_control = pickle.load(f)
f.close