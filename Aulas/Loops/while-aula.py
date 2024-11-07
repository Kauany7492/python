# O QUE É:
  # cria um loop que execulta um blco de código enquanto uma condição for verdadeira.

# SINTAXE:
  # while condição:
    # | bloco de código a ser execultado.

#Ex.:
i = 1
while i < 6:
  print(i)
  i += 1
  

# FUNÇÕES:
  # BREAK: para o loop mesmo se a condição for verdadeira.
  # CONTINUE: para a interação atual e continua com a próxima.
  # ELSE: execulta um bloco de código quando a condição for falsa.

# WHILE - BREAK:

  #Ex.:
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# WHILE - CONTINUE:

  #Ex.:
while i < 6:
  i += 1
  if i == 3:
    continue
 	print(i)

# WHILE - ELSE:

  #Ex.:
while i < 6:
  print(i)
  i += 1
else:
  print("i não é menor que 6
        
