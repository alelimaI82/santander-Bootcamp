class Estudantes:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno_1 = Estudantes("Alexandre", 54321)
aluno_2 = Estudantes("Guilherme", 65432)

print(aluno_1)
print(aluno_2)
