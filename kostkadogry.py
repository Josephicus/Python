import random

pytanie = input('Czy chcesz rzucic kostka - T lub N: ')
lpytanie = pytanie.lower()

if lpytanie == ('t'):
    kostka = random.randint(1,6)
    print('Twoj wynik to:')
    print(kostka)


else:
    print('Wybrales/as Nie')

blank = input()