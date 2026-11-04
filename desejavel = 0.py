desejavel = 0 
limitrofe = 0
alto = 0

entrada = input()
while entrada != '*':
   valor = int(entrada)
   if valor < 150:
       desesavel += 1
   elif valor <= 200:
       limitrofe += 1
   else:
       alto += 1
   entrada = input()

total = desejavel + limitrofe + alto

if total > 0:
    print(f'Desejavel: {desejavel}')