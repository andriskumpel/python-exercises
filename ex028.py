from random import randint
from time import sleep
computador = randint(0,5) # faz o computador "pensar"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
jogador = int(input('Em que número pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

