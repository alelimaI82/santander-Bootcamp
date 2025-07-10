# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Listas para cada grupo
urgentes = []
idosos = []
normais = []

# Entrada dos pacientes
for _ in range(n):
    linha = input().strip()
    partes = linha.split(", ")
    if len(partes) != 3:
        print("Entrada inválida. Use o formato: nome, idade, status")
        continue

    nome, idade_str, status = partes

    try:
        idade = int(idade_str)
    except ValueError:
        print(f"Idade inválida para o paciente {nome}. Ignorado.")
        continue

    paciente = (nome, idade, status.lower())

    if paciente[2] == "urgente":
        urgentes.append(paciente)
    elif idade >= 60:
        idosos.append(paciente)
    else:
        normais.append(paciente)

# TODO: Ordene por prioridade: urgente > idosos > demais:

# urgente -> prioridade 0
# Ordena urgentes por maior idade
urgentes.sort(key=lambda p: -p[1])

# Junta tudo na ordem correta
ordem_final = urgentes + idosos + normais

# Imprime nomes na ordem de atendimento
nomes = [p[0] for p in ordem_final]
print(f"Ordem de Atendimento: {', '.join(nomes)}")


# # idoso (>60) -> prioridade 1
# # demais -> prioridade 2
# def prioridade(paciente):
#     nome, idade, status = paciente
#     if status.lower() == "urgente":
#         return 0
#     elif idade >= 60:
#         return 1
#     else:
#         return 2

# # Ordenar mantendo ordem de chegada entre os de mesma prioridade
# pacientes.sort(key=prioridade)

# # TODO: Exiba a ordem de atendimento com título e vírgulas:

# nomes = [paciente[0] for paciente in pacientes]
# print(f"Ordem de Atendimento: {', '.join(nomes)}")