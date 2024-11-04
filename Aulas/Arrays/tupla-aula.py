# Neste arquivo você verá o básico de o que são e como funcionam as listas do tipo tupla.

# O QUE É?
  # As 'tuplas' são muito parecidas com as 'listas', as diferenças mais notáveis entre elas são que as 'tuplas' são imutáveis, ou seja, não é possível alterar os itens dentro dela após ela ser criada.

# SINTAXE:
  # variável = ( "valor1", 2, "valor3", 4.5)
  # EX.:
x = ("maca", "banana", "cereja")
print(x)


# COMO ACESSAR UM ITEM:
  # nome-da-tupla[numero-do-item]
x = ("maca", "banana", "cereja")
print(x)
print(x[1])

  # nome-da-tupla[-1]
      # referece ao último item da tupla
x = ("maca", "banana", "cereja")
print(x)
print(x[-1])
  # nome-da-tupla[-2]
      # referece ao penúltimo item da tupla
x = ("maca", "banana", "cereja")
print(x)
print(x[-2])


# UMA MANEIRA DE "ALTERAR" A TUPLA É DA SEGUINTE MANEIRA:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
