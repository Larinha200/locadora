class Itens:
    def __init__(self,Id,Titulo,Disponivel):
        self.__Id= Id
        self.__Titulo = Titulo
        self.__Disponivel = Disponivel

    
    def Alugar():
        pass

    def Devolver():
        pass

class Filmes(Itens):
    def __init__(self,Genero,Duração):
        self.__Genero = Genero
        self.__Duração = Duração
    

