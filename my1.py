from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Калькулятор")

# логика калькулятора
def calc(key):
    if key == "=":
# исключаем написание букв
        str1 = "-+0123456789.*/"
        if calc_entry.get()[0] not in str1:
            messagebox.showerror("Ошибка!", "Вы ввели не число!")
# счет
        try:
            result = eval(calc_entry.get())
            calc_entry.delete(0, END)
            calc_entry.insert(0, result)
        except:
            messagebox.showerror("Ошибка!", "Проверь правильность данных")        
# очистить поле
    elif key == "C":
        calc_entry.delete(0, END)
# смена +-
    elif key == "-/+":
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        calc_entry.insert(END, key)                   



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