import random

def sorteios(a):
    b = len(a)
    c = random.randrange(0, b)
    d = random.randrange(0, b)
    while c != b:
        a.pop(c)
        a.pop(d)
        
        print(a.items(c), "vai jogar contra ", a.items(d))

class cadastro:
    def __init__(self, nome, categoria, pontos):
        self.usuarios = {}
        self.nome = nome
        self.categoria = categoria
        self.pontos = pontos


    def cadastro_jogador(self, nome, categoria):
        self.usuarios[nome] = categoria
        print(f"Usuario {nome} cadastrado na categoria seguinte {categoria}")


    def lista_jogadores(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for self.nome in self.usuarios.items():
            print(f"Nome: {self.nome}, Categoria: {self.categoria}")
            
def menu():
    cadastro = cadastro
    
    while True:
        print("\n Menu:")
        print("1- Cadastrar jogador")
        print("2- Listar jogadores")
        print("3- Iniciar as rodadas")
        print("4- Adicionar pontos aos jogadores")
        print("5- Sair")
        
        esco = input("Escolha uma das opções (1, 2, 3, 4 ou 5): ")
        
        if esco == "1":
            nome = input("Digite seu nome: ")
            cadastro.categoria = input(f"Em que categoria {nome} vai jogar (sub12, sub14, sub16, sub18 ou aberto: ")
            
            if cadastro.categoria == "sub12":
                sub12 = dict(nome = "sub12")
            elif cadastro.categoria == "sub14":
                sub14 = dict(nome = "sub14")
            elif cadastro.categoria == "sub16":
                sub16 = dict(nome = "sub16")
            elif cadastro.categoria == "sub18":
                sub18 = dict(nome = "sub18")
            elif cadastro.categoria == "aberto":
                aberto = dict(nome = "aberto")
            else:
                print("Você não respondeu corretamente, responda novamente")
        elif esco == "2":
            cadastro.lista_jogadores()
        elif esco == "3":
            sorteios(sub12)
            sorteios(sub14)
            sorteios(sub16)
            sorteios(sub18)
            sorteios(aberto)
        elif esco == "4":
            jogador = input("Digite o nome do jogador em que você deseja adicionar uma pontuação: ")
            pont = float(input("Qual a pontuaçaõ a ser adicionada: "))
            ponto = dict(jogador = pont)
            
            print(ponto)
        elif esco == "5":
            print("Saindo...")
            break
        else:
            print("Resposta incorreta.")


if __name__ == "_main_":
    menu()
    