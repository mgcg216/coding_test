#!/usr/bin/env python3
from tkinter import *
from functools import partial
from itertools import product

# produce the set of coordinates of the buttons
positions = product(range(10), range(10))
button_ids = []

def change(i):
    # get the button's identity, destroy it
    bname = (button_ids[i])
    bname.configure(bg="red")

win = Tk()
# frame = Frame(win)
# frame.pack()

# for i in range(10):
#     # shape the grid
#     setsize = Canvas(frame, width=30, height=0).grid(row=11, column=i)
#     setsize = Canvas(frame, width=0, height=30).grid(row=i, column=11)
#
# for i, item in enumerate(positions):
#     button = Button(frame, command=partial(change, i))
#     button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
#     button_ids.append(button)

# for i in range(8):
#     for j in range(4):
#         for k in range(15):
#             print(i, j, k)
            # button = Button(win, command=partial(change, i))
            # button.place(x=k*50, y=i*50 + j*100, anchor="nw", height=20, width=20)
            # # add the button's identity to a list:
            # button_ids.append(button)

pos = product(range(8), range(4), range(15))
y = 0
for idx, val in enumerate(pos):
    x = val[2] * 50
    y = val[1] * 50 + val[0] * 4*50 + val[0] *50
    print(x, y)
    print(val)
    button = Button(win, command=partial(change, idx))
    button.place(x=x, y=y, anchor="nw", height=20, width=20)
    button_ids.append(button)


win.minsize(width=400, height=2000)
win.title("Too many squares")
win.mainloop()