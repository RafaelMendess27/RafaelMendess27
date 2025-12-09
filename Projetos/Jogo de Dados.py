"""
Jogo de Dados - Competição contra o Computador
Autor: [Rafel]
Data: [09/12/2025]
"""

import random
from time import sleep


def jogo_dados_simples():
    """
    Jogo de dados simples: jogador vs computador
    """

    print("🎲 JOGO DE DADOS SIMPLES 🎲")
    print("-" * 30)

    # Jogador lança o dado
    input("Pressione ENTER para lançar seu dado...")
    dado_jogador = random.randint(1, 6)
    print("Dado Rolando...")
    sleep(1)
    print(f"Você tirou: {dado_jogador}")

    # Computador lança o dado
    print("\nAgora é a vez do computador...")
    dado_computador = random.randint(1, 6)
    print("Dado Rolando...")
    sleep(1)
    print(f"Computador tirou: {dado_computador}")

    print("\n" + "=" * 30)

    # Verifica quem ganhou
    if dado_jogador > dado_computador:
        print("🎉 VOCÊ GANHOU! 🎉")
    elif dado_computador > dado_jogador:
        print("💻 COMPUTADOR GANHOU!")
    else:
        print("⚡ EMPATE!")

    print("=" * 30)


# Executa o jogo
if __name__ == "__main__":
    jogo_dados_simples()

    # Pergunta se quer jogar novamente
    while True:
        jogar_novamente = input("\nJogar novamente? (s/n): ").lower()
        if jogar_novamente == 's':
            jogo_dados_simples()
        elif jogar_novamente == 'n':
            print("\nObrigado por jogar! 👋")
            break
        else:
            print("Digite 's' para SIM ou 'n' para NÃO")