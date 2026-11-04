qtdFeminina = 0
qtdMasculina = 0
qtdCanExperiencia = 0
qtdMediaExperiencia = 0
qtd_40mais = 0
qtd_mulheresMenor21 = 0
soma_idade = 0



idade = int(input("Qual a idade do Candidato?"))
 
while idade != 0:

    sexo = str(input("Digite M para masculino ou F para feminino. ")).upper
    exp = str(input("Digite S para se tem experiência ou N para não. ")).upper

    if sexo == 'M':
        qtdMasculina += 1
    else:
        qtdFeminina += 1

    if exp == 'S':
        qtdCanExperiencia += 1

    if idade > 40:
        qtd_40mais += 1

    if idade < 21 and sexo == "F" and exp == "S":
        qtd_mulheresMenor21 += 1

    if idade != 0 and exp == "S":
        soma_idade += idade

    print("QUANTIDADE MASCULINA:", qtdMasculina)
    print("QUANTIDADE FEMININA:",  qtdFeminina)
    print ("QUANTIDADE DE CANDIDATOS COM EXPERIÊNCIA:", qtdCanExperiencia)
    print ("PORCENTAGEM DE CANDIDATOS COM MAIS DE 40 ANOS: ",(qtd_40mais / 100), "%" ) 
    print ("QUANTIDADE DE MULHRES COM IDADE INFERIOR A 21 E COM EXPERIÊNCIA:", qtd_mulheresMenor21)
    print ("IDADE MÉDIA DOS CANDIDATOS COM EXPERIENCIA", (soma_idade / qtdCanExperiencia))
   

    idade = int(input("Qual a idade do Candidato?"))


