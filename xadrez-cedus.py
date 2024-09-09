#-cadastrar os jogadores e separalos por categorias
#-sortear de dois em dois jogadores para iniciar uma rodada
#-separar quem ganhou de quem perdeu e fazer um sorteio com base nesta nova lista

class cadastro:
    def __init__(self, nome, categoria, pontos):
        self.usuarios = {}
        self.nome = nome
        self.categoria = categoria
        self.pontos = pontos
    
    def lista_jogadores(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for self.nome in self.usuarios.items():
            print(f"Nome: {self.nome}, Categoria: {self.categoria}")