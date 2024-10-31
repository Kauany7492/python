#Neste arquivo você verá o básico sobre o que é e como funciona a manipulação de arquivos em python.



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

#EXCLUIR ARQUIVO:

    # para excluir um arquivo é necessário importar a biblioteca os
    # os.remove("nome-do-arquivo.txt")

#BIBLIOTECA OS:

    # os.path.exists("nome-do-arquivo.txt") - verifica se o arquivo existe
    # os.rmdir("nome-da-pasta") - exclui a pasta inteira(se estiver vazia)
