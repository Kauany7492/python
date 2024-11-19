# O que é:
  # os booleanos são verdadeiros(True) ou falsos(False).
  # eles podem ser também 1 para verdadeiro ou 0 para falso

# Ex.:
a = True
b = False

# Função type():
  # mostra qual é o tipo de dado dentro de uma variável.

# Sintaxe:
  # type(variável)

#Ex.:
print(type(a))
print(type(b))

# Conversão:
  # retorna verdadeiro caso a variavel/objeto tenha um valor diferente doque está listado abaixo:
    # - 0
    # - None
    # - False
    # - " "
    # - ( )
    # - { }
    # - [ ] 

# Sintaxe:
  # bool(variavel/objeto)

#Ex.:
c = " "
d = "oi"

print(bool(c))
print(bool(d))

# Função isinstance():
  # verfica se uma veriavel/objeto é de um determinado tipo.
  # se o dado for do tipo determinado ele retorna "True", caso contrário ele retorna "False".

# Sintaxe:
  # isinstance(variavel/objeto, tipo de dado) 

e = 20
f = 60.5

print(isinstance(e, int))
print(isinstance(f, str))
