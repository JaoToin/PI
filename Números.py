import sys


def mostrar(qtd, singular, plural):
    if qtd == 1:
        print(f"1 {singular}")
    else:
        print(f"{qtd} {plural}")


def main():
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    for token in sys.stdin.read().split():
        n = int(token)

        # O valor 0 encerra a leitura
        if n == 0:
            break

        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

        if n > 0:
            positivos += 1
        else:
            negativos += 1

    mostrar(pares, "valor par", "valores pares")
    mostrar(impares, "valor impar", "valores impares")
    mostrar(positivos, "valor positivo", "valores positivos")
    mostrar(negativos, "valor negativo", "valores negativos")


if __name__ == "__main__":
    main()
