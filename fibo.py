from termcolor import colored
def fib():
    n = int(input(colored("Hangi sayıya kadar fibonacci listesi "
                             "oluşturulsun? Lütfen giriniz:", "green")))
    a = 0
    b = 1
    liste = []
    while b<n:
        liste.append(b)
        a, b = b, a + b
    print(colored("Fibonacci Listesi:","cyan"))
    print(colored(liste,"red"))

def fib2(n):   # n'e kadar olan fibonacci sayılarını döndürür.
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    print(result)
