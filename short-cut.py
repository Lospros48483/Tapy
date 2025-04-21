import tkinter as tk
from tkinter import ttk
from os import system
import subprocess

def app_1():
    system('start https://github.com') # opens Github webpage

def app_2():
    system('start chrome.exe') #opens chrome

def app_3():
    system('start explorer.exe') # opens the file explorer

def app_4():
    system('powershell start code') # opens visual code studio

def app_5():
    system('start cmd') # starts command prompe

def app_6():
    obs_dir = r"C:\Program Files\obs-studio\bin\64bit" # cd into this folder
    exe_path = f"{obs_dir}\\obs64.exe" # the exe directory
    subprocess.run([exe_path], cwd=obs_dir) # runs everything

def app_7():
    system('start notepad++.exe') #opens notepad++

def app_8():
    system('start snippingtool.exe') # opens snipping tool

def app_9():
    system('start https://open.spotify.com') # opens the link to spotify (if you downloded frome the microsoft store you can use that).

def app_10():
    system('start https://mail.google.com') # opens the link to google mail

root = tk.Tk()
root.config(width=200, height=350)
root.title("Phone")

buton_1 = ttk.Button(text="Github", command=app_1)
buton_1.place(x=60, y=40)

buton_2 = ttk.Button(text="Chrome", command=app_2)
buton_2.place(x=60, y=65)

buton_3 = ttk.Button(text="File Manager", command=app_3)
buton_3.place(x=60, y=90)

buton_4 = ttk.Button(text="VS Code", command=app_4)
buton_4.place(x=60, y=115)

buton_5 = ttk.Button(text="Terminal", command=app_5)
buton_5.place(x=60, y=140)

buton_6 = ttk.Button(text="OBS", command=app_6)
buton_6.place(x=60, y=165)

buton_7 = ttk.Button(text="Notepad++", command=app_7)
buton_7.place(x=60, y=190)

buton_8 = ttk.Button(text="Cut Picture", command=app_8)
buton_8.place(x=60, y=215)

buton_9 = ttk.Button(text="Spotify", command=app_9)
buton_9.place(x=60, y=240)

buton_10 = ttk.Button(text="Gmail", command=app_10)
buton_10.place(x=60, y=265)

root.mainloop()