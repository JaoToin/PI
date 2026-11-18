def buscar_nota(cpfs, notas, consulta):
  # Como a lista de CPFs está ordenada, podemos usar busca binária (ou a busca do dicionário)
  # Para ser bem simples e direto, podemos criar um dicionário previamente ou usar bisect.
  # Vamos usar a busca binária clássica implementada manualmente:
  inicio = 0
  fim = len(cpfs) - 1

  while inicio <= fim:
    meio = (inicio + fim) // 2
    if cpfs[meio] == consulta:
      return notas[meio]
    elif cpfs[meio] < consulta:
      inicio = meio + 1
    else:
      fim = meio - 1

  return "NAO SE APRESENTOU"


def main():
  # 1. Lê o número de inscritos
  n = int(input())

  # 2. Lê a sequência de CPFs (já ordenados)
  cpfs = []
  for _ in range(n):
    cpfs.append(int(input()))

  # 3. Lê a sequência de notas correspondentes
  notas = []
  for _ in range(n):
    notas.append(int(input()))

  # 4. Lê o número de consultas (casos de teste)
  m = int(input())

  # 5. Processa cada consulta de CPF
  for _ in range(m):
    cpf_consulta = int(input())
    resultado = buscar_nota(cpfs, notas, cpf_consulta)
    print(resultado)


if __name__ == "__main__":
  main()