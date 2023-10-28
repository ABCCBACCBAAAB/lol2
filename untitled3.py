# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:41:01 2023

@author: Marcus
"""

import tkinter as tk
window = tk.Tk()
window.title("buttom")
window.geometry("500x500")
string = tk.StringVar()
def selection():
    label.config(text="LOL" + string.get())
label = tk.Label(window, bg='#f00',text='LOL')
label.pack()


radio = tk.Radiobutton(window,
                       text="P2W",
                       variable=string, value="P2W",
                       command=selection)
radio.pack()
radio2 = tk.Radiobutton(window,
                       text="Hacker",
                       variable=string, value="Hacker",
                       command=selection)
radio2.pack()
radio3 = tk.Radiobutton(window,
                       text="Bow spamer",
                       variable=string, value="Bow spamer",
                       command=selection)
radio3.pack()
radio4 = tk.Radiobutton(window,
                       text="atuo cliker",
                       variable=string, value="atuo cliker",
                       command=selection)
radio4.pack()
radio5 = tk.Radiobutton(window,
                       text="toxit",
                       variable=string, value="toxit",
                       command=selection)

radio5.pack()
gender = tk.StringVar()
gender.set("boy")
radio6 = tk.Radiobutton(window,
                       text="boy",
                       variable=gender, value="boy",
                       command=selection)

radio6.pack()
radio7 = tk.Radiobutton(window,
                       text="girl",
                       variable=gender, value="girl",
                       command=selection)

radio7.pack()
window.mainloop()

                       