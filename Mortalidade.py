import sys


def main():
    dados = sys.stdin.read().split()
    n = int(dados[0])

    if n <= 0:
        print("Informe um numero positivo")
        return

    femininos = 0
    masculinos = 0
    ate_24_meses = 0

    for i in range(n):
        sexo = dados[1 + 2 * i].upper()
        meses = float(dados[2 + 2 * i])

        if sexo == "F":
            femininos += 1
        elif sexo == "M":
            masculinos += 1

        if meses <= 24:
            ate_24_meses += 1

    print(f"{femininos / n * 100:.1f}%")
    print(f"{masculinos / n * 100:.1f}%")
    print(f"{ate_24_meses / n * 100:.1f}%")


if __name__ == "__main__":
    main()
