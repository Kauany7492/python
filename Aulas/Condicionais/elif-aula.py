# O QUE É:
  # O elif fuunciona em conjunto com o if, ele verifica se outra condição é verdadeira quando o if for falso.

# SINTAXE:
  # elif condição:
  #  | código a ser execultado caso a condição for verdadeira

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
b = 7
if b < a:
  print(f"{b} é menor que {a}")
elif b > a:
  print(f"{b} é maior que {a}")

# Ex.:
if not b < a:
  print(f"{a} é menor que {b}")
elif b > a:
  print(f"{b} é maior que {a}")

# Ex.:
if a == 0 and b >= 7:
  print("a é igual a 0 e b é maior ou igual a 7")
elif b > a and b == 7:
  print(f"{b}, {a}")

# Ex.:
if a < b or b == 0:
  print(f"{a}, {b}")
elif b > a or a > b:
  print(f"{b} é maior que {a}")
  
