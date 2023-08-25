from tkinter import *
import pyperclip
import random

root = Tk()
root.title("Password Generator")
root.geometry('600x600')
root.resizable(False,False)

password_str = StringVar()
password_len = IntVar()

password_len.set(0)

def generate():
    pass_ = s1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*','(', ')']

    password=''

    for x in range(password_len.get()):
        password = password+random.choice(pass_)
        password_str.set(password)

def copy():
    random_password = password_str.get()
    pyperclip.copy(random_password)


#GUI
Label(root,text="PASSWORD GENERATOR",font="arial 20 bold").pack()
Label(root, text="Enter name").pack(pady=3)
Entry(root).pack(pady=3)
Label(root, text="Enter password length").pack(pady=3)
Entry(root,textvariable=password_len).pack(pady=3)
Button(root, text="Generate Password", command=generate).pack(pady=3)
Entry(root, textvariable=password_str).pack(pady=3)
Button(root,text="Copy", command=copy).pack()
root.mainloop()


