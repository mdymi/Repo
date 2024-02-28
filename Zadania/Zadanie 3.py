# Napisz program który spyta użytkownika o wynik na egzaminie (od 0 do 100) i wyświetli odpowiednią ocenę.
wynik_egzaminu = int(input("Jaki był wynik Twojego egzaminu ? "))
#print(type(wynik_egzaminu))
if wynik_egzaminu in range(90,100):
    print("Dostałeś ocenę 5 !")

elif wynik_egzaminu in range(80,90):
    print("Dostałeś ocenę 4 !")
elif wynik_egzaminu in range(70,80):
    print("Dostałeś ocenę 3 !")
elif wynik_egzaminu in range(60,70):
    print("Dostałeś ocenę 2 !")
elif wynik_egzaminu >100 or wynik_egzaminu <0:
    print("Wynik powinien być w skali 0-100")
else:
    print("Niezdałeś !")