class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe... ")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")

    def latir(self):
        print("Au Au Au")
    
    def dormir(self):
        self.acordado = False
        print("Zzzzzzzz")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Neo", "Branco e caramelo")
c.latir()

print("Olá Mundo")
del c
print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")

# criar_cachorro()