#!/bin/python3
from tkinter import *
from tkinter import ttk
import pyperclip as pc
import os


tk=Tk()
tk.title("Wine")
tk.geometry("700x300+600+300")
tk.configure(bg="#3F3F3F")
tk.resizable(False, False)


def check():
    if os.system("wine --version")==0:
        label1.configure(text="Найден", foreground="#00FF00")
        Start.config(state=["enabled"])
        warn.destroy()
        copy_button.destroy()
    else:
        label1.configure(text="Не найден", foreground="#FF0000")
        Start.config(state=["disabled"])

def wine():
    os.system("sudo mount binfmt_misc -t binfmt_misc /proc/sys/fs/binfmt_misc")
    os.system("sudo chmod 777 /proc/sys/fs/binfmt_misc/register")
    os.system("sudo echo ':DOSWin:M::MZ::/usr/bin/wine:' > /proc/sys/fs/binfmt_misc/register")
    tk.destroy()
    
    tk1=Tk()
    tk1.title("Wine")
    tk1.geometry("400x100+750+400")
    tk1.configure(bg="#3F3F3F")

    label = ttk.Label(text="Wine запущен, наслаждайтесь" ,font=("Arial", 16), background="#3F3F3F", foreground="#FFFFFF")
    label.pack(expand=True)

    tk1.after(1500,tk1.destroy)
    

btn = ttk.Button(text="Проверить",command=check)
btn.place(x=410, y=20)

label = ttk.Label(text="Wine:", font=("Arial", 18), background="#3F3F3F", foreground="#FFFFFF")
label.place(x=170,y=20)

label1 = ttk.Label(text="Не найден", font=("Arial", 18), background="#3F3F3F", foreground="#FF0000")
label1.place(x=250,y=20)

warn = ttk.Label(text="!Для установки wine нажмите сюда ->", font=("Arial", 11), background="#3F3F3F", foreground="#C5C5C5")
warn.place(x=130,y=70)

copy_button=ttk.Button(text="Скопировать комманду",command=lambda: pc.copy("sudo apt install wine"))
copy_button.place(x=400,y=65)

Start=ttk.Button(text="Запустить Wine",command=wine,state=["disabled"])
Start.place(height=50,width=150,x=270,y=150)


tk.mainloop()
