import tkinter
from tkinter import ttk
import math

window = tkinter.Tk()
window.title("Vector calculator ")
window.minsize()
frr = ttk.Frame(window, padding=10)
frr.grid()
global radius1
global theta1
global radius2
global theta2
tkinter.Label(frr, text="r1 = ").grid(column=0, row=0)
radius1 = tkinter.Entry(frr, bg="gray", width=10, borderwidth=2)
# radius1.insert(0, string="1")
radius1.grid(row=0, column=1)
tkinter.Label(frr, text="Angle 1 = ").grid(column=3, row=0)
theta1 = tkinter.Entry(frr, bg="gray", width=10, borderwidth=2)
# theta1.insert(0, string="1")
theta1.grid(row=0, column=4)
tkinter.Label(frr, text="r2 = ").grid(column=0, row=1)
radius2 = tkinter.Entry(frr, bg="gray", width=10, borderwidth=2)
# radius2.insert(0, string="1")
radius2.grid(row=1, column=1)
tkinter.Label(frr, text="Angle 2 = ").grid(column=3, row=1)
theta2 = tkinter.Entry(frr, bg="gray", width=10, borderwidth=2)
# theta2.insert(0, string="1")
theta2.grid(row=1, column=4)
global result
result = tkinter.Label(frr, text="Result = ")


def add():
    r1 = float(radius1.get())
    r2 = float(radius2.get())
    t1 = float(theta1.get()) * math.pi / 180.0
    t2 = float(theta2.get()) * math.pi / 180.0
    resultant_r = math.sqrt(r1 ** 2 + r2 ** 2 + 2 * r1 * r2 * math.cos(t2 - t1))
    resultant_angle = (math.atan(
        (r1 * math.sin(t1) + r2 * math.sin(t2)) / (r1 * math.cos(t1) + r2 * math.cos(t2)))) * 180.0 / math.pi
    resultant_tuple = (resultant_r.__round__(2), resultant_angle.__round__(2))
    result["text"] = f"Result = {resultant_tuple}"
    result.grid(column=0, row=4)
    return


def sub():
    r1 = float(radius1.get())
    r2 = float(radius2.get())
    t1 = float(theta1.get()) * math.pi / 180.0
    t2 = (float(theta2.get()) + 180.0) * math.pi / 180.0
    resultant_r = math.sqrt(r1 ** 2 + r2 ** 2 + 2 * r1 * r2 * math.cos(t2 - t1))
    resultant_angle = (math.atan(
        (r1 * math.sin(t1) + r2 * math.sin(t2)) / (r1 * math.cos(t1) + r2 * math.cos(t2)))) * 180.0 / math.pi
    resultant_tuple = (resultant_r.__round__(5), resultant_angle.__round__(5))
    result["text"] = f"Result = {resultant_tuple}"
    result.grid(column=0, row=4)
    return


add = tkinter.Button(frr, text="click to add",
                     command=add)
add.grid(column=0, row=3)
sub = tkinter.Button(frr, text="click to sub",
                     command=sub)
sub.grid(column=1, row=3)

window.mainloop()
