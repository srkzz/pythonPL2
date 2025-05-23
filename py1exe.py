import math

def analise_frase():
    frase = input("Insere uma frase: ")
    palavra = input("Insere uma palavra para verificar se existe na frase: ")
    print("Palavra existe na frase?", palavra in frase)
    frase_substituida = frase.replace(" ", "*")
    print("Frase com espaços substituídos por '*':", frase_substituida)
    print("Frase começa por 'Olá' ou termina com '!':", frase.startswith("Olá") or frase.endswith("!"))

def indexacao():
    frase = "python é incrível!"
    print("Primeira letra:", frase[0])
    print("Última letra:", frase[-1])
    print("As 6 primeiras letras:", frase[:6])
    print("As últimas 4 letras:", frase[-4:])

def jogo_adivinhacao():
    palavra_correta = "python"
    tentativa = input("Adivinha a palavra secreta: ")
    if tentativa.lower() == palavra_correta:
        print("Correto!")
    else:
        print("Errado, a palavra correta era:", palavra_correta)

def validacao_entrada():
    nome = input("Insere o teu nome: ")
    if nome.isalpha():
        print("Nome válido (só letras). Em maiúsculas:", nome.upper())
    else:
        print("Nome inválido (tem caracteres que não são letras).")

def manipulacao_texto():
    frase = input("Insere uma frase: ")
    print("Número de vogais:", sum(frase.lower().count(v) for v in "aeiou"))
    print("Frase invertida:", frase[::-1])
    palavras = frase.split()
    print("Palavras separadas:", palavras)
    print("Frase junta com '-':", "-".join(palavras))

def f_strings():
    nome = input("Insere o teu nome: ")
    idade = int(input("Insere a tua idade: "))
    print(f"O {nome} tem {idade} anos.")
    raio = float(input("Insere o raio de um círculo: "))
    area = math.pi * raio**2
    print(f"A área do círculo é: {area:.2f}")

def estatisticas_texto():
    frase = input("Insere uma frase: ")
    print("Número total de caracteres:", len(frase))
    print("Frase em maiúsculas:", frase.upper())
    print("Frase com a primeira letra em maiúscula:", frase.capitalize())
    print("A frase contém apenas letras?", frase.isalpha())
    print("A frase contém apenas palavras (split):", frase.split())