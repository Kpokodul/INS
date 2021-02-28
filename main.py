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

    # Copyright (c) 2020 - 2021 Petrov Alexey (kpokodul)


from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb
from datetime import *
from sys import platform
import os

def convert_base(num, to_base=10, from_base=16):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

def Score():
    text2['state']="normal"
    text2.delete(0, END)
    txt1 = text1.get()
    chc1 = int(choice1.get())
    chc2 = int(choice2.get())
    if chc1 == chc2:
        Log(txt1, txt1, str(chc1), str(chc2))
        text2.insert(0, txt1)
    elif txt1 == "":
        text2['state']="readonly"
    else:
        try:
            resulf = convert_base(txt1, chc2, chc1)
            text2.insert(0, resulf)
        except:
            errorms = mb.showerror(
                title="Ошибка", 
                message="Неверный формат введённых данных!"
            )
            text2['state']="readonly"
            
    try:
        Log(txt1, str(resulf), str(chc1), str(chc2))
    except:
        pass
        
    text2['state']="readonly"

def Copyright():
    current_datetime = str(datetime.now().year)
    return current_datetime

def Clear():
    answer = mb.askyesno(
        title="Сброс", 
        message="Очистить данные?")
    if answer:
        text1.delete(0, END)
        text2['state'] = "normal"
        text2.delete(0, END)
        text2['state'] = "readonly"
        text1.focus()
    
def Exit():
    answer = mb.askyesno(
        title="Выход",
        message="Выйти?")
    if answer:
        window.destroy()

def Close():
    try:
        window.destroy()
        if platform == "win32":
            os.system('python start.py')
        else:
            os.system('python3 start.py')
    except:
        errorms = mb.showerror(
            title="Ошибка", 
            message="Не удалось запустить программу! Сделайте это вручную"
        )

def Time():
    today = datetime.today()
    today = today.strftime("%Y-%m-%d %H-%M-%S")
    return(today)

def Log(txt1, resulf, chc1, chc2):
    LogNow = open("Log/{}.txt".format(today), 'a')
    current_datetime = datetime.today()
    current_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
    try:
        LogNow.write("[" + current_datetime + "]" + " " + txt1 + "(" + chc1 + ")" +  " = " + resulf + "(" + chc2 + ")\n")
    except:
        errorms = mb.showerror(
            title="Ошибка",
            message="Не удалось записать данные в лог файл!")

def NewLog(today):
    try:
        os.mkdir("Log")
    except:
        pass
    LogNow = open("Log/{}.txt".format(today), 'w')
    LogNow.close()
    
def RemoveWhiteLog(today):
    if os.path.getsize("Log/{}.txt".format(today)) == 0:
        os.remove("Log/{}.txt".format(today))
    
today = Time()
NewLog(today)

year = "Copyright (c) 2020 - " + str(Copyright() + " Petrov Alexey (kpokodul) for GNU GPL")

window = Tk()
window.title("Перевод систем счисления - Запущено")
w = ((window.winfo_screenwidth())//2) - 200
h = ((window.winfo_screenheight())//2) - 100
window.geometry('400x200+{}+{}'.format(w, h))
window.resizable(False, False)
if platform == "win32":
    window.iconbitmap('img/ico/favicon.ico')
else:
    pass

# Меню

mainmenu = Menu(window) 
window.config(menu=mainmenu) 
#Меню: Пункты: Файл
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Начало работы", font=("Ubuntu 11"), command=Close)
filemenu.add_separator()
filemenu.add_command(label="Выход", font=("Ubuntu 11"), command=Exit)
#Меню: Пункты: Правка
editmenu = Menu(mainmenu, tearoff=0)
editmenu.add_command(label="Сбросить", font=("Ubuntu 11"), command=Clear)
#Меню: Пункты
mainmenu.add_cascade(label="Меню", font=("Ubuntu 12"), menu=filemenu)
mainmenu.add_cascade(label="Правка", font=("Ubuntu 12"), menu=editmenu)


#Копирайт
CopyR = Label(window, text=year, font=("Ubuntu", 9))
CopyR.place(x = 2, y = 180)


#Ввод
text1 = Entry(window, font=("Ubuntu", 18), width=("24"))
text1.place(x = 8, y = 10, width=316)

choice1 = Combobox(window, state="readonly", font=("Ubuntu", 18), width=("4"))
choice1.place(x = 330, y = 10, width=62)
choice1['values'] = (2, 8, 10, 16)
choice1.current(2)

#Результат
text2 = Entry(window, cursor="arrow", state="readonly",font=("Ubuntu", 18), width=("24"))
text2.place(x = 8, y = 50, width=316)

choice2 = Combobox(window, state="readonly", font=("Ubuntu", 18), width=("4"))
choice2.place(x = 330, y = 50, width=62)
choice2['values'] = (2, 8, 10, 16)
choice2.current(0)

#Кнопка вывода результата
res = Button(window, text="Расчитать", font=("Ubuntu", 14), command=Score, width=("34"), height=("2"))
res.place(x = 8, y = 90, width = 384)


text1.focus()

window.mainloop()

RemoveWhiteLog(today)
