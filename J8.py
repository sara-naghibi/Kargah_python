import tkinter as tk
from tkinter import messagebox

def mohasebe_dong():
    try:
        mablagh_kol = float(vorudi_mablagh.get())
        tedad_nafarat = int(vorudi_tedad.get())
        
        if tedad_nafarat <= 0:
            messagebox.showwarning("Khataye Vorudi", "Tedad nafarat bayad bishtar az sefr bashad!")
            return
            
        sahme_har_nafar = mablagh_kol / tedad_nafarat
        messagebox.showinfo("Natije", f"Sahme har nafar: {sahme_har_nafar:.0f} Toman")
        
    except ValueError:
        messagebox.showwarning("Khataye Vorudi", "Lotfan dar har do ghesmat adad vared konid!")
    except Exception as e:
        messagebox.showwarning("Khataye Namashakhas", "Moshkeli pish amade ast!")

panjere = tk.Tk()
panjere.title("Mashin Hesabe Dong")
panjere.geometry("300x200")

tk.Label(panjere, text="Mablaghe Kol:").grid(row=0, column=0, padx=10, pady=10)
vorudi_mablagh = tk.Entry(panjere)
vorudi_mablagh.grid(row=0, column=1)

tk.Label(panjere, text="Tedad Nafarat:").grid(row=1, column=0, padx=10, pady=10)
vorudi_tedad = tk.Entry(panjere)
vorudi_tedad.grid(row=1, column=1)

dokme_mohasebe = tk.Button(panjere, text="Mohasebe sahme har nafar", command=mohasebe_dong)
dokme_mohasebe.grid(row=2, column=0, columnspan=2, pady=20)

panjere.mainloop()
