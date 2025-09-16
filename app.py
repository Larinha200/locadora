from funcion import*
from claases import*
lista_cli=[]
lista_jogo=[]
list_filme=[]
itens_locados=[]
list_cli = Locadora()
list_clii = Clientes(nome=str, cpf=str)
menu()
resp=int(input("Digite: --->"))
while True:
    match resp:
        case 1:
            list_cli.Cadastrar_clientes(lista_cli, Clientes, cadastro_cliente)
            menu()
            resp=int(input("Digite: --->"))
           
        case 2:
            menu1()
            resp3=int(input("Digite: --->"))
            match resp3:
                case 1:
                    list_cli.Cadastrar_jogo(lista_jogo)
                case 2:
                    list_cli.Cadastrar__filme(lista_filme)
                case _:
                    ("Opção invalida. digite outra")
        case 3:
            list_cli.Lista_itens()
            menu()
            resp=int(input("Digite: --->"))
        case 4:
           list_cli.Listar_jogo()
           menu()
           resp=int(input("Digite: --->"))
        case 5:
            list_cli.Listar_filme()
            menu()
            resp=int(input("Digite: --->"))
        case 6:
            list_cli.Listar_clientes()
            menu()
            resp=int(input("Digite: --->"))
        case 7:
            list_clii.locar( Itens)
        case 8:
            list_clii.locar(Itens)
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case _:
            pass

        