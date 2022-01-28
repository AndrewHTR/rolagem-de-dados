from botao import *
from label import *
import tkinter as tk
from tkinter import ttk
class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.iniciar = Iniciar()
        self.botao = Botao()
root = tk.Tk()
root.title('Rolagem de dados')
root.geometry('348x150')
root.iconbitmap("./imagens/icone.ico")
Application(root)
root.mainloop()