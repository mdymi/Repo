# Napisz program czy podana liczba przez użytkownika jest większa od 0, mniejsza od 0, czy równa 0.
liczba = int(input("Podaj jakąś liczbę proszę."))

if liczba <=0:
    print("Liczba jest mniejsza od zera.")
elif liczba ==0:
    print("Liczba jest równa zero")
else:
    print("Liczba jest większa od zera.")