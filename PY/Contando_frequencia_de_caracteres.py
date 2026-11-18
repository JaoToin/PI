def contar_caracteres(texto):
  # Dicionário para armazenar a frequência de cada caractere
  frequencias = {}

  for char in texto:
    if char in frequencias:
      frequencias[char] += 1
    else:
      frequencias[char] = 1

  return frequencias


def main():
  # Lê a linha de texto fornecida na entrada
  texto = input()

  # Obtém o dicionário com as contagens
  frequencias = contar_caracteres(texto)

  # Ordena as chaves (caracteres) em ordem decrescente (reverse=True)
  caracteres_ordenados = sorted(frequencias.keys(), reverse=True)

  # Imprime cada caractere e sua contagem na ordem inversa
  for char in caracteres_ordenados:
    print(f"{char} {frequencias[char]}")


if __name__ == "__main__":
  main()