import sys

# Teclado de telefone: ABC=2, DEF=3, GHI=4, JKL=5, MNO=6, PQRS=7, TUV=8, WXY=9
# (igual ao original em C, a letra Z não é convertida)
TABELA = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXY", "2223334445556667777888999")


def main():
    telefone = sys.stdin.readline().rstrip("\n")
    print(telefone.translate(TABELA))


if __name__ == "__main__":
    main()
