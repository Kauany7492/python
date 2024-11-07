# O QUE É:
  # é utilizado para interagir com uma sequência, podendo ser qualquer tipo de lista ou uma string.

# FOR - LISTAS:

  # SINTAXE:
    # for variável in lista:
      # | código para interagir com a lista.

  # Ex.: 
frutas = ['maca', 'banana', 'cereja']
for x in frutas:
  print(x)

# FOR - STRING:

  # SINTAXE:
    # for variável in "string":
      # | código para interagir com a lista.

  # Ex.:
for x in "banana":
  print(x)

# FUNÇÕES:
  # Break: para um loop antes que ele percorra todos os itens.
  # Continue: para a interação atual do loop e continua com a próxima.
  # Range: retorna uma sequência de números começando em 0 até um número especificado.
  # Else: execulta um bloco de código quando o loop for concluído.

# FOR - BREAK:

  # Ex.:

for x in frutas:
  print(x)
  if x == "banana":
    break

# FOR - CONTINUE:

  #Ex.:
for x in frutas:
  if x == "banana":
    continue
  print(x)

# FOR - RANGE():

  # COM UM PARÂMETRO:

    #Ex.:
for x in range(6):
  print(x)

  # COM DOIS PARÂMETROS:
    # A contagem vai começar com o primeiro parâmetro e terminará com um número antes do segundo parâmetro.

    #Ex.:
for x in range(2,6):
  print(x)

  # COM TRÊS PARÂMETROS:
    # Os dois primeiros parâmetros já foram explicados anteriormente, o terceiro parâmetro indica de qual é o valor da distância de um número ao outro.

    #Ex.:
for x in range(2, 30, 3):
  print(x)

  # FOR - ELSE:

    #Ex.:
for x in range(6):
  print(x)
else:
  print("terminei")
  
