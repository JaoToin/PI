import sys

ESQUERDA = {"e", "esq", "esquerda"}
DIREITA = {"d", "dir", "direita"}


def ler_palavras():
    for linha in sys.stdin:
        yield from linha.split()


def main():
    esquerda = 0
    direita = 0
    incorretas = 0

    for indicacao in ler_palavras():
        if indicacao == "*":
            break

        indicacao = indicacao.lower()

        if indicacao in ESQUERDA:
            esquerda += 1
        elif indicacao in DIREITA:
            direita += 1
        else:
            incorretas += 1

    print(f"Esquerda: {esquerda}")
    print(f"Direita: {direita}")
    print(f"Incorretas: {incorretas}")


if __name__ == "__main__":
    main()
