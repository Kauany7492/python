# Faça um comentário em frente a cada linha ou acima dela no código a seguir para descrever com suas palavras qual é a ação que esta lina está execultando.
# OBS.: Caso desconheça uma função/palavra do código sintase a vontade para pesquisar seu significado. Este exercício tem o objetivo de mostrar na prática como algumas funções podem ser utilizadas e para que a pessoa que responda ela veja onde tem mais dificuldades.



import random
import os

if os.path.exists("id.txt"):
    print()
else:
    f = open ("id.txt", 'w')
    f.write("0")
    f.close()

def mostrarmenu():

    indice = 0

    while True:        
        print("\n Menu:")    
        print("1- Cadastrar jogador")    
        print("2- Listar jogadores")    
        print("3- Iniciar uma rodada")    
        print("4- Adicionar pontos aos jogadores")    
        print("5- Sair")      
        escolha_menu = input("Escolha uma das opções: 1, 2, 3, 4 e 5:  ")

        def extrair_linha(arquivo, numero_linha):
                f = open(arquivo, 'r')
                linhas = f.read().splitlines()
                return linhas[numero_linha].split()

        def pontuacao(arquivo, adicionar):
                pontoantigo = extrair_linha(arquivo=arquivo, numero_linha=3)
                ponto = [float(i) for i in pontoantigo]
                p = ponto[0]
                novapont = adicionar + p
               
                f = open(arquivo, 'r')
                dados = f.read()
                alterapont = dados.replace(f"{p}", f"{novapont}")
               
                f = open(arquivo, 'w')
                f.write(alterapont)
                f.close()
               
                f = open(arquivo, 'r')
                dados = f.readlines()
                idjogador = dados[1].rstrip()
                idjogador = int(idjogador[5:6])
                f.close()

                f = open("listacadastro.txt", 'a')
                dados = f.readlines()
                dados.insert((2*idjogador), novapont + "\n")
               
        if escolha_menu == "1":
           
            linha = extrair_linha(arquivo="id.txt", numero_linha=0)
            id = int(linha[0])

            id += 1
            nome = input("Nome do jogador:  ")
            categoria = input("categoria do jogador:  ")
            pontos = float(input("Pontuação do jogador:  "))

            with open ("listacadastro.txt", 'a+') as listacadastro:
                listacadastro.write(f"{nome}\n {categoria} \n {pontos} \n \n")
           
            arquivo = nome + ".txt"
            f = open (arquivo, 'w')
            f.write(f"Jogador: {nome}\n id: {id}\n categoria:{categoria}\n {pontos}\n")
            f.close()
            f=open(arquivo,'r')
            print(f.read())
            f.close()
           
            with open ("id.txt", 'w') as registro:
                registro.write(f"{str(id)}")  
       
        elif escolha_menu == "2":
            f = open ("listacadastro.txt", 'r')
            print(f.read())
            f.close()
       
        elif escolha_menu == "3":

            id_rodada = input("Número da rodada: \n")
            f = open (id_rodada + "rodada.txt", 'a')
            f.close()

            linha = extrair_linha(arquivo="id.txt", numero_linha=0)
            id = int(linha[0])

            listasorteio = []
            x = 0
            while len(listasorteio) < id:
                f = open ("listacadastro.txt", 'r')
                lista = f.readlines()
                listasorteio.append(lista[x].rstrip())
                x = x + 4
               
                if x > len(lista):
                    break

            indice = 0
            while len(listasorteio) >= 2:

                jogador1, jogador2 = random.sample(listasorteio, 2)
                pontos1 = extrair_linha(arquivo = jogador1 + ".txt", numero_linha = 3)
                p1 = float(pontos1[0])
                pontos2 = extrair_linha(arquivo = jogador2 + ".txt", numero_linha = 3)
                p2 = float(pontos2[0])
                validar = abs(p1 - p2)

                while validar > 1.5:

                    jogador1, jogador2 = random.sample(listasorteio, 2)
                    pontos1 = extrair_linha(arquivo = jogador1 + ".txt", numero_linha = 3)
                    p1 = float(pontos1[0])
                    pontos2 = extrair_linha(arquivo = jogador2 + ".txt", numero_linha = 3)
                    p2 = float(pontos2[0])
                    validar = abs(p1 - p2)

                else:
                    listasorteio.remove(jogador1)
                    listasorteio.remove(jogador2)
                    indice += 1
                   
                    f = open ("rodada" + id_rodada + ".txt", 'a')
                    f.write(f"MESA {indice}: {jogador1.rstrip()} x {jogador2.rstrip()} \n")
                    f.close()

                if len(listasorteio) == 1:
                    impar = listasorteio[0]
                    nome = impar.rstrip()
                    f = open (id_rodada + "rodada.txt", 'a')
                    f.write(f"\n O jogador {nome} vai para a próxima rodada.")
                    f.close()

                    pontuacao(arquivo = nome + ".txt", adicionar = 0.5)

                    listasorteio.remove(impar)
                    
            f = open(id_rodada + "rodada.txt", 'r')    
            print(f.read())

        elif escolha_menu == "4":
            nomejogador = input("Digite o nome do jogador:")
            arquivo = nomejogador + ".txt"
            adicionar = float(input("Digite a pontuacao a ser adicionada ao jogador: "))
           
            pontuacao(arquivo = arquivo, adicionar = adicionar)

            f = open(arquivo, 'r')
            print(f.read())
            f.close()

            with open("listacadastro.txt", "r") as arquivo:
                 linhas = arquivo.readlines()
                 for linha in linhas:
                     indice += 1

            for o in range(1, indice, 4):
               selecionar = extrair_linha(arquivo= "listacadastro.txt", numero_linha= o -1)
               print(selecionar)
               if nomejogador  == selecionar[0]:
                   
                    pontoantigo = extrair_linha(arquivo=  "listacadastro.txt", numero_linha= o + 1)
                    ponto = [float(i) for i in pontoantigo]
                    p = ponto[0]
                    novapont = adicionar + p
               
                    f = open("listacadastro.txt", 'r')
                    i = f.readlines()
                    f.close

                    i.pop(o + 1)
                    i.insert(o + 1, f" {novapont} \n")
               
                    f = open("listacadastro.txt", 'w')
                    f.writelines(i)
                    f.close()
            indice = 0

        elif escolha_menu == "5":
            print("Fechando programa...")
            break

        else:
            print("Opção inválida")

if __name__=="__main__":
    mostrarmenu()
          
