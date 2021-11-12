# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename

#This is where i set the main componets to none so that when i use the global command it has a pre value of 0.
mainLabel = None
mainLabel2 = None
(h, m, s) = (None, None, None)
root = None

#Recrusive function
#This fuction will run when the user has
def alarm():
    global mainLabel

    #This is where i get the values the users sets and saves them under the varible "set_alarm_time"., which will then take that also gets the values of the curent time in comparisin to the computer time
    set_alarm_time = f"{h}:{m}:{s}"
    current_time = datetime.datetime.now().strftime('%H:%M:%S')

    #This will convert the mail label into a coundown by setting the text of the alarm to the curent time, and becuse it is in a loop it will update evry second,making it a coundown.
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
        #alarm time is not reached let's recursively call the function again for one second.
        root.after(1000, alarm)


#This is the function that will run once the users was clicked the "Create new alarm" button.
#This fuction has the main code contain all the smaller fuction that preform the bulk of the code.
def CreateNewAlarm():
    global mainLabel
    global mainLabel2


    #This function will run when the user clickes the "Load" button
    #This fuction then opens the file and gets the time in that file, which was set byt ryh suers when saving the alarm.
    def loadAlarm():
        global hh, mm, ss

        #This is where the program asks the use to slected the file they saved
        filename = askopenfilename()

        #This is where i strip the uneeded content of the file, into only the nessacery conctent.
        infoList = [line.rstrip('\n') for line in open(filename)]

        #This is where i set varible names for the times in the file.
        hh = infoList[0]
        mm = infoList[1]
        ss = infoList[2]

        print("File contents: ", hh, mm, ss)


        #This function will run automaticaly after the users has satrted the alarm.
        # Recrusive function
        def alarm2():
            global mainLabel2

            # This is where i get the values the users sets and saves them under the varible "set_alarm_time"., which will then take that also gets the values of the curent time in comparisin to the computer time
            set_alarm_time2 = f"{h}:{m}:{s}"
            current_time = datetime.datetime.now().strftime('%H:%M:%S')

            # This will convert the mail label into a coundown by setting the text of the alarm to the curent time, and becuse it is in a loop it will update evry second,making it a coundown.
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


        #This function will run after the users clciks the "Staer alarm" button.
        #This function will fetch the values from the file and automaticly run start the alarm after a period of time.
        def startAlarm2():
            global h, m, s, hours2, mins2, secs2

            print('scheduling alarm')

            h = hour2.get()
            m = minute2.get()
            s = second2.get()
            (hours2, mins2, secs2) = (int(h), int(m), int(s))
            root.after(1000, alarm2)
            #-------------------------------------------------------------------------------------------------------------------------------------------



        # This is the configuration for the first window whitch will open upon running the program.
        root = Tk()
        root.geometry("400x300")
        root.config(bg="#447c84")
        root.title('MathAlarm')

        # Add Labels, Frame, Button, Optionmenus
        Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="Black").pack(pady=10)

        # This is the main label whitch says "Set Time", but once the alarm is set this label will convert into a countodown, counting dow till the alarm goes off.
        mainLabel2 = Label(root,text="Set Time",font=("Helvetica 15 bold"))
        mainLabel2.pack()

        # This is a frame that holds the 3 option meuns, i used it beacuse it is eariset than having to give each option meun a varible name
        frame2 = Frame(root)
        frame2.pack()

        #This is where i set the first default option in the option meun to the nukber from the opened file.
        UsersH = (int(hh))

        # This is where i set all the option in the optionmeun that the user will use to select the time they want, that time will then but put in the "Hours list", whitch will be passed onto the next part of the code.
        hour2 = StringVar(root)
        hours2 = (UsersH, '00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23', '24'
                )
        hour2.set(hours2[0])

        # This is where i make a option menu for the hours slot.
        hrs2 = OptionMenu(frame2, hour2, *hours2)
        hrs2.pack(side=LEFT)

        # This is where i set the first default option in the option meun to the nukber from the opened file.
        UsersM = (int(mm))

        # This is where i set all the option in the optionmeun that the user will use to select the time they want, that time will then but put in the "Minutes list", whitch will be passed onto the next part of the code.
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

        # This is where i make a option menu for the minutes slot.
        mins2 = OptionMenu(frame2, minute2, *minutes2)
        mins2.pack(side=LEFT)

        # This is where i set the first default option in the option meun to the nukber from the opened file.
        UsersS = (int(ss))

        # This is where i set all the option in the optionmeun that the user will use to select the time they want, that time will then but put in the "Seconds list", whitch will be passed onto the next part of the code.
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

        # This is where i make a option menu for the seconds slot.
        secs2 = OptionMenu(frame2, second2, *seconds2)
        secs2.pack(side=LEFT)

        #Here are two button on this window.
        #The first button will run the "SetAlarm2" fuction whitch will
        Button(root,text="Set Alarm",font=("Helvetica 15"), command=startAlarm2).pack(pady=20)
        Button(root,text="Exit",font=("Helvetica 15"), command=lambda:root.destroy()).pack(pady=20)
        #--------------------------------------------------------------------------------------------------------------------------------------------



    #This function will run once the "Save" button is clicked.
    #This fuction will ask the user to name thier alarm and then take the values the user put in and save that information to a file with the name set by the user as the alarm name.
    def saveAlarm():
        global h, m, s, hours, mins, secs

        alarmname = simpledialog.askstring("Input", "What would you like to call this alarm?",
                                parent=root)
        if alarmname is not None:
            print("Your alarm name name is ", alarmname)
        else:
            print("You name your alarm")

        #This is where i use the .get() command to fetch the values that the users has put in and then i save them to a varilbe whitch will be used to write onto a file on the users computer.
        saveH = hour.get()
        saveM = minute.get()
        saveS = second.get()

        #This is where i open the file and append into it the values that the users ahs set for thier alarm.
        file = open(alarmname, 'a')
        file.write(saveH)
        file.write('\n')
        file.write(saveM)
        file.write('\n')
        file.write(saveS)
        file.close()

    #This function will run when the user has entred the time they want the alarm to go off and clciked the "Set ALarm" button.
    #This fuction will fetch the values enetred in the option meuns and save them as a variuble which will be used in the countodown.
    def setAlarm():
        global h, m, s, hours, mins, secs

        print('scheduling alarm')
        h = hour.get()
        m = minute.get()
        s = second.get()

        #I set the new varible to int, becuase the next pice of code only takes int values.
        (hours, mins, secs) = (int(h), int(m), int(s))

        #After a period of time the alarm function is called and will run without user input.
        root.after(1000, alarm)
        #---------------------------------------------------------------------------------------------------------------------------------------------------------



    # This is the configuration for the first window whitch will open upon running the program.
    root = Tk()
    root.geometry("400x600")
    root.config(bg="#447c84")
    root.title('MathAlarm')

    # Add Labels, Frame, Button, Optionmenus.
    Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="Black").pack(pady=10)

    #This is the main label whitch says "Set Time", but once the alarm is set this label will convert into a countodown, counting dow till the alarm goes off.
    mainLabel = Label(root,text="Set Time",font=("Helvetica 15 bold"))
    mainLabel.pack()

    #This is a frame that holds the 3 option meuns, i used it beacuse it is eariset than having to give each option meun a varible name.
    frame = Frame(root)
    frame.pack()

    # This is where i set all the option in the optionmeun that the user will use to select the time they want, that time will then but put in the "Hours list", whitch will be passed onto the next part of the code.
    hour = StringVar(root)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23', '24'
            )
    hour.set(hours[0])

    # This is where i make a option menu for the hours slot.
    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)

    # This is where i set all the option in the optionmeun that the user will use to select the time they want, that time will then but put in the "Minutes list", whitch will be passed onto the next part of the code.
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

    # This is where i make a option menu for the minutes slot.
    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)

    #This is where i set all the option in the optionmeun that the user will use to select the time they want, that time will then but put in the "Seconds list", whitch will be passed onto the next part of the code.
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

    #This is where i make a option menu for the seconds slot.
    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)

    #These are button on the second window.
    #The first button is the "Save Alarm" button which will run the "SaveAlarm" fuction which will take the alarm times the user set ans ave them to a file.
    #The next button is the "Set alarm" button which will run the "SetAlarm" fuction which will take the time the user set and coundown to the curent time and then set off the alarm.
    #The last button is the exsit buton which uses the .destroy command to close the aplication
    Button(root,text="Set Alarm",font=("Helvetica 15"), command=setAlarm).pack(pady=20)
    Button(root,text="Exit",font=("Helvetica 15"), command=lambda:root.destroy()).pack(pady=20)
    Button(root,text="Save Alarm",font=("Helvetica 15"), command=saveAlarm).pack(pady=20)
    loadAlarm = Button(root, text="Load", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=loadAlarm)
    loadAlarm.pack()
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------



#This is the configuration for the first window whitch will open upon running the program.
root = Tk()
root.title('MathAlarm')
root.geometry('347x400')
root.config(bg="#447c84")

#This is simply a label that welcomes the user to the program.
welcomelabel = Label(root, text="Welcome to Math Alarm", font=("Times", "24", "bold"))
welcomelabel.pack()

#Here are two buttons, the exsit button uses the .destroy command to close the aplication. The other button will run the fuction "CreateNewAlarm" fuction.
exsitbtn = Button(root, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:root.destroy())
CreateAlarmbtn = Button(root, text="Create new Alarm", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=CreateNewAlarm)
exsitbtn.pack()
CreateAlarmbtn.pack()

#This is the mainloop.
root.mainloop()
