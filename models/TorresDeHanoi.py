from .Torre import Torre

class TorresDeHanoi():
    def __init__(self):
        self.__torres = [Torre([1, 2, 3, 4]), Torre([]), Torre([])]
        self.__movimentos = 0

    def movimento(self, de, para):
        if (not self.__torres[de].vazia() and (
                self.__torres[para].vazia() or 
                self.__torres[para].ultimo() > self.__torres[de].ultimo()
                )):
            
            self.__torres[para].empilha(self.__torres[de].ultimo())
            self.__torres[de].desempilha()
            self.__movimentos += 1
        else:
            print('Movimento Invalido')
    
    @property
    def movimentos(self):
        return self.__movimentos

    def exibe(self):
        print('Torres: ')
        for i in range(0, 4):
            print("| {} | {} | {} |".format(self.__torres[0].toString[i],
                                            self.__torres[1].toString[i],
                                            self.__torres[2].toString[i]
                                            ))
    def ganhou(self):
        return len(self.__torres[2].dados) == 4