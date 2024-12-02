import tkinter as tk
from tkinter import messagebox
import keyboard
from pynput.mouse import Button, Controller
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

mouse = Controller()

MouseButtons={
    "left":Button.left,
    "middle":Button.middle,
    "right":Button.right
    }


def click(duration=0.0,button=Button.left):
    mouse.press(button)
    time.sleep(duration)
    mouse.release(button)

def clicker_tool(keypress='s', clicks=2, key='left', interval=0.0, duration=0.0, cps_precision=0.1):
    m=False
    button=MouseButtons[key]
    while True:
        if keyboard.is_pressed(keypress):
            m=True
            print('Autoclicker turned on')
            time.sleep(0.15)
        c = 0.00001
        tim=time.monotonic()
        s=0.0
        cps="N/A"
        while m:                
            if keyboard.is_pressed(keypress):
                print(cps,'cps reached')
                m=False
                print('Autoclicker turned off') 
                time.sleep(0.15)
                break
                
            click(duration,button)
            c+=1
            cps = c/(time.monotonic()-tim+0.0001)
            if clicks < cps:
                s+=cps_precision
                    
            elif clicks > cps:
                s-=cps_precision
                if s<0.0:
                    s=0.0
            time.sleep(s)
                
                
            lm=time.monotonic()
            while interval > time.monotonic()-lm:
                if keyboard.is_pressed(keypress):
                    print(cps,'cps reached')
                    m=False
                    time.sleep(0.15)
                    break
                

def clicker():
    try:
        clicks = float(entry_click.get())
        keypress = entry_keypress.get()
        key = entry_key.get()
        interval = float(entry_interval.get())
        duration = float(entry_duration.get())
        precision = float(entry_precision.get())
    except ValueError:
        if entry_click.getboolean(): clicks = 10.01
        else: clicks = float(entry_click.get())
        if entry_keypress.getboolean(): keypress = 's'
        else: keypress = entry_keypress.get()
        if entry_key.getboolean(): key = 'left'
        else: key = entry_key.get()
        if entry_interval.getboolean(): interval = 0.0
        else: interval = float(entry_interval.get())
        if entry_duration.getboolean(): duration = 0.0
        else: duration = float(entry_duration.get())
        if entry_precision.getboolean(): precision = 0.1
        else: precision = float(entry_precision.get())
    messagebox.showinfo("Clicker starting", "Clicker is started with "+str(clicks)+" press,"+key+" key, "+str(interval)+" interval !!.\nPress | "+keypress+" | key for start clicker !!")
    clicker_tool(keypress, clicks, key, interval, duration, precision)

root = tk.Tk()

label_click = tk.Label(root, text="Clicks per second")
label_click.pack()
entry_click = tk.Entry(root)
entry_click.pack()

label_keypress = tk.Label(root, text="Start/Stop key")
label_keypress.pack()
entry_keypress = tk.Entry(root)
entry_keypress.pack()


label_key = tk.Label(root, text="Button would you press")
label_key.pack()
entry_key = tk.Entry(root)
entry_key.pack()

label_interval = tk.Label(root, text="Interval for clicks")
label_interval.pack()
entry_interval = tk.Entry(root)
entry_interval.pack()

label_duration = tk.Label(root, text="Click duration")
label_duration.pack()
entry_duration = tk.Entry(root)
entry_duration.pack()

label_precision = tk.Label(root, text="Cps precision")
label_precision.pack()
entry_precision = tk.Entry(root)
entry_precision.pack()

start_clicker = tk.Button(root, text="Start", command=clicker)
start_clicker.pack()

root.mainloop()
