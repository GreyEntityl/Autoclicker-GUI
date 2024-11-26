import tkinter as tk
from tkinter import messagebox
#import pyautogui
import keyboard

import os

import time


from pynput.mouse import Button, Controller

import time
import os

mouse = Controller()
#from time import sleep

global isMouse
isMouse = True

MouseButtons={
    "left":Button.left,
    "middle":Button.middle,
    "right":Button.right
    }


def click(duration=0.0,button=Button.left):
    mouse.press(button)
    time.sleep(duration)
    mouse.release(button)

#def entryTry (entry, entry_get):
#    entry = entry_get.get()
#    return entry


def clicker_tool(keypress='s', key='left', interval=0.0, duration=0.0):
    m=False
    button=MouseButtons[key]
    while True:
        if keyboard.is_pressed(keypress):
            m=True
            print('Autoclicker turned on')
            time.sleep(0.5)
        tim=time.monotonic()
        c=0
        cps="N/A"
        while m:                
            if keyboard.is_pressed(keypress):
                print(cps,'cps reached')
                m=False
                print('Autoclicker turned off') 
                time.sleep(0.5)
                break
                
            click(duration,button) # The line `lm=time.mono` seems to be incomplete and contains a typo.
            c+=1        # It should be `lm = time.monotonic()`.
            cps = c/(time.monotonic()-tim+0.0001)
            
            lm=time.monotonic()
            while interval > time.monotonic()-lm:
                if keyboard.is_pressed(keypress):
                    print(cps,'cps reached')
                    m=False
                    time.sleep(0.5)
                    break
                

def clicker():
    try:
        keypress = entry_keypress.get()
        key = entry_key.get()
        interval = float(entry_interval.get())
        duration = float(entry_duration.get())

    except ValueError:
        if entry_keypress.getboolean(): keypress = 's'
        else: keypress = entry_keypress.get()
        if entry_key.getboolean(): key = 'left'
        else: key = entry_key.get()
        if entry_interval.getboolean(): interval = 0.0
        else: interval = float(entry_interval.get())
        if entry_duration.getboolean(): duration = 0.0
        else: duration = float(entry_duration.get())
    if isMouse:
        messagebox.showinfo("Clicker","Starting with "+key+" mouse button, "+str(interval)+" interval and "+str(duration)+" per clicks !!.\nPress | "+str(keypress)+" | key for start clicker !!")
    else:
        messagebox.showinfo("Clicker","Starting with "+key+" key, "+str(interval)+" interval !!.\nPress | "+str(keypress)+" | key for start clicker !!")
    clicker_tool(keypress, key, interval, duration)
    
# Create the main window

root = tk.Tk()


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

# Connect button
start_clicker = tk.Button(root, text="Start", command=clicker)
start_clicker.pack()


# Run the main loop
root.mainloop()
