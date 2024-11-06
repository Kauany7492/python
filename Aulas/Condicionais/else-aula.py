# O QUE É:
  # O else funciona em conjunto com o if e o elif, ele é execultado quando o if e o elif são falsos.

# SINTAXE:
  # else:
  #  | código a ser execultado caso o if e o elif forem falsos.

# Ex.:
a = 0
b = 3

if b > a:
  print(f"{a} é menor que {b}.")
else:
  print(f"{a} é maior que {b}.")

# Ex.:
if not b < a:
  print(f"{a} é menor que {b}")
else:
  print(f"{b} é menor que {a}")

# Ex.:
if a == 0 and b >= 3:
  print("a é igual a 0 e b é maior ou igual a 3")
else:
  print("a não é igual a 0 e b não é maior ou igual a 3")

# Ex.:
if a < b or b == 0:
  print(f"{a}, {b}")
else:
   print(f"{a}, {b}")
  
