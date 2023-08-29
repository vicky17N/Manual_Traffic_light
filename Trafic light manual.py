from tkinter import *
def red():
    canvas1.create_oval(120,120,50,50,fill='red',outline='lightgray',width= 4)
    canvas2.create_oval(120, 120, 50, 50, fill='white', outline='lightgray', width=4)
    canvas3.create_oval(120, 120, 50, 50, fill='white', outline='lightgray', width=4)

def orange():
    canvas1.create_oval(120, 120, 50, 50, fill='white', outline='lightgray', width=4)
    canvas2.create_oval(120, 120, 50, 50, fill='orange', outline='lightgray', width=4)
    canvas3.create_oval(120, 120, 50, 50, fill='white', outline='lightgray', width=4)

def green():
    canvas1.create_oval(120, 120, 50, 50, fill='white', outline='lightgray', width=4)
    canvas2.create_oval(120, 120, 50, 50, fill='white', outline='lightgray', width=4)
    canvas3.create_oval(120, 120, 50, 50, fill='green', outline='lightgray', width=4)

play=Tk()
play.geometry('300x400')
play.title('Title')
play.configure(bg='black')

button1 = Button(play,text='RED',font='Arial',height='1',bg='lightgray',width='12',command=red)
button1.grid(row=1,column=1)
canvas1=Canvas(play,height=130,bg='black')
canvas1.grid(row=1,column=2)

button2 = Button(play,text='ORANGE',font='Arial',bg='lightgray',height='1',width='12',command=orange)
button2.grid(row=2,column=1)
canvas2=Canvas(play,height=130,bg='black')
canvas2.grid(row=2,column=2)

button3 = Button(play,text='GREEN',font='Arial',height='1',bg='lightgray',width='12',command=green)
button3.grid(row=3,column=1)
canvas3=Canvas(play,height=130,bg='black')
canvas3.grid(row=3,column=2)

play.mainloop()