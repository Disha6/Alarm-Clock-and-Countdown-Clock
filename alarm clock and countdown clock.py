from tkinter import *
import tkinter as tk
from tkinter import font as tkfont
import datetime
import time
import math
import webbrowser
 #import sys
 #import tkinter.messagebox as box


class MainClass(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size='30', weight='bold', slant='italic')
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.geometry()

        # This is the code that makes it possible to switch
        # between windows in the same frame
        self.frames = {}
        for F in (MainWindow, AlarmClock, Countdown):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # Main window that shows on startup
        self.show_frame(MainWindow)

        # Title on the frame
        self.title('Alarm clock')

    # Definition on the main menu, evidence form and investigation
    # record button, which makes it possible to switch between classes in the same window
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text='Clock', font=controller.title_font)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='Alarm clock',
                            command=lambda: controller.show_frame(AlarmClock))
        button1.pack(padx=10, pady=10)

        button2 = tk.Button(self, text='Countdown',
                            command=lambda: controller.show_frame(Countdown))
        button2.pack(padx=10, pady=10)

        
        button3 = tk.Button(self, text='Quit',
                            command=lambda: PopUpConfirmQuit(self))
        button3.pack(padx=10, pady=10)


class AlarmClock(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # self.hour = hour

        tk.Label(self, text='Alarm clock\n').grid(row=1, column=4)

        current_time = tk.Label(self, font=('times', 20, 'bold'))
        current_time.grid(row=2, columns=12)

        tk.Label(self, text='Hour:').grid(row=3, column=3)

        alarm_hour_entry = Entry(self, width=10)
        alarm_hour_entry.grid(row=3, column=4)

        tk.Label(self, text='Minute:').grid(row=4, column=3)

        alarm_minute_entry = Entry(self, width=10)
        alarm_minute_entry.grid(row=4, column=4)

        tk.Label(self, text='Monday').grid(row=7, column=1)
        tk.Label(self, text='Tuesday').grid(row=7, column=2)
        tk.Label(self, text='Wednesday').grid(row=7, column=3)
        tk.Label(self, text='Thursday').grid(row=7, column=4)
        tk.Label(self, text='Friday').grid(row=7, column=5)
        tk.Label(self, text='Saturday').grid(row=7, column=6)
        tk.Label(self, text='Sunday').grid(row=7, column=7)

        monday_box = tk.Checkbutton(self)
        monday_box.grid(row=10, column=1)

        tuesday_box = tk.Checkbutton(self)
        tuesday_box.grid(row=10, column=2)

        wednesday_box = tk.Checkbutton(self)
        wednesday_box.grid(row=10, column=3)

        thursday_box = tk.Checkbutton(self)
        thursday_box.grid(row=10, column=4)

        friday_box = tk.Checkbutton(self)
        friday_box.grid(row=10, column=5)

        saturday_box = tk.Checkbutton(self)
        saturday_box.grid(row=10, column=6)

        sunday_box = tk.Checkbutton(self)
        sunday_box.grid(row=10, column=7)

        create = tk.Button(self, text='Create alarm', command=lambda: create_alarm())
        create.grid(row=11, column=4)

        def create_alarm():
            remaining_time = 0
            while remaining_time < 1:
                if time.localtime().tm_hour == alarm_hour_entry.get() and \
                        time.localtime().tm_min == alarm_minute_entry.get():
                    webbrowser.open_new('https://www.youtube.com/watch?v=iNpXCzaWW1s')
                else:
                    remaining_time = remaining_time + 1

        def tick():
            global time_label
            time_label = time.strftime('%H:%M:%S')
            current_time.config(text=time_label)
            current_time.after(200, tick)

        # tk.Label(self, text=).grid(row=12, column=3)

        tk.Button(self, text="Main menu", command=lambda: controller.show_frame(MainWindow)).grid(row=13, column=1)

        tk.Button(self, text="Quit", command=lambda: PopUpConfirmQuit(self)).grid(row=13, column=10)

        tick()


class PopUpConfirmQuit(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Are you sure you want to quit?").grid(row=1, column=1)
        tk.Button(self, text='Yes', command=lambda: self.quit()).grid(row=2, column=1, padx=8, pady=5)
        tk.Button(self, text='No', command=self.destroy).grid(row=2, column=2, padx=8, pady=5)
        PopUpConfirmQuit.minsize(self, width=100, height=75)




class Countdown(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def down_count(count):
            seconds = math.floor(count % 60)
            minutes = math.floor((count / 60) % 60)
            hours = math.floor((count / 3600))
            label['text'] = "Hours: " + str(hours) + " Minutes:  " + str(minutes) + " Seconds: " + str(seconds)

            if count >= 0:
                self.after(1000, down_count, count - 1)
            else:
                for x in range(1):
                    webbrowser.open_new('https://www.youtube.com/watch?v=iNpXCzaWW1s')
                    label['text'] = "Time is up!"

        def update_button():
            hour, minute, sec = hours_entry.get(), minute_entry.get(), second_entry.get()
            if hour.isdigit() and minute.isdigit() and sec.isdigit():
                time_left = int(hour) * 3600 + int(minute) * 60 + int(sec)
                down_count(time_left)

        tk.Label(self, text='Hours:').grid(row=1, column=1)
        hours_entry = tk.Entry(self)
        hours_entry.grid(row=1, column=2)
        tk.Label(self, text='Minutes:').grid(row=2, column=1)
        minute_entry = tk.Entry(self)
        minute_entry.grid(row=2, column=2)
        tk.Label(self, text='Seconds:').grid(row=3, column=1)
        second_entry = tk.Entry(self)
        second_entry.grid(row=3, column=2)
        label = tk.Label(self)
        label.grid(row=5, column=2)

        button = tk.Button(self, text='Start Timer', command=update_button)
        button.grid(row=4, column=2)

        tk.Button(self, text='Main menu', command=lambda: controller.show_frame(MainWindow)).grid(row=6, column=1)

        tk.Button(self, text='Quit', command=lambda: PopUpConfirmQuit(self)).grid(row=6, column=3)


app = MainClass()
app.minsize(width=400, height=400)
app.maxsize(width=700, height=750)
app.mainloop()
