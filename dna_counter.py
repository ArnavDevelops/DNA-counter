import tkinter as tk
from tkinter import messagebox, ttk
import random

def random_dna(length):
    return ''.join(random.choice("ATGC") for _ in range(length))

root = tk.Tk()
root.title("DNA Counter")
root.geometry("450x400")

tk.Label(root, text="Input DNA Sequence:", font=("Calligraffitti", 10)).pack(pady=5)
entry = tk.Entry(root, width=40, borderwidth=2, font=("Calligraffitti", 10))
entry.pack(pady=5)

result_label = tk.Label(root, text="", justify="left", font=("Calligraffitti", 10))
result_label.pack(pady=10)

def count_dna():  
    dna = entry.get().upper()
    
    if len(dna) == 0 or any(base not in "ATGC" for base in dna):
        messagebox.showerror("Error", "Enter only A, T, G, C!")
        return

    a_count = dna.count('A')
    t_count = dna.count('T')
    g_count = dna.count('G')
    c_count = dna.count('C')
    total = len(dna)
    GC_percent = ((g_count + c_count) / total) * 100
    AT_percent = ((a_count + t_count) / total) * 100

    result_label.config(text=f"""
              
Length: {total}

Nucleoid #
A: {a_count}   T: {t_count}
G: {g_count}   C: {c_count}

Composition:
GC%: {GC_percent:.2f}%   
AT%: {AT_percent:.2f}%
""")

def fill_random():
    seq = random_dna(30) 
    entry.delete(0, tk.END)
    entry.insert(0, seq)

tk.Button(root, text="Count DNA", command=count_dna, font=("Calligraffitti", 10)).pack(pady=10)
tk.Button(root, text="Randomize", command=fill_random, font=("Calligraffitti", 10)).pack(pady=10)

root.mainloop()