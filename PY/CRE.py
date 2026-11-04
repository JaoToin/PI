import sys

CARGAS_VALIDAS = {33, 50, 67, 83}

# Situações que entram no cálculo do CRE (com aprovação ou não)
ENTRAM_NO_CALCULO = {"A", "R", "RF"}
# As demais situações (DT, AD, DE, AE, DD, DC) são lidas, mas não entram no cálculo


def main():
    dados = sys.stdin.read().split()
    i = 0
    soma_ponderada = 0
    soma_cargas = 0

    while i < len(dados):
        # Semestre fora de 1..10 encerra a leitura
        try:
            semestre = int(dados[i])
        except ValueError:
            break
        i += 1

        if semestre <= 0 or semestre > 10:
            break

        # Precisa haver carga horária, nota e situação
        if i + 2 >= len(dados):
            break

        try:
            carga = int(dados[i])
            nota = int(dados[i + 1])
        except ValueError:
            carga = nota = None
        situacao = dados[i + 2].upper()
        i += 3

        # Disciplina com carga horária ou nota inválida é ignorada
        if carga not in CARGAS_VALIDAS or not 0 <= nota <= 100:
            continue

        if situacao in ENTRAM_NO_CALCULO:
            soma_ponderada += nota * carga
            soma_cargas += carga

    if soma_cargas == 0:
        print("entrada invalida")
    else:
        print(f"{soma_ponderada / soma_cargas:.2f}")


if __name__ == "__main__":
    main()
