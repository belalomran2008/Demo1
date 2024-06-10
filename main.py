from tkinter import *

root = Tk()
root.resizable(0, 0)
root.title("Currency converter")
root.iconbitmap('C:/Users/belal/PycharmProjects/First app/Dollar.ico')
dt = Entry(root, width=35, borderwidth=5)
label1 = Label(root, text="Dollar today")
dt.insert(0, 'Dollar today: ')
no = Entry(root, width=35, borderwidth=5)
no.grid(row=3, column=1)
dt.grid(row=1, column=1)
answer = Entry(root, width=35, borderwidth=5)
answer.grid(row=8, column=1)
Dollar = Label(0, text="Dollar today:")
Dollar.grid(row=1, column=0)
de = Label(0, text="Dollar/EGP:")
de.grid(row=3, column=0)
final = Label(0, text="Final:")
final.grid(row=8, column=0)


# no.insert(0, "EGP/Dollar: ")
def egp():
    e = no.get()
    g = dt.get()
    answer.insert(0, float(e) / float(g))


def dollar():
    e = no.get()
    g = dt.get()
    answer.insert(0, float(e) * float(g))


def clear():
    answer.delete(0, END)


f1 = Button(root, text="From Egp to Dollar", padx=5, pady=5, command=egp)
f1.grid(row=4, column=0)
f2 = Button(root, text="From Dollar to EGP", padx=5, pady=5, command=dollar)
f2.grid(row=4, column=1)
f3 = Button(root, text="Clear", padx=10, pady=5, command=clear)
f3.grid(row=4, column=2)
root.mainloop()
