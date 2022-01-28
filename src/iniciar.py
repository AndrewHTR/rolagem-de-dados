from tkinter import *
from tkinter import ttk
from ds import *
class Iniciar(Frame):
    def __init__(self):
        ttk.Style().configure('green/black.TLabel', foreground='green', background='black')
        ttk.Style().configure('green/black.TButton', foreground='green', background='black')
        self.botao = ttk.Button(text="Morrer", bg="black")
        self.botao.grid(column=0,row=2)
        self.botao['command'] = (lambda: print('Você quer morrer.'))
