
class Torre():
    def __init__(self, lista):
        self.__dados = lista

    @property
    def dados(self):
        return self.__dados
    @property
    def toString(self):
        saida = []
        for i in range(0, 4 - len(self.__dados)):
            saida.append(' ')
        saida.extend(self.__dados)
        return saida

    def empilha(self, elemento):
        self.dados.insert(0, elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(0)

    def vazia(self):
        return len(self.dados) == 0

    def ultimo(self):
        if(not self.vazia()):
            return self.__dados[0]