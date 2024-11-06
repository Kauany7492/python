# O QUE É:
  # verifica se uma condição é verdadeira. Caso ela seja verdadeira ele execulta o código contido dentro dele.

# SINTAXE:
  # if condição:
  #  | código a ser execultado caso a condição seja verdadeira.
  # podemos declarar o if em uma linha apenas da seguinte maneira:
    # if condição: código a ser execultado caso a condição seja verdadeira


# CONDICIONAIS:
  # < ou > → menor que ou maior que
  # <= ou >= → menor ou igual a ou maior ou igual a
  # == → igual
  # != → diferente

  # é possivel adicionar mais de uma condicional com os argumentos eguintes:
  # or → uma das condições tem que ser verdadeira.
  # and → ambas as condições tem que ser verdadeiras.
  # not → inverte a condição.

# Ex.:
a = 0
b = 3

if b > a:
  print(f"{a} é menor que {b}.")

# Ex.:
if not b < a:
  print(f"{a} é menor que {b}")

# Ex.:
if a == 0 and b >= 3:
  print("a é igual a 0 e b é maior ou igual a 3")

# Ex.:
if a < b or b == 0:
  print(f"{a}, {b}")
