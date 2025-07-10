class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # return f"Caminhão: {self.cor} {self.placa} {self.numero_rodas} eixos."

class Motocicleta(Veiculo):
    def __str__(self):
        return f"Motocicleta: {self.cor} {self.placa} {self.numero_rodas}"
class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
        print(f"{"Sim," if self.carregado else "Não"} estou carregado.") 


# moto = Motocicleta("preta", "ABC-1234", 2)
# print(moto)
# print(moto.ligar_motor())

# carro = Carro("Branco", "XYZ-1234", 4)
# carro.ligar_motor()

caminhao = Caminhao("Azul", "CDB-4567", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(caminhao)
