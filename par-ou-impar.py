from random import randint
S = N = C = G = 0
print('=-='*10)
print('VAMOS JOGAR PAR OU IMPAR ')
print('=-='*10)
while True:
    N = int(input('Digite um valor '))
    C = randint(0, 10)
    while True:
        PI = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
        if PI in ['P', 'I']:
            break
        print('Digite apenas P ou I')
    print('-'*30)
    S = N + C
    if S % 2 == 0:
        F = 'PAR'
    else:
        F = 'IMPAR'
    print(f'Voce jogou {N} e o computador jogou {C}. Total de {S} deu {F}')
    if F [0] == PI:
        print('Voce \033[32m VENCEU \033[m')
        print('Vamos jogar novamente')
        G += 1
    if F [0] != PI:
        print('Voce \033[31m PERDEU!\033[m')
        print('=-='*10)
        print(f'GAME OVER! Voce venceu {G} vezes')
        break
