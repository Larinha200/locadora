from funcion import*
class Itens:
    def __init__(self, id:int, titulo:str, disponivel:False):
        self.__id= id
        self.__titulo = titulo
        self.__disponivel = disponivel

    #metodos
    def Alugar(self):
        if self.__disponivel:
            self.__disponivel = False
            return f'O item {self.__titulo} alugado com sucesso!'
        else:
            return f'O item {self.__titulo} não esta disponivel para alugar.'

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
    
    def setDisponivel (self, disponivel:False):
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
        self.__itens_locados = []

    def locar(self, Itens):
        if Itens.getDisponivel():
            Itens.Alugar()
            self.__itens_locados.append(Itens)
            return f'Item "{Itens.getTitulo()}" alugado com sucesso para {self.__nome}.'
        else:
            return f'Item "{Itens.getTitulo()}" não está disponível para aluguel.'
    def Devolver():
        pass

    def Listar_itens():
        pass
    
    #get e set
    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def getItens_locados(self):
        return self.__itens_locados
    
    def setNome(self, nome):
        self.__nome = nome 
        return self.__nome
    
    def setCpf(self,cpf):
        self.__cpf = cpf
        return self.__cpf
    
    def setItens_locados(self,itens_locados):
        self.__itens_locados = itens_locados
        return self.__itens_locados


class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []
        self.__filme =[]
        self.__jogo =[]

    def Cadastrar_clientes(self,lista_cli, Clientes, cadastro_cliente):
        cliente = cadastro_cliente(Clientes, lista_cli)
        self.__clientes.append(cliente)
        return self.__clientes
        

    
    def Cadastrar_jogo(self,lista_jogo):
      
        jogo= cadastro_jogo(lista_jogo,Jogos)
        self.__jogo.append(jogo)
        return self.__jogo
    
    def Cadastrar__filme(self,lista_filme):
       
        filme= cadastro_filme(lista_filme,Filmes)
        self.__filme.append(filme)
        return  self.__filme

    def Listar_clientes(self):
        for cliente in self.__clientes:
            print(f"Nome: {cliente.getNome()}, CPF: {cliente.getCpf()}")

    def Listar_filme(self):
        for fil in self.__filme:
            print(f"{id} \n  Titulo:{fil.getTitulo()} \n  Genero:{fil.getGenero()} \n  Duração:{fil.getDuracao()}")
         

    def Listar_jogo(self):
        for joggo in self.__jogo:
            print(f"{id} \n  Titulo:{joggo.getTitulo()} \n  Plataforma:{joggo.getPlataforma()} \n  Faixa etaria:{joggo.getFaixa_etaria()}")  

    def Lista_itens(self):
        for fil in self.__filme:
            print(f"{id} \n  Titulo:{fil.getTitulo()} \n  Genero:{fil.getGenero()} \n  Duração:{fil.getDuracao()}")
        for joggo in self.__jogo:
            print(f"{id} \n  Titulo:{joggo.getTitulo()} \n  Plataforma:{joggo.getPlataforma()} \n  Faixa etaria:{joggo.getFaixa_etaria()}")  
    


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
    