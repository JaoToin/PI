codigo = int(input("Digite o Código"))
valor = float(input("Digite o Valor"))
percentual = int(input("Digite o Valor Do Percentual De 1 a 100"))

produto = 0 



while codigo != 0:
    
    valorPercentual = percentual / 100

    novoValor = valor  + (valor * valorPercentual)

    if novoValor > 100 and percentual > 0.05:
        produto + 1 

