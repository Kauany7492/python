#4)Fazer um código que peça para o usuário escolher um número de 1 a 10 e assim tirar ele da conta

num = int(input("Digite um número: "))
i = 0

while num > 0 and num < 10:
    i += 1

    if i == num:
        continue
    print(i)