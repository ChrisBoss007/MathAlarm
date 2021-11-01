from tkinter import *
import re
from tkinter import messagebox
import sqlite3
import random
import smtplib
import datetime
import time
import winsound


ws = Tk()
ws.title('Python Guides')
ws.geometry('500x400')
ws.config(bg="#447c84")
ws.attributes('-fullscreen',True)

def submit():
    ws = Tk()
    ws.title('Python Guides')
    ws.geometry('500x400')
    ws.config(bg="#447c84")
    ws.attributes('-fullscreen',True)

    frame = Frame(ws, padx=20, pady=20)
    frame.pack(expand=True)

    Label(
        frame,
        text="Create Alarm",
        font=("Times", "24", "bold")
        ).grid(row=0, columnspan=3, pady=10)
    Label(
        frame,
        text = "Set Time for Alarm: ",
        fg="white",
        bg="#922B21",
        relief = "solid",
        font=("Helevetica",15,"bold")
        ).grid(row=1, columnspan=3, pady=10)

    Entry(frame,textvariable = hour,bg = "#48C9B0",font=(20)).grid(row=3, column=1)
    Entry(frame,textvariable = min,bg = "#48C9B0",font=(20)).grid(row=3, column=2)
    Entry(frame,textvariable = sec,bg = "#48C9B0",font=(20)).grid(row=3, column=3)

    ext2 = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:ws.destroy())
    reg2 = Button(frame, text="Set Alarm", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"))
    ext2.grid(row=6, column=2, pady=20)
    reg2.grid(row=6, column=1, pady=25)




# frames
frame = Frame(ws, padx=20, pady=20)
frame.pack(expand=True)

# labels
Label(
    frame,
    text="Welcome to Math Alarm",
    font=("Times", "24", "bold")
    ).grid(row=0, columnspan=3, pady=10)

ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:ws.destroy())
reg = Button(frame, text="Create new Alarm", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=submit)
ext.grid(row=6, column=2, pady=20)
reg.grid(row=6, column=1, pady=25)
ws.mainloop()
