from tkinter import *

root = Tk()
'''                 НАСТРОЙКА РАЗМЕРА И РАСПОЛОЖЕНИЯ ОКНА                 '''
width = int(root.winfo_screenwidth())
height = int(root.winfo_screenheight())
new_geometry = str(width - 300) + 'x' + str(height - 200) + '+100+100'
root.geometry(new_geometry)

'''                                 НАДПИСИ                               '''
label_Project = Label(root, text='Project', width=10, font='arial 12')
label_File = Label(root, text='File', width=10, font='arial 12')
label_For_commit = Label(root, text='For commit', width=10, height=1, font='arial 12')

label_Project.grid(row=0, column=0,columnspan=2)
label_File.grid(row=0, column=2,columnspan=3)
label_For_commit.grid(row=0, column=5,columnspan=2)

'''                                 КНОПКИ                                '''
button_Open = Button(text='Open',width=6,height=0,bg='black',fg='red',font='arial 10')
button_Add_P = Button(text='Add',width=4,height=0,bg='black',fg='red',font='arial 10')
button_Add_F = Button(text='Add',width=4,height=0,bg='black',fg='red',font='arial 10')
button_Index_file = Button(text='Index file',width=10,height=0,bg='black',fg='red',font='arial 10')
button_Cancel_file = Button(text='Cancel index',width=15,height=0,bg='black',fg='red',font='arial 10')
button_Show_f_for_commit = Button(text='Show files for commit',width=20,height=0,bg='black',fg='red',font='arial 10')
button_Commit = Button(text='Commit',width=10,height=1,bg='black',fg='red',font='arial 10')
button_Show_commit_history = Button(text='Show commit\n history',width=11,height=2,bg='black',fg='red',font='arial 13')
button_Check_status_files = Button(text='Check the \nstatus of files',width=11,height=2,bg='black',fg='red',font='arial 13')
button_PUSH = Button(root, text='PUSH to the\n local server',width=11,height=2,bg='black',fg='red',font='arial 13')
button_Help = Button(text='Help',width=5,height=2,bg='black',fg='red',font='arial 13')
button_Exit = Button(text='Exit',width=6,height=2,bg='black',fg='red',font='arial 13')

My_Buttons = [button_Open, button_Add_P, button_Add_F, button_Index_file,
              button_Cancel_file, button_Show_f_for_commit,
              button_Commit, button_Show_commit_history, button_Check_status_files,
              button_PUSH, button_Help, button_Exit]

i = j = 0

for button in My_Buttons:
    if i < 7:
        button.grid(row=1,column=i)
        i += 1
    else:
        button.grid(row=0, column=i + j*2, columnspan=2, rowspan=2)
        j += 1
    #button.pack()


root.mainloop()