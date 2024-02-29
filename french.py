import tkinter as tk
import tkinter.messagebox
import random as r
import os 

import json
with open("../FrenchVerbRevision/Questions.json") as file:
    Database = json.load(file)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack
var = tk.StringVar()
label = tk.Label( root, textvariable=var, relief=tk.RAISED )
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

words = []

def SelectWord():
    CurrentWord = r.choice(list(Database.keys())) 
    if CurrentWord not in SelectWord.WordAlreadySelected:
        SelectWord.WordAlreadySelected.append(CurrentWord)
        return CurrentWord
    else:
        return SelectWord()

SelectWord.WordAlreadySelected = []

for picked in range(3):
    words.append(SelectWord())

ans = r.randint(0,2)
find = words[ans]

def check_correct(char):
    if char == ans:
        tk.messagebox.showinfo("Answer","Correct!!")
    else:
        wrong = ("Wrong the correct answer was ",find)
        tk.messagebox.showinfo("Answer",wrong)
    os.execl(os.sys.executable,*([os.sys.executable]+os.sys.argv))

#                            |word          |command
A = tk.Button(root, text =words[0], command = lambda :check_correct(0))
B = tk.Button(root, text =words[1], command = lambda :check_correct(1))
C = tk.Button(root, text =words[2], command = lambda :check_correct(2))


QuestionAnswer = Database[find]["Questions"]
Length = len(QuestionAnswer)

var.set(QuestionAnswer[Length - 1])

label.pack(side = tk.TOP)
A.pack(side = tk.LEFT)
B.pack(side = tk.LEFT)
C.pack(side = tk.LEFT)

root.geometry("+{}+{}".format(positionRight, positionDown))
 
root.mainloop()
