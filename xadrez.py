import random
nome = []
nome += [input("Digite o nom do novo participante: ")]
print(nome)
participantes = input("Tem mais paticipantes: ")

while participantes != "nao":
    nome += [input("Digite o nom do novo participante: ")]
    participantes = input("Tem mais paticipantes: ")
else:
    print("Os prticipantes são: ", nome)

def jogo():
   a = random.randrange(0, len(nome))
   b = random.randrange(0, len(nome))

   if a != b:
        print(nome[a],"vai jogar contra", nome[b])


def pontos():
    jogo = input("Quem ganhou o jogo: ")

    while jogo == nome:
        i = 0
        i += 1
        print(nome[a], "tem", i, "ponto(s)")
        if jogo == "empate":
            i += 0.5
            print(nome[a], "e", nome[b], "tem", i,"ponto(s)")
    else:
        print(nome[a], "tem", i, "pontos")


    while jogo == nome:
        i = 0
        i += 1
        print(nome[b], "tem", i, "ponto(s)")
        if jogo == "empate":
            i += 0.5
            print(nome[a], "e", nome[b], "tem", i,"ponto(s)")
    else:
        print(nome[b], "tem", i, "pontos")
    


partidas = input("As partidas acabaram, sim ou nao: ")
while partidas != "sim":
    jogo()
    pontos()
else:
    print("Os jogos acabaram")