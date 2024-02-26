# Napisz program który wyświetli wszystkie liczby pierwsze od 0 do 100.

# Example 1.
#
# import math
# def is_prime(n):
#     if n < 2: # liczba mnniejsza niż 2 nie jest pierwsza
#         return False
#     i = 2
#     while i * i <= n:
#         if n % i == 0: # jeśli znajdę dzielnik, to liczba n nie jest pierwsza
#             return False
#         i += 1
#     return True # jeśli do pierwiastka z n nie znajdę dzielnika, to znaczy, że jest ona pierwsza
#
# p = int(input("Podaj liczbę naturalną, aby sprawdzić, czy jest pierwsza: ")) # wczytuję liczbę zestawów danych
#
# if is_prime(p):
#     print("TAK")
# else:
#     print("NIE")


# Example 2.

# Python program to prompt all prime numbers up to a specified limit

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prompt_primes(limit):
    """Print all prime numbers up to a specified limit."""
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

# Example: Prompt all prime numbers up to 100
prompt_primes(100)