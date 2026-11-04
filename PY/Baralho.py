import re
import sys


def main():
    for linha in sys.stdin:
        # Extrai todos os números inteiros da linha
        numeros = [int(n) for n in re.findall(r"\d+", linha)]

        # Linha sem números é ignorada
        if not numeros:
            continue

        # Linha começando com 0 encerra o programa
        if numeros[0] == 0:
            return

        pares = list(zip(numeros, numeros[1:]))
        crescente = all(a <= b for a, b in pares)
        decrescente = all(a >= b for a, b in pares)

        if crescente:
            print("CRESCENTE")
        elif decrescente:
            print("DECRESCENTE")
        else:
            print("DESORDENADA")


if __name__ == "__main__":
    main()
