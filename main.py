# main.py
import tkinter as tk
from interfaz_clima import AplicacionClima

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionClima(root)
    root.mainloop()
