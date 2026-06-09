from calculando_soh import calcular_soh
import cadastro_concluido as cadastro

def menu_principal():

            while True:

                print("\n=== MENU PRINCIPAL ===\n== EcoVolt Analytics ==\n")
                print("1. Calcular Saúde da Bateria (SoH)")
                print("2. Gerenciar Conta")
                print("0. Sair")

                escolha = input("Escolha uma opção: ").strip()

                if escolha == "1":
                    calcular_soh()
                elif escolha == "2":
                    cadastro.menu_conta()  # Chama o menu de cadastro para gerenciar a conta
                elif escolha == "0":
                    print("Obrigado por usar o EcoVolt Analytics! Até a próxima!")
                    exit()
                else:
                    print("Opção inválida. Por favor, tente novamente.")