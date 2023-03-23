import tkinter as tk
import tkinter.messagebox
import random as r
import os 
from question import Questions
from answer import word_array


root = tk.Tk()
frame = tk.Frame(root)
frame.pack
var = tk.StringVar()
label = tk.Label( root, textvariable=var, relief=tk.RAISED )
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)




indices = []
for i in word_array:
    indices.append(i)

picked = 0
a_av = 0
b_av = 0
c_av = 0

a_text = ""
b_text = ""
c_text = ""

while picked < 3:
    word = r.randrange(len(word_array))
    print(word)
    picked += 1
    pick = r.randint(1,3)
    #print(pick)
    print(word_array)
    if pick == 1 and a_av == 0:
        a_av += 1
        a_text = a_text = word_array[word]
        word_array.remove(word_array[word])
    elif pick == 2 and b_av == 0:
        b_av += 1
        b_text = b_text = word_array[word]
        word_array.remove(word_array[word])
    elif pick == 3 and c_av == 0:
        c_av += 1
        c_text = c_text = word_array[word]
        word_array.remove(word_array[word])
    else:
        picked -= 1
    
 
picked_ans = 0
find = ""
ans = r.randint(1,3)
if ans == 1:
    find = find = a_text
elif ans == 2:
    find = find = b_text
elif ans == 3:
    find = find = c_text
number = 0
for i in indices:
    if i == find:
        picked_ans = picked_ans = number
        print("ok")
    number += 1

print(number)




HEIGHT = 500
WIDTH = 600


def check_correct(char):
    global word_array ; global picked
    if char == "a" and a_text == find:
        print("correct")
        word_array += indices

        
    elif char == "b" and  b_text == find:
        print("correct")
        word_array += indices


    elif char == "c" and c_text == find:
        print("correct")
        word_array += indices


    else:
        print("wrong")
        wrong = ("Wrong the correct answer was ",find)
        tk.messagebox.showinfo("Answer",wrong)
    os.execl(os.sys.executable,*([os.sys.executable]+os.sys.argv))

#                            |word          |command
A = tk.Button(root, text =a_text, command = lambda :check_correct("a"))
B = tk.Button(root, text =b_text, command = lambda :check_correct("b"))
C = tk.Button(root, text =c_text, command = lambda :check_correct("c"))

var.set(Questions[picked_ans])

label.pack(side = tk.TOP)
A.pack(side = tk.LEFT)
B.pack(side = tk.LEFT)
C.pack(side = tk.LEFT)

root.geometry("+{}+{}".format(positionRight, positionDown))
 

root.mainloop()