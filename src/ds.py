from tkinter import *
from tkinter import ttk

class Botao(Frame):  
    def __init__(self):
        self.botao1 = ttk.Button( text='Viver', padding= "22")
        self.botao1.grid(column=0, row=1)
        self.botao1['command'] = (lambda: print('Você quer viver.'))

        
    



