import paramiko
import os
import variables as var
import hashlib as hl
import pickle
# import variables as var



def connect_ssh():

	host = 'shell.xShellz.com'

	user = 'daibogh'

	secret = 'b@se32code'

	port = 22

	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	ssh.connect(hostname=host, username=user, password=secret, port=port)
	
	return ssh

# ssh = connect_ssh()

def connect_transport():
	host = 'shell.xShellz.com'

	port = 22

	transport = paramiko.Transport((host, port))

	return transport

def connect_ftp(transport):
	user = 'daibogh'

	secret = 'b@se32code'

	transport.connect(username = user, password = secret)

	sftp = paramiko.SFTPClient.from_transport(transport)

	return sftp

def exit_transport(transport):
	transport.close()



def push_file(ftp,file_path):
	try:
		ftp.put(users_destination+file_path,global_destination+file_path)
	except:
		file = file_path.split("/")[-1]
		file_path2 = "/".join(file_path.split("/")[:-1])
		ftp.normalize(file_path2)
		ftp.put(users_destination+file_path,global_destination+file_path)
	# print(local_path)

def pull_file(ftp,file_path):
	try:
		ftp.get(global_destination+file_path,users_destination+file_path)
	except:
		file = file_path.split("/")[-1]
		file_path2 = "/".join(file_path.split("/")[:-1])
		os.makedirs(file_path2)
		ftp.get(global_destination+file_path,users_destination+file_path)

def push_dir(ftp,path):
	ftp.normalize(global_destination+path)

def pull_dir(path):
	os.makedirs(users_destination+path)

def exit_ssh(ssh):
	# ssh.exec_command('exit')

	ssh.close()

def exit_ftp(sftp):
	sftp.close()
	# transport.close()


def glob_is_dir(ftp,path):
	try:
		ftp.chdir(path)
		ftp.chdir("/"+"/".join(path.split("/")[:-1]))
		return True
	except:
		return False



def download_users(ftp):
	try:
		f = ftp.file(var.administration+"users.txt","rb")
		users = pickle.load(f)
	except:
		users = {"admin":hl.md5("admin".encode()).hexdigest()}
		pass
	return users



def upload_users(ftp,users):
	f = ftp.file(var.administration+"users.txt","wb")
	pickle.dump(users,f)
	return 0



def commandline(ssh,command):
	stdin,stdout,stderr = ssh.exec_command(command)
	# return stdout.read().decode()
	print(stdout.read().decode())

def load_l(username,project_name):
	f = open(var.users_destination+username+"/"+project_name+"/stack.txt","rb")
	local_stack = pickle.load(f)
	f.close()
	return local_stack

def dump_l(username,project_name,stack):
	f = open(var.users_destination+username+"/"+project_name+"/stack.txt","wb")
	pickle.dump(stack,f)
	f.close()
	return 0

def dump_g(project_name,stack):
	transport = connect_transport()
	ftp = connect_ftp(transport)
	f = ftp.file(var.global_destination+project_name+"/stack.txt","wb")
	pickle.dump(stack,f)
	f.close()
	exit_ftp(ftp)
	exit_transport(transport)
	return 0
def load_g(project_name):
	transport = connect_transport()
	ftp = connect_ftp(transport)
	f = ftp.file(var.global_destination+project_name+"/stack.txt","rb")
	global_stack = pickle.load(f)
	f.close()
	exit_ftp(ftp)
	exit_transport(transport)
	return global_stack

def main():
	print("heeeeeey")
	transport = connect_transport()
	ftp = connect_ftp(transport)


	# users = download_users(ftp)

	# upload_users(ftp,users)















