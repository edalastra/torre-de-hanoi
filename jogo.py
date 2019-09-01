from models.TorresDeHanoi import TorresDeHanoi
import os

def controlador():
    welcome()
    torres_de_hanoi = TorresDeHanoi()
    torres_de_hanoi.exibe()

    while(not torres_de_hanoi.ganhou()):
        jogada(torres_de_hanoi)
    print("Parabéns! Você venceu o desafio!")


def jogada(torres_de_hanoi):
    try:
        de, para = input('Digite os respectivos números do movimento: ').split(' ')
        de = int(de)
        para = int(para)
        torres_de_hanoi.movimento(de, para)
        torres_de_hanoi.exibe()

    except (ValueError, IndexError):
        print('Comandos inválidos digite novamente')
        jogada(torres_de_hanoi)


    os.system('cls' if os.name == 'nt' else 'clear')

    
def welcome():
    print('\t\tBem Vindo ao jogo Torre de Hanói\n')
    print('\tEsse é um "quebra-cabeça" que consiste em uma base contendo três pinos,\n'
          'em um dos quais são dispostos alguns discos uns sobre os outros,\n'
          'em ordem crescente de diâmetro, de cima para baixo.\n\n'
          'Objetivo: mover todos os discos para o pino da direita.\n'
          'Regras: Digite primeiro o número da base que o disco está e o número\n'
          'da base para qual ele será movido, você deve mover um disco de cada vez,\n'
          'sendo que um disco maior nunca poderá ficar em cima de um disco menor.\n')
    input('Tecle enter para começar...')
    os.system('cls' if os.name == 'nt' else 'clear')

if(__name__ == "__main__"):
    controlador()