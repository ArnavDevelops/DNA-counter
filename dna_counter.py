from PIL import Image
import random
import customtkinter as ctk

def random_dna(length):
    return ''.join(random.choice("ATGC") for _ in range(length))

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("DNA Counter")
root.geometry("450x400")

ctk.CTkLabel(root, text="Input DNA Sequence:", font=("Calligraffitti", 10))
entry = ctk.CTkEntry(root, width=250, border_width=2, font=("Calligraffitti", 12), corner_radius=5)
entry.pack(pady=5)

randomize_img = Image.open("images/3580329.png")

def fill_random():
    seq = random_dna(30) 
    entry.delete(0, ctk.END)
    entry.insert(0, seq)
ctk.CTkButton(root, text="Randomize", 
              command=fill_random, 
              text_color="white", 
              font=("Calligraffitti", 14), 
              corner_radius=5,
              hover_color="#6969E1",
              image=ctk.CTkImage(dark_image=randomize_img, light_image=randomize_img)).pack(pady=10)

line = ctk.CTkFrame(root, height=2, width=400, fg_color="gray")
line.pack(pady=10)

result_label = ctk.CTkLabel(root, text="", font=("Calligraffitti", 14))
result_label.pack(pady=10)

def count_dna():  
    dna = entry.get().upper()
    
    if len(dna) == 0 or any(base not in "ATGC" for base in dna):
        error_window = ctk.CTkToplevel(root)
        error_window.title("Error!")
        error_window.geometry("200x120")
        error_window.wm_transient(root)
        error_window.resizable(False, False)
        ctk.CTkLabel(error_window, text="Invalid Sequence!", font=("Calligraffitti", 12)).pack(pady=10)
        return

    a_count = dna.count('A')
    t_count = dna.count('T')
    g_count = dna.count('G')
    c_count = dna.count('C')
    total = len(dna)
    GC_percent = ((g_count + c_count) / total) * 100
    AT_percent = ((a_count + t_count) / total) * 100

    result_label.configure(text=f"""
Length: {total}

Nucleoid #
A: {a_count}   T: {t_count}
G: {g_count}   C: {c_count}

Composition:
GC%: {GC_percent:.2f}%   
AT%: {AT_percent:.2f}%
""")

dna_img = Image.open("images/dna.png")

ctk.CTkButton(root, 
              text="Count DNA", 
              command=count_dna, 
              text_color="white", 
              font=("Calligraffitti", 14), 
              corner_radius=5,
              hover_color="#6969E1",
              image=ctk.CTkImage(dark_image=dna_img, light_image=dna_img)).pack(pady=10)

root.mainloop()  