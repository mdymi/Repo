# Stwórz program, który poda, czy podane imię jest imieniem żeńskim bądź męskim
# ( załóż, że imiona żeńskie kończą się na literę A.

name = input('Podaj swoje imię: ')

if name.endswith("a"):
    print('Jest to imię żeńskie.')
else:
    print('Jest to imię męskie')