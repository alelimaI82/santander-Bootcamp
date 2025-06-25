# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:

# Loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()

    # Divide por vírgula e remove espaços extras
    if "," in linha:
        nome, tema = map(str.strip, linha.split(",", 1))
    else:
        # Caso não tenha vírgula, ignora a linha ou mostra erro
        continue

    # Adiciona o participante ao tema correspondente
    if tema in eventos:
        eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
