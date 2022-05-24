from tkinter import *

ws = Tk()
ws.title('Опросик')
ws.geometry('300x300')

def isChecked():
    if cb.get() == 1:
        btn['state'] = NORMAL
        btn.configure(text='Done')
    elif cb.get() == 0:
        btn['state'] = DISABLED
        btn.configure(text='Not Done')
    else:
        messagebox.showerror('Num16', 'Something went wrong!')

def selection():
    choice = var1.get()
    if choice == 1:
        m = 'Женщина '
    elif choice == 2:
        m = 'Мужик '
    return m

def selectionFIO():
    choice = var2.get()
    if choice == 1:
        n = 'есть ФИО, '
    elif choice == 2:
        n = 'нет ФИО, '
    return n

def selectionRoulet():
    choice = var3.get()
    if choice == 1:
        n = 'с рулетом)). '
    elif choice == 2:
        n = 'без рулета. '
    return n

def submit():
    try:
        name = selectionFIO()
        m = selection()
        Roulet = selectionRoulet()
        return messagebox.showinfo('Num16', f'{m} {name} {Roulet}')
    except Exception as ep:
        return messagebox.showwarning('Num16', 'Please provide valid input')


cb = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()


frame1 = LabelFrame(ws, text = "Пол:", padx=20, pady=10)
frame1.pack()

Radiobutton(frame1, text='Female', variable=var1, value=1,command = selection).pack(side = LEFT)
Radiobutton(frame1, text='Male', variable=var1, value=2,command = selection).pack(side = RIGHT)

frame2 = LabelFrame(ws, text='Есть ФИО?', padx=30, pady=10)
frame2.pack()
Radiobutton(frame2, text='Да', variable=var2, value=1,command=selection).pack(side = LEFT)
Radiobutton(frame2, text='Нет', variable=var2, value=2,command=selection).pack(side = LEFT)




frame3 = LabelFrame(ws, text='Кто-то украл твой сладкий рулет?', padx=30, pady=10)
frame3.pack()
Radiobutton(frame3, text='Да TRIGGER', variable=var3, value=1,command=selection).pack(side = LEFT)
Radiobutton(frame3, text='Нет)', variable=var3, value=2,command=selection).pack(side = LEFT)


Checkbutton(ws, text = "Соглашайся!!!!", variable = cb, onvalue = 1, offvalue = 0, command = isChecked).pack()
btn = Button(ws, text="Submit", command=submit, padx=50, pady=5, state=DISABLED)
btn.pack()

ws.mainloop()