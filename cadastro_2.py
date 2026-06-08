usuarios = []

while True:

    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Atualizar")
    print("5 - Excluir")
    print("6 - Login")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    # CREATE
    if opcao == "1":

        try:
            nome_completo = input("Digite seu nome completo: ").strip()

            if not nome_completo:
                raise ValueError("O nome não pode ficar vazio.")

            if not nome_completo.replace(" ", "").isalpha():
                raise ValueError("O nome deve conter apenas letras.")

            partes_nome = nome_completo.split()

            if len(partes_nome) < 2:
                raise ValueError("Digite nome e sobrenome.")

            nome = partes_nome[0]
            sobrenome = " ".join(partes_nome[1:])

            email = input("Digite seu e-mail: ").strip().lower()

            if email.count("@") != 1:
                raise ValueError("Digite um e-mail válido.")

            usuario_email, dominio = email.split("@")

            if not usuario_email or "." not in dominio:
                raise ValueError("Digite um e-mail válido.")

            for usuario in usuarios:
                if usuario["email"] == email:
                    raise ValueError("E-mail já cadastrado.")

            senha = input("Digite sua senha: ").strip()
            confirmar_senha = input("Confirme sua senha: ").strip()

            if len(senha) < 6:
                raise ValueError("A senha deve ter pelo menos 6 caracteres.")

            if senha != confirmar_senha:
                raise ValueError("As senhas não coincidem.")

            cadastro = {
                "nome": nome,
                "sobrenome": sobrenome,
                "email": email,
                "senha": senha
            }

            usuarios.append(cadastro)

            print("Cadastro realizado com sucesso!")

        except ValueError as erro:
            print(f"Erro: {erro}")

    # READ
    elif opcao == "2":

        if not usuarios:
            print("Nenhum usuário cadastrado.")

        else:
            print("\n=== USUÁRIOS CADASTRADOS ===")

            for usuario in usuarios:
                print("-" * 30)
                print(f"Nome: {usuario['nome']} {usuario['sobrenome']}")
                print(f"E-mail: {usuario['email']}")

    # BUSCAR
    elif opcao == "3":

        email = input("Digite o e-mail para busca: ").strip().lower()

        encontrado = False

        for usuario in usuarios:
            if usuario["email"] == email:

                print("\nUsuário encontrado!")
                print(f"Nome: {usuario['nome']} {usuario['sobrenome']}")
                print(f"E-mail: {usuario['email']}")

                encontrado = True
                break

        if not encontrado:
            print("Usuário não encontrado.")

    # UPDATE
    elif opcao == "4":

        email = input("Digite o e-mail do usuário: ").strip().lower()

        for usuario in usuarios:

            if usuario["email"] == email:

                novo_nome = input("Novo nome: ").strip()

                if novo_nome:
                    if not novo_nome.isalpha():
                        print("Nome inválido.")
                    else:
                        usuario["nome"] = novo_nome

                novo_sobrenome = input("Novo sobrenome: ").strip()

                if novo_sobrenome:
                    if not novo_sobrenome.replace(" ", "").isalpha():
                        print("Sobrenome inválido.")
                    else:
                        usuario["sobrenome"] = novo_sobrenome

                print("Usuário atualizado com sucesso!")
                break

        else:
            print("Usuário não encontrado.")

    # DELETE
    elif opcao == "5":

        email = input("Digite o e-mail do usuário: ").strip().lower()

        for usuario in usuarios:

            if usuario["email"] == email:

                usuarios.remove(usuario)

                print("Usuário removido com sucesso!")
                break

        else:
            print("Usuário não encontrado.")

    # LOGIN
    elif opcao == "6":

        email = input("Digite seu e-mail: ").strip().lower()
        senha = input("Digite sua senha: ").strip()

        for usuario in usuarios:

            if usuario["email"] == email and usuario["senha"] == senha:

                print(f"\nLogin realizado com sucesso!")
                print(f"Bem-vindo, {usuario['nome']}!")
                break

        else:
            print("E-mail ou senha incorretos.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")