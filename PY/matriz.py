def multiplicar_matrizes(n, m, o, matriz_a, matriz_b):
  # Cria a matriz C com dimensões N x O preenchida com zeros
  matriz_c = [[0 for _ in range(o)] for _ in range(n)]

  # Realiza a multiplicação padrão de matrizes
  for i in range(n):
    for j in range(o):
      for k in range(m):
        matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]

  return matriz_c


def main():
  # 1. Lê as dimensões N, M e O
  linha_dimensoes = input().split()
  if not linha_dimensoes:
    return
  n = int(linha_dimensoes[0])
  m = int(linha_dimensoes[1])
  o = int(linha_dimensoes[2])

  # 2. Lê a matriz A (N linhas, M colunas)
  matriz_a = []
  for _ in range(n):
    linha = [int(x) for x in input().split()]
    matriz_a.append(linha)

  # 3. Lê a matriz B (M linhas, O colunas)
  matriz_b = []
  for _ in range(m):
    linha = [int(x) for x in input().split()]
    matriz_b.append(linha)

  # 4. Calcula a matriz resultante C
  matriz_c = multiplicar_matrizes(n, m, o, matriz_a, matriz_b)

  # 5. Imprime a matriz C no formato exigido (elementos da linha separados por espaço)
  for linha in matriz_c:
    print(*(linha))


if __name__ == "__main__":
  main()