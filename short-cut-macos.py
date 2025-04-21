import tkinter as tk
from tkinter import ttk
from os import system
import subprocess

def app_1():
    system('open -u https://github.com') # opens Github webpage

def app_2():
    system('open -a Arc') #opens Arc

def app_3():
    system('open -a finder') # opens the finder

def app_4():
    system('code') # opens visual code studio (need to activate shell!)

def app_5():
    system('open -a terminal') # starts terminal

def app_6():
    system('open -a obs') # opens OBS

def app_7():
    system('open -a TextEdit') #opens the basic MacOS text editor

def app_8():
    system('open -a Screenshot') # opens screenchots

def app_9():
    system('open -u https://open.spotify.com') # opens the link to spotify

def app_10():
    system('open -u https://mail.google.com') # opens the link to google mail

root = tk.Tk()
root.config(width=200, height=350)
root.title("Phone")

buton_1 = ttk.Button(text="Github", command=app_1)
buton_1.place(x=60, y=40)

buton_2 = ttk.Button(text="Arc", command=app_2)
buton_2.place(x=60, y=65)

buton_3 = ttk.Button(text="Finder", command=app_3)
buton_3.place(x=60, y=90)

buton_4 = ttk.Button(text="VS Code", command=app_4)
buton_4.place(x=60, y=115)

buton_5 = ttk.Button(text="Terminal", command=app_5)
buton_5.place(x=60, y=140)

buton_6 = ttk.Button(text="OBS", command=app_6)
buton_6.place(x=60, y=165)

buton_7 = ttk.Button(text="Text Editor", command=app_7)
buton_7.place(x=60, y=190)

buton_8 = ttk.Button(text="Screenshot", command=app_8)
buton_8.place(x=60, y=215)

buton_9 = ttk.Button(text="Spotify", command=app_9)
buton_9.place(x=60, y=240)

buton_10 = ttk.Button(text="Gmail", command=app_10)
buton_10.place(x=60, y=265)

root.mainloop()
