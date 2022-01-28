from tkinter import *
from tkinter import ttk
from random import randint
class Iniciar(Frame):
    def __init__(self):
        ttk.Style().configure('green/black.TLabel', foreground='green', background='black')
        ttk.Style().configure('green/black.TButton', foreground='green', background='black')
        self.texto = ttk.Label(text="Numero que caiu: 0")
        self.texto.grid(row=3)
        def onclick():
            numero_random = randint(1, 6)
            self.texto.configure(text=f"Numero que caiu: {numero_random}")
            return numero_random

        def mudarimagem(label):
            dado = ''
            match(onclick()):
                case 1:
                    label.configure(file='./imagens/dado1.png')
                case 2:
                    label.configure(file='./imagens/dado2.png')
                case 3:
                    label.configure(file='./imagens/dado3.png')
                case 4:
                    label.configure(file='./imagens/dado4.png')
                case 5:
                    label.configure(file='./imagens/dado5.png')
                case 6:
                    label.configure(file='./imagens/dado6.png')

        def resetdedado(label):
            self.texto.configure(text="Numero que caiu: 0")
            label.configure(file = "./imagens/dado0.png")
            
        
        self.imagemdado = PhotoImage(file='imagens/dado0.png')
        self.labelimg = Label(image=self.imagemdado)
        self.labelimg.grid()
        
        self.botao = ttk.Button(text="Rolar dado")
        self.botao['command'] = (lambda: onclick())
        self.botao['command'] = (lambda: mudarimagem(self.imagemdado))
        self.botao.place(x=50,y=63)

        self.botaoreset = ttk.Button(text="Resetar")
        self.botaoreset['command'] = (lambda: resetdedado(self.imagemdado))
        self.botaoreset.place(x=230, y=63)


        