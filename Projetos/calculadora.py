# Calculadora com Menu Interativo
import os


def mostrar_menu():
    """
    Mostra o menu de opções da calculadora
    """
    print("\n" + "=" * 40)
    print("🧮 CALCULADORA PYTHON 🧮")
    print("=" * 40)
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potência (x^y)")
    print("6. Raiz quadrada (√)")
    print("7. Limpar tela")
    print("8. Sair")
    print("=" * 40)


def calculadora_menu():
    """
    Calculadora completa com menu interativo
    """

    while True:  # Loop infinito até o usuário sair
        mostrar_menu()

        try:
            opcao = input("Escolha uma opção (1-8): ")

            if opcao == "1":  # Adição
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 + num2
                print(f"\n✅ Resultado: {num1} + {num2} = {resultado}")

            elif opcao == "2":  # Subtração
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 - num2
                print(f"\n✅ Resultado: {num1} - {num2} = {resultado}")

            elif opcao == "3":  # Multiplicação
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 * num2
                print(f"\n✅ Resultado: {num1} × {num2} = {resultado}")

            elif opcao == "4":  # Divisão
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"\n✅ Resultado: {num1} ÷ {num2} = {resultado}")
                else:
                    print("\n❌ Erro: Não é possível dividir por zero!")

            elif opcao == "5":  # Potência
                base = float(input("Digite a base: "))
                expoente = float(input("Digite o expoente: "))
                resultado = base ** expoente
                print(f"\n✅ Resultado: {base}^{expoente} = {resultado}")

            elif opcao == "6":  # Raiz quadrada
                numero = float(input("Digite o número: "))
                if numero >= 0:
                    resultado = numero ** 0.5  # √x = x^(1/2)
                    print(f"\n✅ Resultado: √{numero} = {resultado}")
                else:
                    print("\n❌ Erro: Não existe raiz real de número negativo!")

            elif opcao == "7":  # Limpar tela
                os.system('cls' if os.name == 'nt' else 'clear')
                print("🧮 Calculadora Python 🧮")

            elif opcao == "8":  # Sair
                print("\n👋 Obrigado por usar a calculadora! Até logo!")
                break

            else:
                print("\n❌ Opção inválida! Escolha um número de 1 a 8.")

        except ValueError:
            print("\n❌ Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"\n❌ Ocorreu um erro inesperado: {e}")


# Executa a calculadora
if __name__ == "__main__":
    calculadora_menu()