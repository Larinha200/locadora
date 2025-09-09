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
    def __init__(self,Id, Titulo,Genero,Duração):
        self.__Id= Id
        self.__Titulo = Titulo
        self.__Genero = Genero
        self.__Duração = Duração
    
class Jogos(Itens):
    def __init__(self,Id, Titulo,Plataforma,Faixa_etaria):
        self.__Id= Id
        self.__Titulo = Titulo
        self.__Plataforma = Plataforma
        self.__Faixa_etaria = Faixa_etaria

class Clientes:
    def __init__(self,Nome, Cpf, Itens_locados):
        self.__Nome = Nome
        self.__Cpf = Cpf
        self.__Itens_locados = Itens_locados

