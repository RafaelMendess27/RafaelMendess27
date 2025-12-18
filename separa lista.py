lista= list()
pares = list()
impares = list()
while True:
    numero = int(input('digite um numero: '))
    lista.append(numero)
    resp=str(input('quer continuar? [s/n] ')).upper()
    if resp=='N':
        break
for pos,v in enumerate(lista): # verifica a posição e o valor
    if v%2==0:
        pares.append(v)
    else:
        impares.append(v)
print(f' a lista completa é {lista}')
print(f'a lista de pare é {pares}')
print(f'a lista de impare {impares}')