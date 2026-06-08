try:
    nome_completo = input("Digite seu nome completo: ").strip()

    if not nome_completo.replace(" ", "").isalpha():
        raise ValueError("O nome deve conter apenas letras.")

    partes_nome = nome_completo.split()

    if len(partes_nome) < 2:
        raise ValueError("Digite nome e sobrenome.")

    nome = partes_nome[0]
    sobrenome = " ".join(partes_nome[1:])

    email = input("Digite seu e-mail: ").strip().lower()

    if len(email) < 6:
        raise ValueError("O e-mail é muito curto.")

    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Digite um e-mail válido.")

    senha = input("Digite sua senha: ").strip()
    confirmar_senha = input("Confirme sua senha: ").strip()

    if senha != confirmar_senha:
        raise ValueError("As senhas não coincidem.")

    if len(senha) < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres.")

    if not any(c.isupper() for c in senha):
        raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")

    if not any(c.islower() for c in senha):
        raise ValueError("A senha deve conter pelo menos uma letra minúscula.")

    if not any(c.isdigit() for c in senha):
        raise ValueError("A senha deve conter pelo menos um número.")

    caracteres_especiais = "!@#$%&*"

    if not any(c in caracteres_especiais for c in senha):
        raise ValueError(
            f"A senha deve conter pelo menos um caractere especial ({caracteres_especiais})."
        )

    cadastro = {
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "senha": senha
    }

    print("\nCadastro realizado com sucesso!")

    print("=" * 50)
    print("RELATÓRIO DO USUÁRIO")
    print("=" * 50)

    for chave, valor in cadastro.items():
        print(f"{chave.capitalize()}: {valor}")

except ValueError as erro:
    print(f"Erro: {erro}")