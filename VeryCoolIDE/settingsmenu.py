import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json


window = tk.Tk()

w = open('config/theme.txt', 'r+')
lines = w.readlines()
themecolour = w
window.geometry('807x380')
window.tk.call("source", "sun-valley.tcl")
window.tk.call("set_theme", "dark")

a = ttk.Combobox(window, textvariable=tk.StringVar())
a['values'] = ("dark", "light")
a.pack()




def a_changed(event):
   print("You Selected " + a.get())
   themecolour = a.get()
   window.tk.call("set_theme", themecolour)
   w = open('config/theme.txt', 'r+')
   lines = w.readlines()
   w.seek(0)
   w.truncate(4)
   w.write(themecolour)
   

      
   


       
   #w.write(themecolour)






a.bind('<<ComboboxSelected>>', a_changed)

window.title("VeryCoolIDE - Settings")
window.mainloop()



#print(variable.get())
