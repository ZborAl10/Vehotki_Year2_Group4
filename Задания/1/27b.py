from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor

root = Tk( )
root.title("Главное окно программы")
root.geometry("300x300+250+250")

win1 = Frame(root, bg = '#555555')
win1.pack(anchor = "n", expand = YES, fill = X)

def closeQuery( ):
    if askyesno('Выход из программы...', 'Закрыть программу? '):
        root.destroy( )

Button(win1, text = 'Выход', command = closeQuery).pack(side = RIGHT, padx = 10, pady = 5)

sizes = [2, 5, 10]

_size = sizes[0]

varSize = StringVar()

for s in sizes:
    Radiobutton(win1, bg = '#555555', text = s, variable = varSize, value = s).pack(side = LEFT, padx = 10, pady = 10)

varSize.set(sizes[0])

def set_color(w):
    global _color
    res = askcolor()
    print("Диалоговое окно Цвет возвращает результат:", res)
    if res[1]:
        _color = res[1]

b1 = Button(win1, text = 'Цвет', command = (lambda: set_color(b1)))
b1.pack(side = RIGHT, padx = 10, pady = 5)

can = Canvas(root)
can.pack(expand = YES, fill = BOTH)

_x1 = 0
_y1 = 0
_x2 = 0
_y2 = 0

_color = '#000000'

_line = can.create_line(-10,-10,-10,-10, fill="black", width=varSize.get())

def draw(x1, y1, x2, y2, col):
    can.create_line(x1, y1, x2, y2, fill = col, width = varSize.get())

def onclick(event):
    print("Нажали на кнопку %s X = %s Y = %s" % (event.widget, event.x, event.y))
    global _x1
    global _y1
    _x1 = event.x
    _y1 = event.y
    global _x2
    global _y2
    _x2 = event.x
    _y2 = event.y
    global line
    _line = draw(_x1, _y1, _x2, _y2, _color)
    


def onmove(event):
    global _x2
    global _y2
    _x2 = event.x
    _y2 = event.y
    can.itemconfig(_line, fill=_color, width = varSize.get())
    can.coords(_line, _x1, _y1, _x2, _y2)

def onrelease(event):
    draw(_x1, _y1, _x2, _y2, _color)


can.bind("<Button-1>", onclick)
can.bind("<B1-Motion>", onmove)
can.bind("<ButtonRelease-1>", onrelease)

root.mainloop()
