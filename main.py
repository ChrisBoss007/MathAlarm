# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename


mainLabel = None
mainLabel2 = None
(h, m, s) = (None, None, None)
root = None


def alarm(): #Recrusive function
    global mainLabel

    set_alarm_time = f"{h}:{m}:{s}"
    current_time = datetime.datetime.now().strftime('%H:%M:%S')

    mainLabel['text'] = current_time #update current time in label, you can show whatever you want
    print(current_time, set_alarm_time)

    # Check whether set alarm is equal to current time or not
    if current_time == set_alarm_time:
        print("Time to Wake up")
        # Playing sound
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        messagebox.showinfo(title="ALARM", message="Alarm is going off, its time to wake up!")
        #no more need to schedule the function
    else:
        #alarm time is not reached let's recursively call the function again for one second
        root.after(1000, alarm)

def submit():
    global mainLabel
    global mainLabel2































    def load():
        global hh, mm, ss
        filename = askopenfilename()

        infoList = [line.rstrip('\n') for line in open(filename)]





        hh = infoList[0]
        mm = infoList[1]
        ss = infoList[2]

        print("File contents: ", hh, mm, ss)






        def alarm2(): #Recrusive function
            global mainLabel2

            set_alarm_time2 = f"{h}:{m}:{s}"
            current_time = datetime.datetime.now().strftime('%H:%M:%S')

            mainLabel2['text'] = current_time #update current time in label you can show whatever you want
            print(current_time, set_alarm_time2)

            # Check whether set alarm is equal to current time or not
            if current_time == set_alarm_time2:
                print("Time to Wake up")
                # Playing sound
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                messagebox2.showinfo(title="ALARM", message="Alarm is going off, its time to wake up!")
                #no more need to schedule the function
            else:
                #alarm time is not reached let's recursively call the function again for one second
                root.after(1000, alarm2)


        def start2():
            global h, m, s, hours2, mins2, secs2


            print('scheduling alarm')


            h = hour2.get()
            m = minute2.get()
            s = second2.get()
            (hours2, mins2, secs2) = (int(h), int(m), int(s))
            root.after(1000, alarm2)




        root = Tk()
        root.geometry("400x300")
        root.config(bg="#447c84")
        root.title('MathAlarm')


        # Add Labels, Frame, Button, Optionmenus
        Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="Black").pack(pady=10)
        mainLabel2 = Label(root,text="Set Time",font=("Helvetica 15 bold"))
        mainLabel2.pack()

        frame2 = Frame(root)
        frame2.pack()

        UsersH = (int(hh))

        hour2 = StringVar(root)
        hours2 = (UsersH, '00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23', '24'
                )
        hour2.set(hours2[0])

        hrs2 = OptionMenu(frame2, hour2, *hours2)
        hrs2.pack(side=LEFT)

        UsersM = (int(mm))

        minute2 = StringVar(root)
        minutes2 = (UsersM, '00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23',
                '24', '25', '26', '27', '28', '29', '30', '31',
                '32', '33', '34', '35', '36', '37', '38', '39',
                '40', '41', '42', '43', '44', '45', '46', '47',
                '48', '49', '50', '51', '52', '53', '54', '55',
                '56', '57', '58', '59', '60')
        minute2.set(minutes2[0])

        mins2 = OptionMenu(frame2, minute2, *minutes2)
        mins2.pack(side=LEFT)

        UsersS = (int(ss))

        second2 = StringVar(root)
        seconds2 = (UsersS, '00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23',
                '24', '25', '26', '27', '28', '29', '30', '31',
                '32', '33', '34', '35', '36', '37', '38', '39',
                '40', '41', '42', '43', '44', '45', '46', '47',
                '48', '49', '50', '51', '52', '53', '54', '55',
                '56', '57', '58', '59', '60')
        second2.set(seconds2[0])

        secs2 = OptionMenu(frame2, second2, *seconds2)
        secs2.pack(side=LEFT)

        Button(root,text="Set Alarm",font=("Helvetica 15"), command=start2).pack(pady=20)
        Button(root,text="Exit",font=("Helvetica 15"), command=lambda:root.destroy()).pack(pady=20)


































    def save():
        global h, m, s, hours, mins, secs

        alarmname = simpledialog.askstring("Input", "What would you like to call this alarm?",
                                parent=root)
        if alarmname is not None:
            print("Your alarm name name is ", alarmname)
        else:
            print("You name your alarm")

        hui = hour.get()
        mui = minute.get()
        sui = second.get()


        file = open(alarmname, 'a')
        file.write(hui)
        file.write('\n')
        file.write(mui)
        file.write('\n')
        file.write(sui)
        file.close()

    def start():
        global h, m, s, hours, mins, secs

        print('scheduling alarm')
        h = hour.get()
        m = minute.get()
        s = second.get()
        (hours, mins, secs) = (int(h), int(m), int(s))
        root.after(1000, alarm)

    root = Tk()
    root.geometry("400x600")
    root.config(bg="#447c84")
    root.title('MathAlarm')

    # Add Labels, Frame, Button, Optionmenus
    Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="Black").pack(pady=10)
    mainLabel = Label(root,text="Set Time",font=("Helvetica 15 bold"))
    mainLabel.pack()

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

    Button(root,text="Set Alarm",font=("Helvetica 15"), command=start).pack(pady=20)
    Button(root,text="Exit",font=("Helvetica 15"), command=lambda:root.destroy()).pack(pady=20)
    Button(root,text="Save Alarm",font=("Helvetica 15"), command=save).pack(pady=20)
    load = Button(root, text="Load", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=load)
    load.pack()

root = Tk()
root.title('MathAlarm')
root.geometry('347x400')
root.config(bg="#447c84")

welcomelabel = Label(root, text="Welcome to Math Alarm", font=("Times", "24", "bold"))
welcomelabel.pack()

ext = Button(root, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:root.destroy())
reg = Button(root, text="Create new Alarm", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=submit)

ext.pack()
reg.pack()

root.mainloop()
