# O QUE SÃO:
  # são palavras ou números cercados pos aspas( '' → simples ou "" → duplas)
  # podem ser inseridas em variáveis e em algumas funções, como "print()"

#Ex.: 
a = "oi"
print(a)
print("ola")

# COMO PULAR LINHA:
  # para pular linha utiliza-se o \n.

# SINTAXE:
  # "string \n"

#Ex.:
nova-linha = "folha,\ncaule,\nterra"
print(nova-linha)

# FUNÇÃO LEN():
  # retorna o comprimento da string.

# SINTAXE:
  # len(string)

#Ex.:
b = "bom dia"
print(len(b))

# FUNÇÃO UPPER():
  # transforma a string toda em maiúscula.

# SINTAXE:
  # variavel.upper()

#Ex.:
c = "canada"
print(c.upper())

# FUNÇÃO LOWER():
  # transforma a string toda em minúsculo.

# SINTAXE:
  # variavel.lower()

#Ex.:
d = "DINAMARCA"
print(d.lower())

# FUNÇÃO STRIP():
  # remove os espaços do inicio e/ou do final da string.

# SINTAXE:
  # variavel.strip()

#Ex.:
e = "  espaço  "
print(e.strip())

# FUNÇÃO REPLACE():
  # troca uma string por outra.

# SINTAXE:
  # variavel.replace( string-antiga, string-nova)

#Ex.:
f = "bom dia, como vai?"
print(f.replace("bom dia", "boa tarde"))

# FUNÇÃO SPLIT():
  # retorna uma lista onde o texto entre o separador especificado se torna os itens da lista.

# SINTAXE:
    # variavel.split(separador)

#Ex.:
g = "goiaba, banana, cereja"
print(g.split(","))

# FUNÇÃO FORMAT(f):
  # utilixzado para adicionar strings com números em apenas uma variável.

# MODULOS:
  # {variavel:.nf} - "n" pode ser trocado por qualquer número, que será fixo como a quantidade de decimais a se colocados ao número da variável.
  # {numero operador numero} - utilizado para fazer contas dentro de uma strring.

# SINTAXE:
  # f"string {variavel, modulo ou numero}" 

#Ex.:
h = 16
print(f"Eu tenho {h} anos")
