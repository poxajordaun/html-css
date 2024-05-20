from time import sleep

minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
cont = 0
conts = 0
while minuto != 0 and segundo != 0:
    if conts == segundo:
        minuto = minuto - 1
    if cont == 0:
        cont += 1
        for c in range(segundo, 0, -1):
            print(f'{minuto}:', end='')
            print(c)
            conts += 1
            sleep(1)
    else:
        for c in range(59, 0, -1):
            print(f'{minuto}:', end='')
            print(c)
            sleep(1)
print('FIM DA CONTAGEM')
            
      