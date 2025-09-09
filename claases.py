class Itens:
    def __init__(self, id:int, titulo:str, disponivel:bool):
        self.__id= id
        self.__titulo = titulo
        self.__disponivel = disponivel

    #metodos
    def Alugar():
        pass

    def Devolver():
        pass

    #metodos get e set
    def getTitulo(self):
        return self.__titulo
    
    def getDisponivel(self):
        return self.__disponivel
    
    def setTitulo (self,titulo:str):
        self.__titulo = titulo
        return self.__titulo
    
    def setDisponivel (self, disponivel:bool):
        self.__disponivel = disponivel
        return self.__disponivel

class Filmes(Itens):
    def __init__(self, id:int, titulo:str, genero:str, duracao:int):
        self.__id= id
        self.__titulo = titulo
        self.__genero = genero
        self.__duracao = duracao

    #metodos get e set
    def getTitulo(self):
        return self.__titulo
    
    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        return self.__titulo
    
    def setGenero(self,genero):
        self.__genero = genero
        return self.__genero
    
    def setDuracao(self,duracao):
        self.__duracao = duracao
        return self.__duracao
    
    
class Jogos(Itens):
    def __init__(self, id:int, titulo:str, plataforma:str, faixa_etaria:int):
        self.__id= id
        self.__titulo = titulo
        self.__plataforma = plataforma
        self.__faixa_etaria = faixa_etaria

class Clientes:
    def __init__(self,nome:str, cpf:str, itens_locados:list):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = itens_locados

    def Locar():
        pass
 
    def Devolver():
        pass

    def Listar_itens():
        pass

class Locadora:
    def __init__(self, clientes:list, itens:list):
        self.__clientes = clientes
        self.__itens = itens

    def Cadastrar_clientes():
        pass

    def Cadastrar_item():
        pass

    def Listar_clientes():
        pass

    def Lista_itens():
        pass