class Itens:
    def __init__(self,id,titulo,disponivel):
        self.__id= id
        self.__titulo = titulo
        self.__disponivel = disponivel

    
    def Alugar():
        pass

    def Devolver():
        pass

class Filmes(Itens):
    def __init__(self,id, titulo,genero,duração):
        self.__id= id
        self.__titulo = titulo
        self.__genero = genero
        self.__duração = duração
    
class Jogos(Itens):
    def __init__(self,id, titulo,plataforma,faixa_etaria):
        self.__id= id
        self.__titulo = titulo
        self.__plataforma = plataforma
        self.__faixa_etaria = faixa_etaria

class Clientes:
    def __init__(self,nome, cpf, itens_locados):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = itens_locados

    def Locar():
        pass
 
    def Devolver():
        pass

    def Listar_itens():
        pass

