from py1exe import (
    analise_frase,
    estatisticas_texto,
    f_strings,
    manipulacao_texto,
    validacao_entrada,
    jogo_adivinhacao,
    indexacao
)

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Análise de Frase")
        print("2. Estatísticas de Texto")
        print("3. F-Strings")
        print("4. Manipulação de Texto")
        print("5. Validação de Entrada")
        print("6. Jogo de Adivinhação")
        print("7. Indexação")
        print("0. Sair")

        escolha = input("Escolhe uma opção: ")

        if escolha == "1":
            analise_frase()
        elif escolha == "2":
            estatisticas_texto()
        elif escolha == "3":
            f_strings()
        elif escolha == "4":
            manipulacao_texto()
        elif escolha == "5":
            validacao_entrada()
        elif escolha == "6":
            jogo_adivinhacao()
        elif escolha == "7":
            indexacao()
        elif escolha == "0":
            print("A sair do programa...")
            break
        else:
            print("Opção inválida. Tenta novamente.")

menu()