from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Калькулятор")

# логика калькулятора
def calculate(calc_entry):
    sym = "-+0123456789.*/"
    if calc_entry.get()[0] not in sym:
        messagebox.showerror("Ошибка!", "Вы ввели не число!")
    try:
        result = eval(calc_entry.get())
        calc_entry.delete(0, END)
        calc_entry.insert(0, result)
    except:
        messagebox.showerror("Ошибка!", "Проверь правильность данных")  

def delet_last(calc_entry):
    calc_entry.delete(0, END)

def change_sign(calc_entry):
    if calc_entry.get().startswith('-'):
        calc_entry.delete(0)
    else:
        calc_entry.insert(0, "-")

def append_token(calc_entry, key):
    calc_entry.insert(END, key)

def calc(key):
    if key == "=":
      calculate(calc_entry)  
    elif key == "C":
        delet_last(calc_entry)
    elif key == "-/+":
        change_sign(calc_entry)
    else:
        append_token(calc_entry, key)
                    
# создание кнопок
bttn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C"
]
r = 1
c = 2

for i in bttn_list:
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c>4:
        c=0
        r += 1  

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()