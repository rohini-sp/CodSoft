import tkinter
from tkinter import *

root = Tk()
root.title("To-Do list")
root.geometry('400x650+400+100')
root.resizable(False,False)

task_ls=[]

def open_file():
    try:
        global task_ls
        with open("tasklist.txt","r") as tfile:
            tasks=tfile.readlines()
        for task in tasks:
            if task!='\n':
                task_ls.append(task)
                listbox.insert(END, task)
    except:
        file=open("tasklist.txt","w")
        file.close()

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt","a") as tfiles:
            tfiles.write(f"\n{task}")
        task_ls.append(task)
        listbox.insert(END,task)
    
def deleteTask():
    global task_ls
    task=str(listbox.get(ANCHOR))
    if task in task_ls:
        task_ls.remove(task)
        with open("tasklist.txt","w") as tfiles:
            for task in task_ls:
                tfiles.write(task+"\n")
        listbox.delete(ANCHOR)

        
Icon_img = PhotoImage(file='images/icon.png')
root.iconphoto(False, Icon_img)

Top = PhotoImage(file='images/pngegg.png')
Label(root,image=Top).pack()

icon_img = PhotoImage(file='images/icon.png')
Label(root,image=icon_img, bg="#73ad70").place(x=70,y=60)

heading = Label(root,text="ALL TASKS", font="arial 25 bold",fg='white',bg='#73ad70')
heading.place(x=130,y=57)

frame = Frame(root,width=400,height=50,bg='white')
frame.place(x=0,y=180)

task = StringVar()
task_entry=Entry(frame,width=25,font='arial 15',bd=2)
task_entry.place(x=10,y=10)
task_entry.focus()

button=Button(frame,text="ADD",font='arial 20 bold',width=6,bg='#477744',fg='#FEF4F4',bd=0,command=addTask)
button.place(x=300,y=0)

frame1=Frame(root,bd=3,width=700,height=280,bg='#73ad70')
frame1.pack(pady=(90,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#73ad70",fg='#FEF4F4',cursor="hand2",selectbackground="#477744")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scroll=Scrollbar(frame1)
scroll.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

button1=Button(text="DELETE",font='arial 20 bold',width=8,bg='#477744',fg='#FEF4F4',bd=0,command=deleteTask)
button1.place(x=140,y=580)

open_file()



root.mainloop()
