from iniciar import *
from ds import *
import tkinter as tk
from tkinter import ttk
class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.iniciar = Iniciar()
        self.botao = Botao()
root = tk.Tk()
root.title('Teste')
root.geometry('800x600')
root.config(bg='black')
Application(root)
root.mainloop()