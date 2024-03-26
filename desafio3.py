#Desafio 3

class heroi:
    def __init__(self,nome,idade,tipo):
        self.nome = nome
        self.idade = int(idade)
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'

        print(f"O {self.tipo} {self.nome} atacou usando {ataque}")

h1 = heroi('Joao',15,'mago')
h1.atacar()

