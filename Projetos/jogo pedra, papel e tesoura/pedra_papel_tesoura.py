import random

def venceu(jogado, oponente):
    if (jogado == 'r' and oponente == 't') or (jogado == 't' and oponente == 'p') or\
    (jogado == 'p' and oponente == 'r'):
        return True

def jogo():
    
    jogador = input("'p' para papel, 'r' rocha/pedra ou 't' para tesoura: ")
    computador = random.choice(['p', 'r', 't'])
    
    if jogador == computador:
        return "Empate!"
        
    elif venceu(jogador, computador):
        return "Ganhou!"
        
    else:
        return "Perdeu!"
