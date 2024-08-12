#Lista: alterar estrutura
#nomedalista[numero do elemento a ser alterado]=elemento alterado

#Ex.:

mercado = ["maçã", "banana", "morango", "pêssego"]
print(mercado)
mercado[4]="abacaxi"
print(mercado)

#Lista: adicionar estrutura
#nomedalista.append(item a ser adicionado)

#Ex.:

letras = ["a", "b", "c", "d"]
print(letras)
letras.append("e")
print(letras)

#Lista: remover estrutura
#nomedalista.remove(item a ser removido)

#Ex.:

numeros = [1, 2, 3, 4, 5, 6]
print(numeros)
numeros.remove(6)
print(numeros)

#Dicionario: adicionar estrutura
#nomedodicionario[variavel]=valor

#Ex.:

carro = {
    "marca" : "ford",
    "modelo" : "mustang",
    "ano" : 1964
}
print(carro)
carro["cor"]="vermelho"
print(carro)

#Dicionario: alterar estrutura
#nomedodicionario[variavel]=valor alterado

#Ex.:

supermercado = {
    "arroz" : "R$20,50",
    "macarrão" : "R$5,90",
    "bolacha" : "R$9,90"
}
print(supermercado)
supermercado["arroz"]="R$15,40"
print(supermercado)
