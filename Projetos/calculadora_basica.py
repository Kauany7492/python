# Utilizando seus conhecimentos em python crie um programa que simule uma calculadora básica e que faça os seguintes calculos: adição, subtração, mutiplicação e divisão.
# OBS.: O código abaixo é uma das maneiras de resolver a questão acima.


def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


def calculadora():

    operacao = input("Escolha umaa operação (+, -, * ou /): ")
    num1 = float(input("Escolha o primeiro número: "))
    num2 = float(input("Escolha o segundo número: "))

    if operacao == "+":
        resultado = adicao(num1, num2)
        print("O resultado da adição é: ", resultado)

    elif operacao == "-":
        resultado = subtracao(num1, num2)
        print("O resultado da subtração é: ", resultado)

    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
        print("O resultado da multiplicação é: ", resultado)

    elif operacao == "/":
        resultado = divisao(num1, num2)
        print("O resultado da divisão é: ", resultado)

    else:
        print("Operação inválida!")

calculadora()
