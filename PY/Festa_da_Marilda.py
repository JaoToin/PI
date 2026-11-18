def inserir_ordenado(lista, nome):
  """Insere um novo nome mantendo a lista ordenada

  sem usar funções de ordenação de bibliotecas.
  """
  i = 0
  while i < len(lista) and lista[i] < nome:
    i += 1
  lista.insert(i, nome)


def main():
  # 1. Leitura da lista inicial de convidados
  convidados = []
  while True:
    nome = input().strip()
    if nome == "FIM":
      break
    convidados.append(nome)

  # Ordena a lista inicial (ÚNICA chamada permitida de método de ordenação)
  convidados.sort()

  # Imprime a lista inicial
  for nome in convidados:
    print(nome)

  # 2. Leitura dos grupos adicionais de convidados
  while True:
    linha = input().strip()
    if not linha:
      continue
    n = int(linha)

    if n == 0:
      break

    # Imprime o separador antes de mostrar o grupo atualizado
    print("-" * 50)

    # Lê e insere cada novo convidado ordenadamente
    for _ in range(n):
      novo_nome = input().strip()
      inserir_ordenado(convidados, novo_nome)

    # Imprime a lista atualizada
    for nome in convidados:
      print(nome)


if __name__ == "__main__":
  main()