#6)Fazer um código que mostre a lista de contas e remova uma delas

nomes = ["Alana", "Nata", "Rafhael", "Lucas", "Kauany"]

def rev(a):
    nomes.remove(a)

while len(nomes) > 4:
    print(nomes)
    esco = input("Escolha um para remover: ")

    if esco == "Alana" or esco == "Nata" or esco == "Rafhael" or esco == "Lucas" or esco == "Kauany":
        rev(esco)
        print(nomes)

    else:
        print("Escolha inválida")
