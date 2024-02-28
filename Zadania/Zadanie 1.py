# Stwórz program, który sprawdza czy podana liczba przez użytkownika jest parzysta czy nie.

liczba = int(input("Podaj jakąś liczbę: ")) # Konwersja na typ int

if liczba % 2 == 0: # Sprawdzenie, czy liczba jest parzysta
    print('Liczba jest parzysta')
elif liczba:
    print('Liczba jest nieparzysta')
else:
    print('To nie jest liczba')
if liczba not int