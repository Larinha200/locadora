import os
from claases import *

def menu():
  print("1-Cadastro cliente \n2-Cadastro de jogo  \n3-Cadastro de filme \n4-Listar tudo \n5-Listar jogos \n6-Listar filmes \n7-Alugar filme \n8-Alugar jogo \n9-Devolver filme \n10-Devolver jogo \n11-Sair")

def ls():
  os.system("pause")


def cadastro_jogo(lista_jogo):
   print("Bem vind* ao cadastro de jogos. \nInsira:")
   id = (len(lista_jogo)+1)
   titulo= input("Titulo:")
   plataforma=input("Plataforma:")
   faixa_etaria=input("Faixa etaria:")
   jogo= Jogos(id,titulo,plataforma,faixa_etaria)
   lista_jogo.append(jogo)

   for joggo in lista_jogo:
      print(f"{id} \n  Titulo:{joggo.getTitulo()} \n  Plataforma:{joggo.getPlataforma()} \n  Faixa etaria:{faixa_etaria}")


