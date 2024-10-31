#Neste arquivo você verá o básico sobre o que é e como funciona as funções em python.



#Uma função é um bloco de código que só é executado quando é chamado.

#Como resultado, uma função pode retornar dados.
    
    #def nome-da-funcao(): 
    #  | o que vai ocorrer quando a função for chamada

#Ex.:

def funcao():
    print("Bom dia")

funcao()

#Podemos adicionar um argumento especifico dentro dos parenteses.
   
    #def nome-da-funcao(argumento):
    #  | o que vai ocorrer quando a função for chamada

#Ex.:

def nomes(nome):
    print(f"Bem vindo {nome}")

name = input("Digite seu nome: ")
nomes(name)

# Videos sobre função:
'''
1- Vídeo sobre Funções(básico):
https://youtu.be/XbvSBegg09s?si=ByvxvVbsnRhaJFep

2- Vídeo sobre o que é uma função:
https://youtu.be/kYnPpUn8_kA?si=e2KMhyBqsFLyL1bG
'''
