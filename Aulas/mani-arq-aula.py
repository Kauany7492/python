#O QUE É: 
    # É utilizado para analise de dados com o python

#INICIO:
    #para abrir um arquivo utilizamos a função open() com dois parâmetros 
    #sendo eles o nome do arquivo e o modo/método

#MODOS/MÉTODOS:

    # r : permiti abrir um arquivo para leitura(da erro se o arquivo não existir)
        # nome-do-arquivo.read(número de caracteres)
        # nome-do-arquivo.readline() - retorna a primira linha do arquivo
    # a : permiti abrir um arquivo para escrita(adiciona tudoao final do arquivo)
        # nome-do-arquivo.write("o que sera adicionado ao arquivo")
    # w : permiti abrir um arquivo para escrita(substitui todo o arquivo)
        # nome-do-arquivo.write("o que ira substituir ")
    # x : permiti apenas criar um arquivo(da erro se o arquivo existir)
   
#FORMATOS:

    # t : permiti criar um arquivo no formato de texto(padrão)
        # f = open("nome-do-arquivo.txt", 'modo/t')
    # b : permiti criar um arquivo em formato binario(ex.: imagens)
        # f = open("nome-do-arquivo.txt", 'modo/b')

#SINTAXE:

    # f = open("nome-do-arquivo.txt", 'modo/formato')
    # f.close() - fecha o arquivo


#EX.:

f = open('meuarquivo.txt', 'w')
f.write("Ola, seja bem vindo(a)")
f.close()

f = open('meuarquivo.txt', 'r')
print(f.read()) 
f.close()

# APROFUNDAMENTO:
    # você pode escrever o mesmo código acima usando uma função "with".
    # com a função "with" você não precisa fechar o arquivo, a função fecha automática.

# SINTAXE:
    # with open('arquivo.txt', 'modulo/formato') as nome-da-variavel:
        # | o que você quer fazer com o arquivo

#Ex.:

with open('meuarquivo.txt', 'w') as f:
    f.write("Ola, seja bem vindo(a)")
    
with open('meuarquivo.txt', 'r') as f:
    print(f.read()) 

#EXCLUIR ARQUIVO:

    # para excluir um arquivo é necessário importar a biblioteca "os"

# SINTAXE:

    # os.remove("nome-do-arquivo.txt")

#BIBLIOTECA OS:

    # os.path.exists("nome-do-arquivo.txt") - verifica se o arquivo existe
    # os.rmdir("nome-da-pasta") - exclui a pasta inteira(se estiver vazia)

# Vídeos sobre manipulação de arquivos:

'''
1-Vídeo sobre manipulação de arquivos de texto(ler, editar e criar):
    https://youtu.be/AvUG8wZMh_E?si=QBniMd1Hx01b3OF0

2-Vídeo sobre manipulação de arquivos(iniciantes):
    https://youtu.be/G-kUBX0U8IQ?si=panU0A24lANsLW0I

3-Série de vídeos sobre manipulação de arquivos(txt, CSV e Jason) básico:
    1-https://youtu.be/10Pdysnsihg?si=8lghx9aWQEDl22qm
    2-https://youtu.be/xIC2xyLmo7M?si=-PQMaqTtpCa_to_Z
    3-https://youtu.be/6iAOrL5TBe8?si=wc_7uSI8rwiljsCa
    4-https://youtu.be/yNFiFQ-AI4Q?si=55I72FgNSQV_CDOm
    5-https://youtu.be/S26BbiBC4lY?si=iBQg4hGZZT74YsbN
'''
