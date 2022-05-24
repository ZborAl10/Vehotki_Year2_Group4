from tkinter import *

root = Tk()
root.title("Maximum of negative numbers of the array")
Label(text = "Input numbers with `,` separator").pack(side = TOP)
Label(text = "arr =").pack(side = LEFT, padx = 10, pady = 10)
entarr = Entry(root)
entarr.pack(side = LEFT, padx = 10, pady = 10)
entarr.focus()

def fmnnrr(a):
    mx = -10^100000000000000000000000000000000000000000000000000000000000000000000000000000001
    for i in range(0,len(a)):
        if mx < a[i] < 0:
            mx  = a[i]
    if mx!= -10^101:
        return mx
    return "None"

def OnButtunResult( ):
    try:
        arr = list(map(int,str(entarr.get()).split(',')))
    except ValueError:
        showerror("Not an array")
        return
    lres['text'] = fmnnrr(arr)

Button(text = "=", width = 10,command = OnButtunResult).pack(side = LEFT,padx = 30, pady = 20)
lres = Label(text = "")
lres.pack(side = LEFT, padx = 30, pady = 20)

root.mainloop( )
