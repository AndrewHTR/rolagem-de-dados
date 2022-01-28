import random
import os
def main():
#! o objetivo é criar um programa que joga um numero de 1 a 6, semelhante a um dado e que o usuario consiga rodar quantas vezes quiser
    linha = os.get_terminal_size()
    size = linha.columns * '='
    numero = random.randint(1, 6)
    print(size)
    print('''Bem-Vindo ao programa de rolagem de dados! 

Neste programa você pode rolar um dado que vai de 1 a 6.''')

    print('')
    print('Você quer participar do jogo? [S]SIm ou [N]Nâo')
    resposta = input().lower
    print(size)
  

main()