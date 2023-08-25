from tkinter import *
import math

answerVar = ""
SqRoot = ""
root = Tk()
root.title('Calculator')
root.resizable(False,False)
EntryLabel = StringVar()
Label(root, font=('arial', 25),
textvariable = EntryLabel,
justify = LEFT, height=2, width=7).grid(columnspan=4, padx=120)
FinalLabel = StringVar()
Label(root, font=('arial', 25),
textvariable = FinalLabel,
justify = LEFT, height=2, width=7).grid(columnspan = 4 , padx=120)


def Clear():
    global answerVar
    global SqRoot
    answerVar = ""
    SqRoot = ""
    EntryLabel.set("")
    FinalLabel.set("")

def clearEntry():
    global answerVar
    global SqRoot
    SqRoot = answerVar
    answerVar = ""
    EntryLabel.set(answerVar)

def changeEntry(entry):
    global answerVar
    global SqRoot
    
    answerVar = answerVar + str(entry)
    SqRoot = answerVar
    EntryLabel.set(answerVar)

def evalSqRoot():
    global answerVar
    global SqRoot
    try:
        sqrtAnswer = math.sqrt(eval(str(SqRoot)))
        clearEntry()
        FinalLabel.set(sqrtAnswer)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(answerVar)))
            clearEntry()
            FinalLabel.set(sqrtAnswer)
        except(ValueError,SyntaxError,TypeError,ZeroDivisionError):
            clearEntry()
            FinalLabel.set("Error")

def evalAnswer():
    global answerVar
    try:
       eval(answerVar)
       evaluatedAnswerLabel= str(eval(answerVar))    
       clearEntry()
       FinalLabel.set(evaluatedAnswerLabel)

    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clearEntry()
        FinalLabel.set("Error")


def createButton(txt,x,y):
    Button(root, font=('arial', 12),
           padx=16,pady=16,text = str(txt),
           command = lambda:changeEntry(txt),
           height = 2, width=9).grid(row = x , column = y, sticky=E)

buttons = ['AC','√','%','/','7','8','9','*','4','5','6','-','1','2','3','+','','','.','']
btn_ls_TraversalCounter = 0
for i in range(3,8):
    for j in range(0,4):
        createButton(buttons[btn_ls_TraversalCounter],i,j)
        btn_ls_TraversalCounter =btn_ls_TraversalCounter + 1

Button(root,font=('arial', 12),
       padx=16,pady=16, text = "√",
       command = lambda:evalSqRoot(),
       height=2, width=9).grid(row = 3 , column = 1, sticky = E)

Button(root,font=('arial', 12),
       padx=16,pady=16, text = "AC",
       command = lambda:Clear(),
       height=2, width=9).grid(row = 3 , column = 0 , sticky = E)

Button(root,font=('arial', 12),
       padx=16,pady=16, text = "0",
       command = lambda:changeEntry(0),
       height=2, width=21).grid(row = 7 , column = 0 ,
       columnspan=2 , sticky = E)

Button(root,font=('arial', 12),
       padx=16,pady=16, text = "=",
       command = lambda:evalAnswer(),
       height=2, width=9).grid(row = 7 , column = 3, sticky = E)


root.mainloop()
