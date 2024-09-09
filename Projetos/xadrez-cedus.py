#-cadastrar os jogadores e separalos por categorias
#-sortear de dois em dois jogadores para iniciar uma rodada
#-separar quem ganhou de quem perdeu e fazer um sorteio com base nesta nova lista

import random


class cadastro:
    def __init__(self, nome, categoria, pontos):
        self.usuarios = {}
        self.nome = nome
        self.categoria = categoria
        self.pontos = pontos

    def cadastro_jogador(self, nome, categoria):
        self.usuarios[nome] = categoria
        print(f"Usuario {nome} cadastrado na categoria seguinte {categoria}")

    def lista_jogadores(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for self.nome in self.usuarios.items():
            print(f"Nome: {self.nome}, Categoria: {self.categoria}")

class rodada:
    cadastros = cadastro
    sub12 = {}
    sub14 = {}
    sub16 = {}
    sub18 = {}
    aberto = {}
    categoria = []

    cate = input("Escolha uma das seguintes caegorias de acordo com a sua idade: sub12, sub14, sub16, sub18, aberto(obrigatória para maiores de 18 anos)")
    if cate == "sub12":
        cadastros.categoria = "sub12"  
        sub12[cadastros.nome] = cadastros.pontos  
        categoria += ["sub12"]

    elif cate == "sub14":
        cadastros.categoria = "sub14"
        sub14[cadastros.nome] = cadastros.pontos
        categoria += ["sub14"]

    elif cate == "sub16":
        cadastros.categoria = "sub16" 
        sub16[cadastros.nome] = cadastros.pontos
        categoria += ["sub16"]

    elif cate == "sub18":
        cadastros.categoria = "sub18"  
        sub18[cadastros.nome] = cadastros.pontos
        categoria += ["sub18"]

    elif cate == "aberto":
        cadastros.categoria = "aberto"
        aberto[cadastros.nome] = cadastros.pontos
        categoria += ["aberto"]

    else:
        print("Categoria inválida.")

    def joga(a):
        del cadastro.usuarios[a]
    
    def partida():
        categoria = rodada.categoria
        part = int(input("Quantas pessoas vam participar: "))

        while part%2 == 0:
            sorteio = random.choice(categoria)
            return random.sample(sorteio, 2)
