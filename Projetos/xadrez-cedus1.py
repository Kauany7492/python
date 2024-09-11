import random #importa um modulo aleatório(random)

def sorteios(a): #define a função chamada sorteio com a variavél a como argumento
    b = len(a) #cria avariavél b que vai receber o comprimento do argumento a
    while b % 2 == 0: #enquanto o resto da divisão da variavél b por 2 for 0 o código abaixo será executado:
        c = random.randrange(0, b) #cria a variavél c que vai receber um número aleatório entre 0 e a variavél b
        d = random.randrange(0, b) #cria a variavél d que vai receber outro número aleatório entre 0 e a variavél b
    while c != b: #adiciona um loop com a condição de que enquanto a variavél c for diferente de b vai acontecer o código abaixo:
        a.pop(c) #a variavél c vai ser removida do dicionário a
        a.pop(d) #a variavél d vai ser removida do dicionário a
        
        print(a.items(c), "vai jogar contra ", a.items(d)) #imprimi no terminal a chave e o valor c e d do dicionário a da seguinte maneira: chave:valor(c) vai jogar contra chave:valor(d)

class cadastro: #cria um objeto chamado de cadastro
    def __init__(self, nome, categoria, pontos): #define a instância(objeto) da classe com as variaveis nome,categoria e pontos como argumento e self como referência da instância(objeto) 
        self.usuarios = {} #define que a referência da instância(objeto) usuarios é um dicionário
        self.nome = nome #define que a referência de instância(objeto) nome vai receber a variavél nome declarada como argumento
        self.categoria = categoria #define que a referência da intância(objeto) categoria vai receber a variavél categoria declarada como argumento
        self.pontos = pontos #define  que a referência da instância(objeto) pontos vai receber a variavél pontos declarada como argumento


    def cadastro_jogador(self, nome, categoria): #define a função chamada cadastro_jogador com as variaveis nome e categoria como argumento e self como referência da instãncia(objeto)
        self.usuarios[nome] = categoria #define que a referência de instância(objeto) usuarios adicione ao dicionário a variavél nome que vai receber a variavél categoria
        print(f"Jogador {nome} cadastrado na categoria seguinte {categoria}") #imprimi no terminal o nome do jogador e em qual categoria ele está


    def lista_jogadores(self): #define a função chamada lista_jogadores com self como referência de instância(objeto)
        if not self.usuarios: #indica uma condição onde se não haver nenhum jogador o código abaixo será executado:
            print("Nenhum usuário cadastrado.") #imprimi no terminal que não tem nenhum jogador cadastrado
            return #retorna a função lista_jogadores
        for self.nome in self.usuarios.items(): #cria um loop que vai rodar dentro do dicionário usuarios
            print(f"Nome: {self.nome}, Categoria: {self.categoria}") #imprimi o nome e acategoria de cada jogador
            
def menu(): #define a função chamada menu
    cadastros = cadastro() #cria a variavél cadastros que recebe a classe cadastro
    
    while True: #cria um loop com a uma condição "verdade"
        print("\n Menu:") #impri no terminal "Menu:"
        print("1- Cadastrar jogador") #imprimi no terminal "1- Cadastrar jogador"
        print("2- Listar jogadores") #imprimi no terminal "2- Listar jogadores"
        print("3- Iniciar as rodadas") #imprimi no terminal "3- Iniciar as rodadas"
        print("4- Adicionar pontos aos jogadores") #imprimi no terminal "4- Adicionar pontos os jogadores"
        print("5- Sair") #imprimi o terminal "5- Sair" 
        
        esco = input("Escolha uma das opções (1, 2, 3, 4 ou 5): ") #cria uma variavél esco que recebe um input
        
        if esco == "1": #define uma condição onde se a variavél esco for igual a 1 o código abaixo será executado
            nome = input("Digite seu nome: ") #adiciona um input a variavél nome decarada anteriormente
            cadastros.categoria = input(f"Em que categoria {nome} vai jogar (sub12, sub14, sub16, sub18 ou aberto: ") #adiciona um input a variavél categoria
            
            if cadastros.categoria == "sub12": #se a variavél categoria for igual a "sub12" o código abaixo será executado
                sub12 = dict(nome = "sub12") #cria o dicionário sub12 e adiciona a  a variavél nome de cada jogador e a categoria "sub12" como valor
            elif cadastros.categoria == "sub14": #se a variavél categoria for igual a "sub14" o código abaixo será executado
                sub14 = dict(nome = "sub14") #cria o dicionário sub14 e adiciona a  a variavél nome de cada jogador e a categoria "sub14" como valor
            elif cadastros.categoria == "sub16": #se a variavél categoria for igual a "sub16" o código abaixo será executado
                sub16 = dict(nome = "sub16") #cria o dicionário sub16 e adiciona a  a variavél nome de cada jogador e a categoria "sub16" como valor
            elif cadastros.categoria == "sub18": #se a variavél categoria for igual a "sub18" o código abaixo será executado
                sub18 = dict(nome = "sub18") #cria o dicionário sub18 e adiciona a  a variavél nome de cada jogador e a categoria "sub18" como valor
            elif cadastros.categoria == "aberto": #se a variavél categoria for igual a "aberto" o código abaixo será executado
                aberto = dict(nome = "aberto") #cria o dicionário aberto e adiciona a  a variavél nome de cada jogador e a categoria "aberto" como valor
            else: #caso as condicionais assima sejam falsas o código abaixo será executado
                print("Você não respondeu corretamente, responda novamente") #imprimi na tela "Você não respondeu corretamente, responda novamente"
        elif esco == "2": #define uma condição onde se a variavél esco for igual a 2 o código abaixo será executado
            cadastros.lista_jogadores() #chama a função lista_jgadores 
        elif esco == "3": #define uma condição onde se a variavél esco for igual a 3 o código abaixo será executado
            sorteios(sub12) #chama a função sorteios com o argumento sub12
            sorteios(sub14) #chama a função sorteios com o argumento sub14
            sorteios(sub16) #chama a função sorteios com o argumento sub16
            sorteios(sub18) #chama a função sorteios com o argumento sub18
            sorteios(aberto) #chama a função sorteios com o argumento aberto
        elif esco == "4": #define uma condição onde se a variavél esco for igual a 4 o código abaixo será executado
            jogador = input("Digite o nome do jogador em que você deseja adicionar uma pontuação: ") #cria a variavél jogador que recebe um input
            pont = float(input("Qual a pontuaçaõ a ser adicionada: ")) #cria a variavél pont que recebe um input de um número quebrado
            ponto = dict(jogador = pont) # cria o dicionário ponto que recebe a variavél jogador com o valor da variavél pont
            
            print(ponto) #imprimi no terminal o dicionário ponto
        elif esco == "5": #define uma condição onde se a variavél esco for igual a 5 o código abaixo será executado
            print("Saindo...") #imprimi no terminal "Saindo..."
            break #quebra o código (ele para o programa)
        else: #caso as condicionais assima sejam falsas o código abaixo será executado
            print("Resposta incorreta.") #imprimi no terminal "Resposta incorreta."


if __name__ == "_main_": #| permiti ou impede que partes do código sejam 
    menu()               #| executadas antes de importar os módulos
    