# Função para calcular a nota comparando as respostas com o gabarito
def calcular_nota(gabarito, respostas):
  nota = 0
  for i in range(10):
    if respostas[i] == gabarito[i]:
      nota += 1
  return nota


def main():
  # 1. Lê o gabarito (converte a linha em uma lista de inteiros)
  linha_gabarito = input().split()
  if not linha_gabarito or linha_gabarito[0] == "*":
    return
  gabarito = [int(x) for x in linha_gabarito]

  participantes = {}  # Dicionário para armazenar {nome: nota}

  # 2. Leitura dos dados dos participantes até encontrar '*'
  while True:
    entrada = input().split()
    if entrada[0] == "*":
      break

    # O nome pode ser o primeiro elemento (ou combinado se houver espaços, mas vamos assumir nome simples por padrão)
    nome = entrada[0]
    respostas = [int(x) for x in entrada[1:]]

    # Calcula a nota usando a função e guarda no dicionário
    nota = calcular_nota(gabarito, respostas)
    participantes[nome] = nota

  if not participantes:
    return

  # 3. Saída A: Lista em ordem alfabética
  nomes_ordenados = sorted(participantes.keys())
  print("\n--- Notas dos Participantes ---")
  for nome in nomes_ordenados:
    print(f"{nome}: {participantes[nome]}")

  # 4. Saída B: Maior e menor pontuação
  maior_nota = max(participantes.values())
  menor_nota = min(participantes.values())

  maiores = [n for n, nota in participantes.items() if nota == maior_nota]
  menores = [n for n, nota in participantes.items() if nota == menor_nota]

  print(f"\nMaior pontuação ({maior_nota}): {', '.join(maiores)}")
  print(f"Menor pontuação ({menor_nota}): {', '.join(menores)}")

  # 5. Saída C: Percentual com mais da metade certa (> 5 questões)
  total_alunos = len(participantes)
  certas_mais_da_metade = sum(
      1 for nota in participantes.values() if nota > 5
  )
  percentual = (certas_mais_da_metade / total_alunos) * 100

  print(
      f"\nPercentual com mais da metade certa: {percentual:.1f}%"
  )


# Executa o programa
if __name__ == "__main__":
  main()



  # -----------------------------------------------------------------------------


  def calcular_nota(gabarito, respostas):
  nota = 0
  for i in range(10):
    if respostas[i] == gabarito[i]:
      nota1 += 1
  return nota1


def main():
  gabarito = [int(x) for x in input().split()]
  participantes = {}

  while True:
    entrada = input().split()
    if entrada[0] == "*":
      break

    nome = entrada[0]
    respostas = [int(x) for x in entrada[1:]]
    participantes[nome] = calcular_nota(gabarito, respostas)

  nomes_ordenados = sorted(participantes.keys())

  # a) Lista em ordem alfabética
  print("Participante Nota")
  for nome in nomes_ordenados:
    print(f"{nome} {participantes[nome]}")

  # b) Melhor e pior pontuação
  maior_nota = max(participantes.values())
  menor_nota = min(participantes.values())

  print(f"Melhor pontuacao: {maior_nota}")
  for nome in nomes_ordenados:
    if participantes[nome] == maior_nota:
      print(nome)

  print(f"Pior pontuacao: {menor_nota}")
  for nome in nomes_ordenados:
    if participantes[nome] == menor_nota:
      print(nome)

  # c) Percentual com mais da metade certa (> 5 questões)
  acima_da_media = sum(1 for nota in participantes.values() if nota > 5)
  percentual = (acima_da_media / len(participantes)) * 100
  print(
      f"Percentual de participantes com mais da metade de questoes certas:"
      f" {percentual:.1f}%"
  )


if __name__ == "__main__":
  main()