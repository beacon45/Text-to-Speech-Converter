from tkinter import *
#from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.geometry("900x450")
root.title('Burger Speech')
root.configure(bg="#35b8c4")
root.resizable(False,False)
root.wm_iconbitmap("icon.ico")

engine=pyttsx3.init()
#Functions
def speakNow():
    text=text_area.get(1.0, END)
    gender=gen_values.get()
    speed=speed_values.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender== 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if (speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

#Head Part
top_frame=Frame(root,bg="#e0db6e",highlightbackground="black",highlightthickness=2,width=900,height=100)
top_frame.place(x=0,y=4)

#logo
logo=PhotoImage(file="microphone.png")
Label(top_frame,image=logo,bg="#e0db6e").place(x=10,y=5)
Label(top_frame,text="Listen Burger",font="forte 38 bold",bg="#e0db6e",fg="red").place(x=100,y=20)

#Text Area
text_area=Text(root,font="calibri 14",relief=GROOVE)
text_area.place(x=10,y=130,width=500,height=280)

#comboBox
Label(root,text='VOICE',bg="#35b8c4",font="candara 18 bold",fg="black").place(x=580,y=130)
Label(root,text='SPEED',bg="#35b8c4",font="candara 18 bold",fg="black").place(x=775,y=130)

gen_values=Combobox(root,values=['Male','Female'],font="calibri 14",state='r',width=10)
gen_values.place(x=550,y=170)
gen_values.set('Male')

speed_values=Combobox(root,values=['Fast','Medium','Slow'],font="calibri 14",state='r',width=10)
speed_values.place(x=750,y=170)
speed_values.set('Normal')

#Button


play_icon=PhotoImage(file="play.png")
play_btn=Button(root,compound=LEFT,image=play_icon,bg="#35b8c4",command=speakNow)
play_btn.place(x=575,y=270)

save_icon=PhotoImage(file="save.png")
save_btn=Button(root,compound=LEFT,image=save_icon,bg="#35b8c4")
save_btn.place(x=775,y=270)


root.mainloop()
