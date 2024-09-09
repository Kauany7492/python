#Dicionario: variavel que recebe mais de um valor. Os valores sao agrupados em pares.
#nomedodicionario={"variavel":"valor", "variavel":"valor1", "variave2":"valor2"}
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

#Dicionario: remover estrutura
#nomedodicionario.pop(valor a ser removido)

#Ex.:

acougue = {
    "carne1" : "bovina",
    "carne2" : "frango",
    "carne3" : "porco"
}
print(acougue)
acougue.pop("carne2")
print(acougue)