from funcion import*
clientes=[]
itens_locados=[]
menu()
resp=int(input("Digite: --->"))
while True:
    match resp:
        case 1:
            cadastro_cliente(clientes)
            menu()
            resp=int(input("Digite: --->"))
           
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
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