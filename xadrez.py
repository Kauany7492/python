import random
nome = ["Lucas", "Nata", "Alana", "Kauany", "Rafhael"]
print("Os prticipantes são: ", nome)

def jogo():
   a = random.randrange(0, len(nome))
   b = random.randrange(0, len(nome))
   print(a,"vai jogar contra", b)


def pontos():
    jogo = input("Quem ganhou o jogo: ")
    while jogo == "Lucas":
        i = 0
        i += 1
        print("Lucas tem ", i, "ponto(s)")
    else:
        print("Lucas tem ", 0, "pontos")
        

    while jogo == "Nata":
        i = 0
        i += 1
        print("Nata tem ", i, "ponto(s)")
    else:
        print("Nata tem ", 0, "pontos")


    while jogo == "Alana":
        i = 0
        i += 1
        print("Alana tem ", i, "ponto(s)")
    else:
        print("Alana tem ", 0, "pontos")


    while jogo == "Kauany":
        i = 0
        i += 1
        print("Kauany tem ", i, "ponto(s)")
    else:
        print("Kauany tem ", 0, "pontos")


    while jogo == "Rafhael":
        i = 0
        i += 1
        print("Rafhael tem ", i, "ponto(s)")
    else:
        print("Rafhael tem ", 0, "pontos")
        
jogo()
pontos()