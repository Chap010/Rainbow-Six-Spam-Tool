from ctypes import pythonapi
from tkinter import *
import tkinter
from tkinter import font 
from tkinter import ttk
from tkinter import messagebox
import pyautogui
import time




# Logo 


# App GUi
RainbowSpammer = Tk()
RainbowSpammer.title('Rainbow Siege Chat Spammer')
RainbowSpammer.geometry('550x300')
RainbowSpammer.resizable(width=0, height=0)
RainbowSpammer.configure(background="#282e3e")

# App Content
Dev = Label(RainbowSpammer, text="Creator: Greaser", font="Arial", bg="#1b1d28", fg="Green")
Dev.pack(side="bottom")

var = IntVar()
frame = LabelFrame(RainbowSpammer, text='Pick A Selection',bg="#282e3e", fg="white",)
frame.pack(pady=10)
Radiobutton(frame, text='3 spams', variable=var, value=1, bg="#282e3e", fg="green").grid(row=0, column=1)
Radiobutton(frame, text="5 spams", variable=var, value=2, bg="#282e3e", fg="green").grid(row=0, column=2)
Radiobutton(frame, text="7 spams", variable=var, value=3, bg="#282e3e", fg="green").grid(row=1, columnspan=3)


input_data = Entry(RainbowSpammer, width='30', bg="#1b1d28", fg="white",)
input_data.pack()
input_data.insert(0,"Enter Text")   
input_data.place(x=180, y=100) 

def sendClick():  
    global Spam_send  
    text = input_data.get()

    for i in range(3): 
        time.sleep(1)
        pyautogui.moveTo(840, 460)
        pyautogui.doubleClick(840,60)
        pyautogui.write(input_data)
        #pyautogui.press('t')
        pyautogui.write(input_data)
        
        pyautogui.press('enter')


                                                                        
        Spam_send = Label(RainbowSpammer, text="Spam Send! ", font="Arial", bg="#282e3e", fg="white")
        Spam_send.place(x=405, y=150) 

Send_Spam_button = Button(RainbowSpammer, text='Send Spam', width='10', height='2', font="Arial", bg="#20bebe", fg="white", command=sendClick )
Send_Spam_button.place(x=130, y=150)

def spamDelete():
    Send_Spam_button.pack_forget()

def clearedClick():
    Clear_Text = Label(RainbowSpammer, text="", font="Arial", bg="#282e3e", fg="white", )
    Clear_Text.place(x=405, y=150)
    #Send_Spam.pack_forget()
    input_data.configure(state=NORMAL)
    input_data.delete(0, END)

Clear_button = Button(RainbowSpammer, text='Clear', width='10', height='2', font="Arial", bg="#20bebe", fg="white", command=lambda:[spamDelete(), clearedClick()])
Clear_button.place(x=300, y=150) 

# Fail-safe trigger mouse 

RainbowSpammer.mainloop()



