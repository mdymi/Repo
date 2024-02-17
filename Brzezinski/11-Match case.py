light = input("Jakie widzisz światło ? (zielone, zółte, czerwone)")

match light:
    case 'zielone':
        print("Możesz jechać")
    case 'zółte':
        print("Przygotuj się !")
    case 'czerwone':
        print("Stój !")
    case _:
        print("Nie znam takiego koloru ?")

