import random
import uuid
nome = ["Lucas","Nata","Alana","Kauany","Rafhae"]

print("Os prticipantes são: ", nome)

def partida():
    a = random.randrange(0, len(nome))
    b = random.randrange(0, len(nome))

    if a != b:
        print(nome[a],"e", nome[b])

    partic = print(nome[a],"vai jogar contra", nome[b])

    jogo = input("Quem ganhou o jogo: ")
    while jogo == "empate":
        i = 0
        i += 0.5
        print(nome[a],"e",nome[b], "ganharam 0,5 ponto(s)")
        break
    while jogo == "Lucas":
        i = 0
        i += 1
        print("Lucas tem ", i, "ponto(s)")
        break
    else:
        print("Lucas tem ", 0, "pontos")
        
    while jogo == "Nata":
        i = 0
        i += 1
        print("Nata tem ", i, "ponto(s)")
        break
    else:
        print("Nata tem ", 0, "pontos")

    while jogo == "Alana":
        i = 0
        i += 1
        print("Alana tem ", i, "ponto(s)")
        break
    else:
        print("Alana tem ", 0, "pontos")

    while jogo == "Kauany":
        i = 0
        i += 1
        print("Kauany tem ", i, "ponto(s)")
        break
    else:
        print("Kauany tem ", 0, "pontos")

    while jogo == "Rafhael":
        i = 0
        i += 1
        print("Rafhael tem ", i, "ponto(s)")
        break
    else:
        print("Rafhael tem ", 0, "pontos")


class CadastroEvento:
    def __init__(self):
        self.usuarios = {}

partidas = input("As partidas acabaram, sim ou nao: ")
while partidas != "sim":
   partida()
else:
    print("Os jogos acabaram")