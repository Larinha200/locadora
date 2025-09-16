from funcion import*
from claases import*
lista_cli=[]
lista_jogo=[]
list_filme=[]
itens_locados=[]
list_cli = Locadora()
menu()
resp=int(input("Digite: --->"))
while True:
    match resp:
        case 1:
            list_cli.Cadastrar_clientes(lista_cli, Clientes, cadastro_cliente)
            menu()
            resp=int(input("Digite: --->"))
           
        case 2:
            cadastro_jogo(lista_jogo)
            menu()
            resp=int(input("Digite: --->"))
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            list_cli.Listar_clientes()
            menu()
            resp=int(input("Digite: --->"))
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

        