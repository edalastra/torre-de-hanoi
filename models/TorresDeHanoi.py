from .Torre import Torre

class TorresDeHanoi():
    def __init__(self):
        self.__torres = [Torre([1, 2, 3, 4]), Torre([]), Torre([])]

    def movimento(self, de, para):
        if (not self.__torres[de - 1].vazia() and (
                self.__torres[para - 1].vazia() or self.__torres[para - 1].ultimo() > self.__torres[de - 1].ultimo())):
            self.__torres[para - 1].empilha(self.__torres[de - 1].ultimo())
            self.__torres[de - 1].desempilha()
        else:
            print('Movimento Invalido')

    def exibe(self):
        for i in range(0, 4):
            print("| {} | {} | {} |".format(self.__torres[0].toString[i],
                                            self.__torres[1].toString[i],
                                            self.__torres[2].toString[i]
                                            ))
    def ganhou(self):
        return len(self.__torres[2].dados) == 4