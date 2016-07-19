import os
import pickle
administration = "/Users/DaiBogh/practice/global/bin"
dest = os.getcwd()
def build_project():
	os.chdir("/Users/DaiBogh/vcs/practice_work/")
	m = os.listdir()
	m.remove("variables.py")
	m.remove("__pycache__")
	mass = []
	for i in m:
		f = open(i,"rb")
		file = f.read()
		f.close()
		mass.append({i:file})
	os.chdir(administration)
	d = open("help.txt","rb")
	s = d.read()
	d.close()
	os.chdir(dest)
	os.remove("bin_file.txt")
	g = open("bin_file.txt","wb")
	pickle.dump([s,mass],g)
	g.close()
if __name__ == "__main__":
	build_project()