# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# Verifica se o cupom é válido e aplica o desconto
if cupom in descontos:
    desconto = descontos[cupom]
    preco_final = preco * (1 - desconto)
    print(f"{preco_final:.2f}")
else:
    # Caso o cupom seja inválido, nenhum desconto é aplicado
    print(f"{preco:.2f}")
