import random

def adivinha_numero(x):
    
    numero_aleatorio = random.randint(1, x)
    adivinha = 0
    
    while numero_aleatorio != adivinha:
        adivinha = int(input(f"Digite um numero entre 1 e {x}: "))
        
        if adivinha < numero_aleatorio:
            print("O número escolhido é menor que o número aleatório")
        
        elif adivinha > numero_aleatorio:
            print("O número escolhido é maior que o número aleatório")
            
        else:
            print(f"Você acertou o número aleatório {numero_aleatorio}")
            
adivinha_numero(10)
