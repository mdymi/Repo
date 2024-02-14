imie=input("Jak masz na imię?")
wiek=input("Ile masz lat?")

print("Cześć " + imie + " Masz " + wiek + " lat!")

if int(wiek) >= 18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")