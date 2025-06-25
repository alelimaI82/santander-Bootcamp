# Entrada do usuário
email = input().strip()

# Função de validação de e-mail


def validar_email(email):
    if "@" not in email or email.count("@") != 1:
        return "E-mail inválido"
    if email.startswith("@") or email.endswith("@"):
        return "E-mail inválido"
    if " " in email:
        return "E-mail inválido"

    parte_local, dominio = email.split("@")
    if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
        return "E-mail inválido"

    return "E-mail válido"


# Saída exata
print(validar_email(email))