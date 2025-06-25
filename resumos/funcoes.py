def exibir_mensagem():
    print("Olá Mundo!!!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Alexandre"):
    print(f"Seja bem vindo {nome}!")

# Ctrol + K - Ctrol + C e depois K e U


# exibir_mensagem()
# exibir_mensagem_2(nome="Guilherme")
# exibir_mensagem_3()
# exibir_mensagem_3(nome="Chappie")
# ____________________________________________________________________________________________________________


def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


# print(calcular_total([10, 20, 30]))
# print(retorna_antecessor_e_sucessor(10))
# ____________________________________________________________________________________________________________


def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# salvar_carro(marca="Ford", modelo="Fusion", ano=2000, placa="ABC-5678")
# salvar_carro(**{"marca": "Ford", "modelo": "Fiesta",
#              "ano": 2001, "placa": "CBA-1234"})
# ____________________________________________________________________________________________________________

#Aqui em *args os parâmetros podem ser passados tanto por nome quanto por posição.
#Já em **kwargs, somente por nome.

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n" .join(args)
    meta_dados = "\n" .join(
        [f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


# exibir_poema("Segunda-feira, 24 de junho de 2025", "Zen of Python", "Beautiful is better than ugly.",
#              autor="Tim Peters", ano=1999)
# ____________________________________________________________________________________________________________

# Antes da barra é por posição (Positional Only = /) e posterior a barra, tanto faz (nome ou posição).

def criar_carro(modelo, ano, placa, /, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)


# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat",
#             motor="1.0", combustível="Gasolina")
# # ou pode ser assim:
# criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")
# ____________________________________________________________________________________________________________

# Agora (keyword Only = *) é somente aceito passar parâmetro por nome.

def criar_carro(*, modelo, ano, placa, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)


# criar_carro(modelo="Fiesta", ano=2008, placa="CBA-4321",
#             marca="Ford", motor="1.6", combustível="Alcool")
# ____________________________________________________________________________________________________________

#Objetos de primeira  classe

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao (a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

# exibir_resultado(10, 10, somar)
# ____________________________________________________________________________________________________________

# Escopo de variável Local e Global

salario = 20000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(5000)
print(salario)