# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    posicao_espaco = linha.rfind(" ")
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    carrinho.append((item, preco))
    total += preco

# Exibe os itens no formato esperado
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

# Exibe o total no formato esperado
print(f"Total: R${total:.2f}")
