#garador de senha de cartão
import secrets
#atualização do progrma 
print("="*20,"🗃️","GERADOR DE CARTAO","="*20) 
def gerar_senha_memoravel(palavras=4, separador="."):
    """
    Gera uma senha memorável usando palavras aleatórias
    """
    # Lista de palavras comuns (pode ser expandida)
    lista_palavras = [
        "casa", "tempo", "pessoa", "ano", "dia", "coisa", "homem", "mulher",
        "agua", "trabalho", "problema", "grupo", "informacao", "numero",
        "filho", "mundo", "cidade", "ponto", "estado", "rua", "livro",
        "historia", "poder", "dia", "pai", "mae", "filha", "noite", "verdade"
    ]

    # Seleciona palavras aleatoriamente
    senha_palavras = [secrets.choice(lista_palavras) for _ in range(palavras)]

    # Adiciona um número aleatório no final
    senha_palavras.append(str(secrets.randbelow(100)))

    # Junta as palavras com separador
    return separador.join(senha_palavras)


# Uso
senha_memoravel = gerar_senha_memoravel()
print(f" Segue a sua nova senha : {senha_memoravel}")

