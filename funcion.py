import os
from claases import *

def menu():
  print("1-Cadastro cliente \n2-Cadastro de jogo  \n3-Cadastro de filme \n4-Listar tudo \n5-Listar jogos \n6-Listar filmes \n7-Alugar filme \n8-Alugar jogo \n9-Devolver filme \n10-Devolver jogo \n11-Sair")

def ls():
  os.system("pause")

def cadastro_cliente(clientes):
    
    print("bem vind* ao cadastro. \nInsira seu:")
    nome=input("Nome:")
    cpf=input("CPF:")
    client=Clientes(nome=nome,cpf=cpf)
    clientes.append(client)
    
    print(clientes)
