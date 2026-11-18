def main():
  # 1. Lê se é "acima" ou "abaixo"
  posicao = input().strip()

  # 2. Lê o valor do limiar
  limiar = int(input().strip())

  # 3. Lê a ordem da matriz (N)
  n = int(input().strip())

  # 4. Lê os elementos da matriz
  matriz = []
  for _ in range(n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

  # 5. Calcula a soma conforme a regra
  soma = 0
  for i in range(n):
    for j in range(n):
      if posicao == "acima" and j > i:
        soma += matriz[i][j]
      elif posicao == "abaixo" and i > j:
        soma += matriz[i][j]

  # 6. Verifica se a soma é maior que o limiar e imprime True ou False
  if soma > limiar:
    print("True")
  else:
    print("False")


if __name__ == "__main__":
  main()