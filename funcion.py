import os
from claases import *

def menu():
  print("1-Cadastro cliente  \n2-Cadastro de itens \n3-Listar tudo \n4-Listar jogos \n5-Listar filmes \n6-Listar clientes \n7-Alugar filme \n8-Alugar jogo \n9-Devolver filme \n10-Devolver jogo \n11-Sair")

def menu1():
  print("DIgite: \n1-Cadastro de jogo \n2-Cadastro de filme")

def menu2():
   print("Digite: \n1-Listar jogos \n2-Listar filmes")

def ls():
  os.system("pause")

def cadastro_cliente(Clientes,lista_cli):
    
    print("bem vind* ao cadastro. \nInsira seu:")
    nome=input("Nome:")
    cpf=input("CPF:")
    client=Clientes(nome,cpf)
    lista_cli.append(client)
    return client 
    
def cadastro_jogo(lista_jogo, Jogos, Locadora):
   print("Bem vind* ao cadastro de jogos. \nInsira:")
   id = (len(lista_jogo)+1)
   titulo= input("Titulo:")
   plataforma=input("Plataforma:")
   faixa_etaria=input("Faixa etaria:")
   jogo= Jogos(titulo,plataforma,faixa_etaria)
   

   

def cadastro_filme(lista_filme,Filmes):
    print("Bem vind* ao cadastro de filmes. \nInsira:")
    id = (len(lista_filme)+1)
    titulo= input("Titulo:")
    genero=input("Genero:")
    duracao=input("Duração:")
    filme= Filmes(titulo,genero,duracao)
    lista_filme.append(filme)
    Locadora.cadastrar_item()
    return Locadora.getItens()
    