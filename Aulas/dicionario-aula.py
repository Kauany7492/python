#Neste arquivo você verá o básico sobre o que é como funciona os dicionários em python. Este arquivo pode teajudar a aprender de maneira simplis como funcionam os dicionários em python.



# Dicionário: variavel que recebe mais de um valor. Os valores sao agrupados em pares.
    # nomedodicionario={"variavel":"valor", "variavel1":"valor1", "variavel2":"valor2"}

# Dicionário: adicionar estrutura
    # nomedodicionario[variavel]=valor

#Ex.:

carro = {
    "marca" : "ford",
    "modelo" : "mustang",
    "ano" : 1964
}
print(carro)
carro["cor"]="vermelho"
print(carro)

# Dicionário: alterar estrutura
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

# Dicionário: remover estrutura
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

# Vídeos sobre dicionários e tipos de listas:
'''
1-Vídeo sobre lista, tupla, conjuntos e dicionários:
https://youtu.be/0zYuLLIzPIQ?si=jl5YlEMU4Ij9dhpB

2-Vídeo sobre dicionários:
https://youtu.be/YwENuegbpEM?si=T4Ogq_AqlB_TKM4l
'''
