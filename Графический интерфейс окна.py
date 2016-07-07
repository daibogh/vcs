from tkinter import *

root = Tk()

width = int(root.winfo_screenwidth())
height = int(root.winfo_screenheight())
new_geometry = str(width - 300) + 'x' + str(height - 200) + '+100+100'
root.geometry(new_geometry)

#buttons = [ Button(root) for i in range(16) ]
#for i in buttons:
#    i.pack()

label_Project = Label(root, text='Project', width=10)
label_File = Label(root, text='File', width=10)
label_For_commit = Label(root, text='For commit', width=10)

label_Project.grid(row=0, column=0,columnspan=2)
label_File.grid(row=0, column=2,columnspan=4)
label_For_commit.grid(row=0, column=6,columnspan=2)
#label_Project.pack()
#label_File.pack()
#label_For_commit.pack()


button_Open = Button(text='Open',width=5,height=0,bg='black',fg='red',font='arial 8')
button_Add_P = Button(text='Add',width=4,height=0,bg='black',fg='red',font='arial 8')
button_Add_F = Button(text='Add',width=4,height=0,bg='black',fg='red',font='arial 8')
button_Index_file = Button(text='Index file',width=15,height=0,bg='black',fg='red',font='arial 8')
button_Cancel_file = Button(text='Cancel index',width=15,height=0,bg='black',fg='red',font='arial 8')
#button_Delete = Button(text='Delete',width=10,height=0,bg='black',fg='red',font='arial 8')
button_Show_f_for_commit = Button(text='Show files for commit',width=20,height=0,bg='black',fg='red',font='arial 8')
button_Commit = Button(text='Commit',width=10,height=0,bg='black',fg='red',font='arial 8')
button_Show_commit_history = Button(text='Show commit history',width=25,height=3,bg='black',fg='red',font='arial 8')
button_Check_status_files = Button(text='Check the status of files',width=25,height=3,bg='black',fg='red',font='arial 8')
button_PUSH = Button(root, text='PUSH to the local server',width=25,height=3,bg='black',fg='red',font='arial 8')
button_Help = Button(text='Help',width=25,height=3,bg='black',fg='red',font='arial 8')
button_Exit = Button(text='Exit',width=25,height=3,bg='black',fg='red',font='arial 8')
My_Buttons = [button_Open, button_Add_P, button_Add_F, button_Index_file,
              button_Cancel_file, button_Show_f_for_commit,
              button_Commit, button_Show_commit_history, button_Check_status_files,
              button_PUSH, button_Help, button_Exit]
ПОПРАВИТЬ КНОПКИ И LABEL
i = 0
#button_Add_F.pack(side='left')
for button in My_Buttons:
    if i < 7:
        button.grid(row=1,column=i)
        i += 1
    else:
        button.grid(row=0, column=i, columnspan=2, rowspan=2)
        i += 1
    #button.pack()


root.mainloop()