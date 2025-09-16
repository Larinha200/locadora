import os
from claases import *

def menu():
  print("1-Cadastro cliente \n2-Cadastro de jogo  \n3-Cadastro de filme \n4-Listar tudo \n5-Listar jogos \n6-Listar filmes \n7-Listar clientes \n8-Alugar filme \n9-Alugar jogo \n10-Devolver filme \n11-Devolver jogo \n12-Sair")

def ls():
  os.system("pause")

def cadastro_cliente(Clientes,lista_cli):
    
    print("bem vind* ao cadastro. \nInsira seu:")
    nome=input("Nome:")
    cpf=input("CPF:")
    client=Clientes(nome,cpf)
    lista_cli.append(client)
    return client 
    
def cadastro_jogo(lista_jogo):
   print("Bem vind* ao cadastro de jogos. \nInsira:")
   id = (len(lista_jogo)+1)
   titulo= input("Titulo:")
   plataforma=input("Plataforma:")
   faixa_etaria=input("Faixa etaria:")
   jogo= Jogos(id,titulo,plataforma,faixa_etaria)
   lista_jogo.append(jogo)

   for joggo in lista_jogo:
      print(f"{id} \n  Titulo:{joggo.getTitulo()} \n  Plataforma:{joggo.getPlataforma()} \n  Faixa etaria:{joggo.getFaixa_etaria}")

def cadastro_filme(lista_filme):
    print("Bem vind* ao cadastro de filmes. \nInsira:")
    id = (len(lista_filme)+1)
    titulo= input("Titulo:")
    genero=input("Genero:")
    duracao=input("Duração:")
    filme= Filmes(id,titulo,genero,duracao)
    lista_filme.append(filme)

    for fil in lista_filme:
        print(f"{id} \n  Titulo:{fil.getTitulo()} \n  Genero:{fil.getGenero()} \n  Duração:{fil.getDuracao}")
        