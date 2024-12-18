#Neste arquivo você verá um resumo sobre o que são classes e como elas funcionam de uma maneira bem simples.
#OBS.: se você não souber o básico de python este arquivo pode ser muito complexo e ou desnecessári para seus objetivo. Mas você pode dar uma conferida em outras aulas que se encontram nesta mesma pasta.



#Uma classe é como um construtor de objeto ou um "projeto" para criar objetos.
#class nome-da-classe: 
#   | como vai ser esse objeto

#Ex.: 

class exemplo:
    x = 5

p1 = exemplo
print(p1.x)

#Todas as classes têm uma função chamada __init__(), que é sempre executada quando A aula está sendo iniciada.
#Use a função __init__() para atribuir valores a propriedades de objetos ou outros operações que são necessárias para fazer quando o objeto está sendo criado:

class Person:
  def __init__(pesoa, nome, idade):
    pesoa.nome = nome
    pesoa.idade = idade

p1 = Person("John", 36)

print(p1.nome)
print(p1.idade)

#Adicionando o codigo abaixo ele retorna o objeto com uma string:
#def __str__(self):
#   | return f"{self.name}  {self.age}"

class Personagem:
    def __init__(pesoa2, nome2, idade2):
        pesoa2.nome2 = nome2
        pesoa2.idade2 = idade2

    def __str__(pesoa2):
        return f"{pesoa2.nome2}({pesoa2.idade2})"
    
p2 = Personagem("John", 36)

print(p2)

#Você pode excluir objetos usando a palavra-chave: del

#Ex.:

del p1

#Uma classe não podem estar vazias, mas se você, por algum motivo, tem uma definição sem conteúdo, coloque a instrução pass para evitar um erro.

#Ex.:

class vazia:
   pass

# Vídeos sobre classes:
'''
1-Vídeo sobre classes(básico): 
https://youtu.be/97A_Cyyh-eU?si=E1ndmCnu5uXWAQ3U

2-Vídeo sobre classes(básico, self e init):
https://youtu.be/gomDSZaay3E?si=jDtW_IPs5_UDhFcO

3-Vídeo sobre orientação a objeto:
https://youtu.be/tS9LETaEomI?si=OpP9PIyIP_smhWw6
'''
