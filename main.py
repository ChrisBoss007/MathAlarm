# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
from tkinter import messagebox

def submit():

    def alarm(Curent):
        # Infinite Loop
        while True:
            # Set Alarm
            set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

            # Wait for one seconds
            time.sleep(1)

            # Get current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time,set_alarm_time)


            # Check whether set alarm is equal to current time or not
            if current_time == set_alarm_time:
                print("Time to Wake up")
                # Playing sound
                winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                messagebox.showinfo(title="ALARM", message="Alarm is going off, its time to wake up!")
                break


    root = Tk()
    root.geometry("400x300")
    root.config(bg="#447c84")
    root.title('MathAlarm')

    # Add Labels, Frame, Button, Optionmenus
    Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="Black").pack(pady=10)
    Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

    frame = Frame(root)
    frame.pack()

    hour = StringVar(root)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23', '24'
            )
    hour.set(hours[0])

    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)

    minute = StringVar(root)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')
    minute.set(minutes[0])

    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)

    second = StringVar(root)
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')
    second.set(seconds[0])

    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)

    Button(root,text="Set Alarm",font=("Helvetica 15"),command=alarm).pack(pady=20)
    Button(root,text="Exit",font=("Helvetica 15"), command=lambda:root.destroy()).pack(pady=20)

#his is the window configuration
root = Tk()
root.title('MathAlarm')
root.geometry('347x400')
root.config(bg="#447c84")

#This is a label that just wlecome the users.
welcomelabel = Label(root, text="Welcome to Math Alarm", font=("Times", "24", "bold"))
welcomelabel.pack()

#Here are two button that will ither exit the aplication by using the root destory command, or it will run the submit function whitch will open the alarm window.
ext = Button(root, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:root.destroy())
reg = Button(root, text="Create new Alarm", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=submit)
ext.pack()
reg.pack()

# Execute Tkinter
root.mainloop()








