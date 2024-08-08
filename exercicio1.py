#1)Fazer um código que pergunte se o usuário gosta de programar e se  não for respondido sim ou não ele vai repetir a pergunta.

per = input("Você gosta de programar? ")

while per == "s" or per == "n":
    print("Obrigado pela colaboração! ")

while per != "s" or per != "n":
    print("Você não respondeu corretamente responda novamente")
    per = input("Você gosta de programar? ")
