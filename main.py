from tkinter import *
#import re
from tkinter import messagebox
#import sqlite3
#import random
#import smtplib
import datetime
import time
import winsound


def submit():
    def Alarm(set_alarm_timer):
        while True:
            time.sleep(1)
            actual_time = datetime.datetime.now()
            cur_time = actual_time.strftime("%H:%M:%S")
            cur_date = actual_time.strftime("%d/%m/%Y")
            msg="Current Time: "+str(cur_time)
            print(msg)
            if cur_time == set_alarm_timer:
                winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
                ws.messagebox.showinfo("Alarm")
                break

    def get_alarm_time():
        alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
        Alarm(alarm_set_time)

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

    #def clear_search(event):
        #search.delete(0, tk.END)

    hour = StringVar()
    min = StringVar()
    sec = StringVar()

    HoursEntry = Entry(frame, width=8, textvariable = hour)
    #HoursEntry.insert(0, "Hours")
    HoursEntry.grid(row=2, column=1, columnspan=1)
    #HoursEntry.bind("<Button-1>", clear_search)

    MinutesEntry = Entry(frame, width=8, textvariable = min)
    #MinutesEntry.insert(0, "Minutes")
    MinutesEntry.grid(row=2, column=2)
    #MinutesEntry.bind("<Button-1>", clear_search)

    SecondsEntry = Entry(frame, width=8, textvariable = sec)
    #SecondsEntry.insert(0, "Seconds")
    SecondsEntry.grid(row=2, column=3)
    #SecondsEntry.bind("<Button-1>", clear_search)



    ext2 = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:ws.destroy())
    reg2 = Button(frame, text="Set Alarm", padx=20, pady=10, relief=SOLID,command = get_alarm_time,font=("Times", "14", "bold"))
    ext2.grid(row=6, column=2, pady=20)
    reg2.grid(row=6, column=1, pady=25)


ws = Tk()
ws.title('Python Guides')
ws.geometry('500x400')
ws.config(bg="#447c84")
ws.attributes('-fullscreen',True)



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
