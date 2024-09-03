import random
import uuid

class CadastroEvento:
    def _init_(self, categoria, vitorias):
        self.usuarios = {}
        self.categoria = categoria
        self.vitorias = vitorias

    def gerar_id(self):
        return str(uuid.uuid4())

    def cadastrar_usuario(self, nome):
        usuario_id = self.gerar_id()
        self.usuarios[usuario_id] = nome
        print(f"Usuário {nome} cadastrado com ID: {usuario_id} na categoria: {self.categoria}")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for usuario_id, nome in self.usuarios.items():
            print(f"ID: {usuario_id}, Nome: {nome}, Categoria: {self.categoria}")

def menu():
    cadastro = CadastroEvento()

    while True:
        print("\n Menu:")
        print("1- Cadastrar novo usuário")
        print("2- Listar usuários")
        print("3- Sair")

        escolha = input("Escolha uma opção(número): ")

        if escolha == "1":
            nome = input("Digite o nome do usuário: ")
            cadastro.categoria = input("Digite a categoria em que o usuário jogará: ")
            cadastro.cadastrar_usuario(nome)
        elif escolha == "2":
            cadastro.listar_usuarios()
        elif escolha == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, por favor escolha novamente.")

class Participante:
    def __init__(self, nome, categoria, vitorias):
        self.nome = nome
        self.categoria = categoria
        self.vitorias = vitorias

def cadastrar_participantes():
    participantes = []
    participantes.append(CadastroEvento.listar_usuarios)
    return participantes

def sortear_participantes(participantes):
    categorias = {}

    for participante in participantes:
        key = (participante.categoria, participante.vitorias)
        if key not in categorias:
            categorias[key] = []
        categorias[key].append(participante)

    possiveis_sorteios = [v for v in categorias.values() if len(v) > 1]
    if not possiveis_sorteios:
        print("Não há participantes que atendem os critérios de sorteio.")
        return None

    sorteados = random.choice(possiveis_sorteios)
    return random.sample(sorteados, 2)

def atualizar_vitorias(participante):
    participante.vitorias += 1

def main():
    participantes = cadastrar_participantes()
    
    print("Participantes cadastrados:")
    for p in participantes:
        print(f"{p.nome} - Categoria: {p.categoria}, Vitórias: {p.vitorias}")
    
    sorteados = sortear_participantes(participantes)
    if sorteados:
        print(f"\nParticipantes sorteados para jogar: {sorteados[0].nome} e {sorteados[1].nome}")

        vencedor = random.choice(sorteados)
        atualizar_vitorias(vencedor)
        print(f"\n{vencedor.nome} venceu a partida e agora tem {vencedor.vitorias} vitórias!")

if __name__ == "_main_":
    menu()
    main()