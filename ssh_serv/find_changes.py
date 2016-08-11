import ssh_client as ssc

transport = ssc.connect_transport()
ftp = ssc.connect_ftp(transport)
def changes_lines(old_file, new_file,glob):
	if glob == 1:

		print(old_file,new_file)
		mass_of_changes={}
		oldFile=ftp.file(old_file,'r')
		newFile=open(new_file,'r')
		arr1=[line1 for line1 in oldFile]
		arr2=[line2 for line2 in newFile]
		if len(arr1)>len(arr2):
			for i in range(len(arr1)-len(arr2)):
				arr2.append('\n')
		else:
			for i in range(len(arr2)-len(arr1)):
				arr1.append('\n')

		maxlen=max(len(arr1), len(arr2))
						
		for i in range(maxlen):
			if arr1[i]!=arr2[i]:
				if arr1[i]=='':
					mass_of_changes[i+1]=["+",arr2[i]]
				elif arr2[i]=='':
						mass_of_changes[i+1]=['-',arr1[i]]
				else:
					mass_of_changes[i+1]=["...",arr1[i], arr2[i]]
	else:
		print(old_file,new_file)
		mass_of_changes={}
		oldFile=open(old_file,'r')
		newFile=ftp.file(new_file,'r')
		arr1=[line1 for line1 in oldFile]
		arr2=[line2 for line2 in newFile]
		if len(arr1)>len(arr2):
			for i in range(len(arr1)-len(arr2)):
				arr2.append('\n')
		else:
			for i in range(len(arr2)-len(arr1)):
				arr1.append('\n')

		maxlen=max(len(arr1), len(arr2))
						
		for i in range(maxlen):
			if arr1[i]!=arr2[i]:
				if arr1[i]=='':
					mass_of_changes[i+1]=["+",arr2[i]]
				elif arr2[i]=='':
						mass_of_changes[i+1]=['-',arr1[i]]
				else:
					mass_of_changes[i+1]=["...",arr1[i], arr2[i]]
	oldFile.close()
	newFile.close()
	return mass_of_changes
def main():
	return	
if "__name__" == "__main__":
	main()