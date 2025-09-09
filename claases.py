class Itens:
    def __init__(self, id:int, titulo:str, disponivel:bool):
        self.__id= id
        self.__titulo = titulo
        self.__disponivel = disponivel

    
    def Alugar():
        pass

    def Devolver():
        pass

class Filmes(Itens):
    def __init__(self, id:int, titulo:str, genero:str, duração:int):
        self.__id= id
        self.__titulo = titulo
        self.__genero = genero
        self.__duração = duração
    
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