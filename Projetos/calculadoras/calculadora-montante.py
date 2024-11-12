
def montante(capital, taxa, tempo):
  montante = capital*(1 + (taxa/100))**tempo
  print(f"M = {capital} × ( 1 + ({taxa} ÷ 100))^tempo")
  print(f"M = {montante})


capital1 = float(input("Digite o capital: "))
taxa1 = float(input("Digite a taxa em porcentagem: "))
tempo1 = float(input("Digite o tempo que seu capital foi aplicado: "))

montante(capital=capital1, taxa=taxa1, tempo=tempo1)
