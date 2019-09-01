from models.TorresDeHanoi import TorresDeHanoi
import os

def controlador():
    welcome()
    torres_de_hanoi = TorresDeHanoi()
    torres_de_hanoi.exibe()

    while(not torres_de_hanoi.ganhou()):
        jogada(torres_de_hanoi)
    imprime_mensagem_vencedor()
    print('Numero de movimentos = {}'.format(torres_de_hanoi.movimentos))
    if(torres_de_hanoi.movimentos > 15):
        print('Voce pode fazer melhor. Tente novamente')


def jogada(torres_de_hanoi):
    try:
        de, para = input('Digite os respectivos numeros do movimento: ').split(' ')
        de = int(de)
        para = int(para)
        os.system('cls' if os.name == 'nt' else 'clear')
        torres_de_hanoi.movimento(de - 1, para - 1)
        torres_de_hanoi.exibe()

    except (ValueError, IndexError):
        print('Comandos invalidos digite novamente')
        jogada(torres_de_hanoi)

    
def welcome():
    print("\t***************************************")
    print("\t***Bem vindo ao jogo Torre de Hanoi!***")
    print("\t***************************************")
    print('\tEsse e um "quebra-cabeça" que consiste em uma base contendo tres \n'
          'pinos, em um dos quais sao dispostos alguns discos uns sobre os outros,\n'
          'em ordem crescente de diametro, de cima para baixo.\n\n'
          '\tObjetivo: mover todos os discos para o pino da direita, com o numero de movimentos.\n'
          'mais proximo de 15'
          '\tRegras: Digite primeiro o numero da base que o disco esta e o numero\n'
          'da base para qual ele sera movido, você deve mover um disco de cada vez,\n'
          'sendo que um disco maior nunca podera ficar em cima de um disco menor.\n')
    input('Tecle enter para comecar...')
    os.system('cls' if os.name == 'nt' else 'clear')

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

if(__name__ == "__main__"):
    os.system('cls' if os.name == 'nt' else 'clear')
    controlador()