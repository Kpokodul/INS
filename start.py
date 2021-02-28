#! /usr/python3
# -*- coding: utf-8 -*-

    # This file is part of INS (Interpreter of Number Systems).

    # Foobar is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # Foobar is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb
from datetime import *
from sys import platform
import time
import shutil
import os

def DelLog():
    dir_log = "./Log"
    answer = mb.askyesno(
        title="Удалить Лог?", 
        message="Вы уверены?")
    if answer:
        if os.path.exists('Log') == True:
            try:
                shutil.rmtree(dir_log)
            except:
                errorms = mb.showerror(
                    title="Ошибка", 
                    message="Не удалось удалить Лог! Сделайте это вручную"
                )
        else:
            pass

def Start():
    try:
        window.destroy()
        if platform == "win32":
            os.system('python main.py')
        else:
            os.system('python3 main.py')
    except:
        errorms = mb.showerror(
            title="Ошибка", 
            message="Не удалось запустить программу! Сделайте это вручную"
        )

def Copyright():
    current_datetime = str(datetime.now().year)
    return current_datetime

year = "Copyright (c) 2020 - " + str(Copyright() + " Petrov Alexey (kpokodul) for GNU GPL")

window = Tk()
window.title("Перевод систем счисления - Начало работы")
w = ((window.winfo_screenwidth())//2) - 200
h = ((window.winfo_screenheight())//2) - 100
window.geometry('400x200+{}+{}'.format(w, h))
window.resizable(False, False)
if platform == "win32":
    window.iconbitmap('img/ico/favicon.ico')
else:
    pass


name = Label(window, text = "Перевод систем счисления (INS)", font = "Ubuntu 16")
name.place(x = 8, y = 10)

version = Label(window, text = "v0.1.0 Graphic Edition", font = "Ubuntu 12")
version.place(x = 8, y = 45)

delLog = Button(text="Удалить Лог", width = 15, height = 3, font = "Ubuntu", command = DelLog)
delLog.place(x = 8, y = 80, width = 188, height = 70)

start = Button(text="Запуск", width = 15, height = 3, font = "Ubuntu", command = Start)
start.place(x = 204, y = 80, width = 188, height = 70)

CopyR = Label(window, text=year, font=("Ubuntu", 9))
CopyR.place(x = 2, y = 180)

window.mainloop()
