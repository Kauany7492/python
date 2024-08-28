import random
nome = []
nome += input("Digite o nom do novo participante: ")
participantes = input("Tem mais paticipantes: ")

while participantes != "nao":
    nome += input("Digite o nom do novo participante: ")
else:
    print("Os prticipantes são: ", nome)

def jogo():
   a = random.randrange(0, len(nome))
   b = random.randrange(0, len(nome))

   if a != b:
        print(nome[a],"vai jogar contra", nome[b])


def pontos():
    jogo = input("Quem ganhou o jogo: ")
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


partidas = input("As partidas acabaram, sim ou nao: ")
while partidas != "sim":
    jogo()
    pontos()
else:
    print("Os jogos acabaram")