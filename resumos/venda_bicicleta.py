class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Buzzzzzzz")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def pedalar(self):
        print("Vrummmm")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha...")

        if nro_marcha > self.trocar_marcha:
            print("Marcha trocada!")
        else:
            print("Não foi possível trocar de marcha.")

    def get_cor(self):
        return self.cor

    # def __str__(self):
    #     return f"Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor} reais."
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
# b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
# b1.buzinar()
# b1.parar()
# b1.pedalar()

# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2018, 450)
# Bicicleta.buzinar(b2)
# print(b2.cor, b2.modelo, b2.ano, b2.valor)

# print(b2.get_cor())
print(b2)
