#5)Fazer um código que mostre a lista de contas e remova uma delas

nomes = ["Alana", "Nata", "Rafhael", "Lucas", "Kauany"]

while len(nomes) > 4:
    print(nomes)
    esco = input("Escolha um para ser removido: ")

    if esco == "Alana":
        nomes.remove("Alana")
        print(nomes)

    elif esco == "Nata":
        nomes.remove("Nata")
        print(nomes)

    elif esco == "Rafhael":
        nomes.remove("Rafhael")
        print(nomes)

    elif esco == "Lucas":
        nomes.remove("Lucas")
        print(nomes)

    elif esco == "Kauany":
        nomes.remove("Kauany")
        print(nomes)

    else:
        print("Escolha inválida")

# Outra maneira de resolver:
nomes = ["Alana", "Kauany", "Lucas", "Nata", "Rafhael"]

while len(nomes) > 4:
    print(nomes)
    escolha = input("Quem sera removido: ")
    
    for x in nomes:
        if x == escolha:
            nomes.remove(x)
    print(nomes)
