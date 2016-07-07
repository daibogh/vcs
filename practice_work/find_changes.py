oldFile=open('test1.txt','r')
newFile=open('test2.txt','r')
arr1=[line1.strip() for line1 in oldFile]
arr2=[line2.strip() for line2 in newFile]

if len(arr1)>len(arr2):
	maxlen=len(arr1)
	for i in range(len(arr1)-len(arr2)):
		arr2.append('')
else:
	maxlen=len(arr2)
	for i in range(len(arr2)-len(arr1)):
		arr1.append('')		
for i in range(maxlen):
	if arr1[i]!=arr2[i] and arr1[i]!='' and arr2[i]!='':
		print(i+1,') -',arr1[i],' || +',arr2[i],sep="")
	elif arr2[i]=='':
		print(i+1,') -',arr1[i],sep="")
	elif arr1[i]=='':
		print(i+1,') +',arr2[i],sep="")

oldFile.close()
newFile.close()
