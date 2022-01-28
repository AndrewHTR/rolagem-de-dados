from tkinter import *
from tkinter import ttk

class Botao(Frame):  
    def __init__(self):
        self.texto1 = ttk.Label(text="Bem Vindo a rolagem de dados!")
        self.texto1.grid(row=1)

        self.texto2 = ttk.Label(text="Aperte nos botões abaixo para que um resultado aleatorio ocorra.")
        self.texto2.grid(column=0, row=2)
        
        self.criador = ttk.Label(text="Criador por: Andrew Silva")
        self.criador.configure(font=('Arial', 16))
        self.criador.place(y=124)
    



