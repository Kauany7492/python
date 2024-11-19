# 2) Faça um programa que peça uma peça de roupa e seu valor e imprima na tela a peça e o valor.
#Exemplo de resposta:

roupa = input("Digite a peça de roupa: ")
valor = int(input("Digite o valor arredondado da peça (ex.: 10.50 fica 11): "))

print(f"A peça {roupa} está custando {valor:.2f}")
