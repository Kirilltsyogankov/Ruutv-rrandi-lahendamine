"""
from tkinter import *
def errorEntry():
    a=textbox1.get()
    b=textbox2.get()
    c=textbox3.get()
    if a.isalnum() or b.isalnum() or c.isalnum():
        if a.isdigit() or b.isdigit() or c.isdigit():
            pass
        else:



aken=Tk()
aken.geometry("800x400")
aken.title("Tkineri kasutamine")

tekst1="Ruutvõrrandi lahendamine"

pealkiri
esimineForm=
teineForm=
kolmasForm=

textbox1=
textbox2=
textbox3= 

nupp=Button(aken,
            tetx"=0",
            bg="#ffd042",
            fg="#000000",
            font="Arial 20",
            height=1,
            width=6
            )    """

import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def lahenda_kvadraatne(a, b, c):
    """Funktsioon kvadraatse võrrandi juurte leidmiseks."""
    diskriminant = b**2 - 4*a*c
    if diskriminant > 0:
        x1 = (-b + np.sqrt(diskriminant)) / (2*a)
        x2 = (-b - np.sqrt(diskriminant)) / (2*a)
        return x1, x2
    elif diskriminant == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

def naita_lahendust():
    """Funktsioon nupule 'Lahenda' vajutamiseks."""
    a_val = a_entry.get()
    b_val = b_entry.get()
    c_val = c_entry.get()

    if not a_val or not b_val or not c_val:
        # Kui mõni väli on täitmata, muudame taustavärvi
        solution_frame.config(bg="red")
        messagebox.showerror("Viga", "Palun täitke kõik väljad.")
        return

    try:
        a = float(a_val)
        b = float(b_val)
        c = float(c_val)
    except ValueError:
        messagebox.showerror("Viga", "Vigased väärtused väljades.")
        return

    juured = lahenda_kvadraatne(a, b, c)
    if juured:
        solution_label.config(text=f"Võrrandi juured: {juured}")
    else:
        solution_label.config(text="Võrrandil pole juuri.")

def joonista_graafik():
    """Funktsioon graafiku joonistamiseks."""
    a_val = a_entry.get()
    b_val = b_entry.get()
    c_val = c_entry.get()

    try:
        a = float(a_val)
        b = float(b_val)
        c = float(c_val)
    except ValueError:
        messagebox.showerror("Viga", "Vigased väärtused väljades.")
        return

    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c

    plt.plot(x, y)
    plt.title("Kvadraatse võrrandi graafik")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# Loome graafikakeskkonna
root = tk.Tk()
root.title("Kvadraatse võrrandi lahendamine")

# Väljade raam
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Väljad koefitsientide jaoks
a_label = tk.Label(input_frame, text="a:")
a_label.grid(row=0, column=0, padx=5, pady=5)
a_entry = tk.Entry(input_frame)
a_entry.grid(row=0, column=1, padx=5, pady=5)

b_label = tk.Label(input_frame, text="b:")
b_label.grid(row=1, column=0, padx=5, pady=5)
b_entry = tk.Entry(input_frame)
b_entry.grid(row=1, column=1, padx=5, pady=5)

c_label = tk.Label(input_frame, text="c:")
c_label.grid(row=2, column=0, padx=5, pady=5)
c_entry = tk.Entry(input_frame)
c_entry.grid(row=2, column=1, padx=5, pady=5)

# Nupp lahenduse leidmiseks
solve_button = tk.Button(root, text="Lahenda", command=naita_lahendust)
solve_button.pack(pady=5)

# Raam väljundile
solution_frame = tk.Frame(root)
solution_frame.pack(padx=10, pady=10)
solution_label = tk.Label(solution_frame, text="")
solution_label.pack()

# Nupp graafiku joonistamiseks
plot_button = tk.Button(root, text="Graafik", command=joonista_graafik)
plot_button.pack(pady=5)

root.mainloop()
