import tkinter
from tkinter import *

tk = Tk()

tk.title("Mile to Km Converter")
tk.geometry("300x170")


def miles2km():
    getm2km = float(milesEntry.get())
    getm2km *= 1.609344
    kmResult["text"] = round(getm2km, 2)


miles = Label(text="Miles", font=("Arial", 15))
miles.grid(row=1, column=3, padx=10, pady=10)

km = Label(text="Km", font=("Arial", 15))
km.grid(row=2, column=3, padx=10, pady=10)

isEqualTo = Label(text="is equal to:", font=("Arial", 12))
isEqualTo.grid(row=2, column=1, padx=10, pady=10)

calculate = Button(text="Calculate", font=("Arial", 15, "bold"), command=miles2km)
calculate.grid(row=3, column=2, padx=10, pady=10)

milesEntry = Entry(width=10, font=("Arial", 15))
milesEntry.grid(row=1, column=2, padx=10, pady=10)

kmResult = Label(text="0", font=("Arial", 15))
kmResult.grid(row=2, column=2, padx=10, pady=10)

tk.mainloop()
