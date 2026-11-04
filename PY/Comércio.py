import sys


def main():
    dados = sys.stdin.read().split()
    n = int(dados[0])

    if n == 0:
        return

    produtos = []
    lucros = []

    for i in range(n):
        produtos.append(dados[1 + 2 * i])
        lucros.append(float(dados[2 + 2 * i]))

    media = sum(lucros) / n
    limite = media / 2

    for produto, lucro in zip(produtos, lucros):
        if lucro < limite:
            print(produto)


if __name__ == "__main__":
    main()
