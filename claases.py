from funcion import*
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
    
    
    def getTitulo(self):
        return self.__titulo
    
    def getPlataforma(self):
        return self.__plataforma
    
    def getFaixa_etaria(self):
        return self.__faixa_etaria
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        return self.__titulo
    
    def setPlataforma(self, plataforma:str):
        self.__plataforma = plataforma
        return self.__plataforma

    def setFaixa_etaria(self, faixa_etaria:int):
        self.__faixa_etaria = faixa_etaria

class Clientes:
    def __init__(self,nome:str, cpf:str):
        self.__nome = nome
        self.__cpf = cpf
        #self.__itens_locados = itens_locados

    def Locar():
        pass
 
    def Devolver():
        pass

    def Listar_itens():
        pass
    
    #get e set
    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    #def getItens_locados(self):
        return self.__itens_locados
    
    def setNome(self, nome):
        self.__nome = nome 
        return self.__nome
    
    def setCpf(self,cpf):
        self.__cpf = cpf
        return self.__cpf
    
    #def setItens_locados(self,itens_locados):
        self.__itens_locados = itens_locados
        return self.__itens_locados


class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []

    def Cadastrar_clientes(self,lista_cli, Clientes):
        
        print("bem vind* ao cadastro. \nInsira seu:")
        nome=input("Nome:")
        cpf=input("CPF:")
        client=Clientes(nome,cpf)
        lista_cli.append(client)
        return client 
    
        

    
    def Cadastrar_item():
        pass

    def Listar_clientes(self):
        for cliente in self.__clientes:
            print(f"Nome: {cliente.getNome()}, CPF: {cliente.getCpf()}")
            

    def Lista_itens():
        pass
    
    #get e set
    def getClientes(self):
        return self.__clientes
    
    def getItens(self):
        return self.__itens
    
    def setClientes(self,clientes:list):
        self.__clientes = clientes
        return self.__clientes
    
    def setItens(self,itens:list):
        self.__itens = itens
        return self.__itens
    