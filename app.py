from funcion import*
from claases import*
lista_cli=[]
lista_jogo=[]
itens_locados=[]
list_cli = Locadora(clientes=[], itens = [])
menu()
resp=int(input("Digite: --->"))
while True:
    match resp:
        case 1:
            list_cli.Cadastrar_clientes(lista_cli)
            menu()
            resp=int(input("Digite: --->"))
           
        case 2:
            cadastro_jogo(lista_jogo)
            menu()
            resp=int(input("Digite: --->"))
        case 3:
            pass
        case 4:
            list_cli.Listar_clientes(lista_cli)
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case _:
            pass