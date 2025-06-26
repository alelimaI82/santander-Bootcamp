import textwrap

def menu():
    menu = """\n
    =================== MENU ===================
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc] \tNova Conta
    [lc] \tListar Contas
    [nu] \tNovo Usuário
    [q] Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \t R$ {valor: .2f}\n"
        print("\n === Depósito realizado com sucesso! ===")
    else:
        print("\n @@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saques, lim_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques >= lim_saques
    if excedeu_saldo:
        print ("\n @@@ Operação falhou! Você não tem saldo suficiente. @@@ ")
    elif excedeu_limite:    
        print ("\n @@@ Operação falhou! O valor do saque excedeu o limite. @@@")
    elif excedeu_saques:
        print ("\n @@@ Operação falhou! O número máximo de saques excedeu o limite. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\t R$ {valor:.2f}\n"
        num_saques += 1
        print("\n === Saque realizado com sucesso! === ")
    else:
        print("\n @@@ Operação falhou! O valor informado é inválido. @@@ ")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("\n==================== Extrato =====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================================")

def criar_usuario(usuarios):
    CPF = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(CPF, usuarios)

    if usuario:
        print("\n @@@ Já existe usuário com esse CPF! @@@ ")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o edereço completo (logradouro, número, bairro, cidade e sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "CPF": CPF, "endereço": endereco})

    print("\n === Usuário criado com sucesso! === ")

def filtrar_usuario(CPF, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == CPF]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    CPF = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(CPF, usuarios)
    if usuario:
        print("\n === Conta criada com sucesso! === ")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
    print("\n @@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@ ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            CC: \t\t{conta['num_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                num_saques = num_saques,
                lim_saques = LIMITES_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")

main()

    