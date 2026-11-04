import sys


def main():
    texto = sys.stdin.readline().rstrip("\n")

    # Ignora espaços e diferença entre maiúsculas/minúsculas
    limpo = texto.replace(" ", "").lower()

    if limpo == limpo[::-1]:
        print("SIM")
    else:
        print("NAO")


if __name__ == "__main__":
    main()
