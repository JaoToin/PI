def main():
    infimo = float(input())

    soma = 0.0
    sinal = 1
    denominador = 1

    while True:
        termo = 1 / denominador
        soma += sinal * termo

        # Para quando o valor absoluto do último termo é <= ao valor ínfimo
        if abs(termo) <= infimo:
            break

        sinal = -sinal
        denominador += 2

    pi = 4 * soma
    print(f"{pi:.12f}")


if __name__ == "__main__":
    main()
