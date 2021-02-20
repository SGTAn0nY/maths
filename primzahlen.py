'''
Author:     Kjell Ziegert
Date:       02.02.2021
LICENSE:    MIT
'''

from math import floor, sqrt
from sys import argv
from mpmath.functions.functions import arg
from sympy import mod_inverse


#returns True if given number is a prime number, false otherwise
def is_prime(num):
    if(num < 0):
        return False
    num = int(num)
    for i in range(2, num//2):
        #print("%s mod %s = %s" % (num, i, num % i))
        if num % i == 0:
            return False
    return True

#A much faster algorithm to do the same
def is_prime_fast(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


#returns greatest divisor of given two numbers
def ggt(a, b):
    if b == 0:
        return a
    else:
        return ggt(b, a % b)

#returns smallest shared multiplicator of a and b
def kgv(a, b):
    return ((a * b) / ggt(a, b))

#returns a list of all prime numbers you have to multiply to get given number
def primefactors(num, print_out):
    l = []
    prime_factors = [num]
    if(num < 0):
        prime_factors.append(-1)
    for i in range(2, floor(sqrt(221)) + 1):
        if(is_prime(i)):
            l.append(i)
    for prime_factor in l:
        if(is_prime(num)) and num != 1:
            prime_factors.append(int(num))
            break
        while True:
            if int(num % prime_factor) == 0:
                prime_factors.append(int(prime_factor))
                num = num / prime_factor
            else:
                break
    if(num > l[len(l) - 1]) and not is_prime(num) and num != 1:
        prime_factors.append(int(num))
    if(print_out):
        print(prime_factors)
    return prime_factors


def write_primefactors_to_file(num, filename):
    with open(filename, "w+") as f:
        for i in range(1, num):
            f.write(str(primefactors(i, True)) + "\n")
        f.write(str(primefactors(num, True)))
    #print("Invalid filename given ! (Please include full path)")


def crack_rsa(e, N):
    phi_N = (primefactors(N, False)[1] - 1) * (primefactors(N, False)[2] - 1)
    d = mod_inverse(e, phi_N)
    #validation of cracked private key
    if(mod_inverse(d, phi_N) != e):
        return "ERROR"
    return (d, N)


argv = argv[1:]
if(len(argv) > 0):
    if(argv[0] == "-h" or argv[0] == "--help"):
        print("functions you can use:\n\nis_prime (number)  -> Checks if a number is a prime number\nggt (number 1) (number 2)  -> Calculates ggt of two numbers\nkgv (number 1) (number 2) -> Calculates kgv of two numbers\nprimefactors (number) -> Gives back a list: First number is the number itself, after that follow primefactors\nwrite_primefactors_to_file (number) (filepath)    -> Writes all primefactors for primenumbers up to a given number to a specified text file that will be generated or overwritten\ncrack_rsa (e) (N)  -> Tries to deriviate a private key from cracking a public RSA key and gives the private key back\n")

    if(argv[0] == "is_prime"):
        try:
            print(is_prime(int(argv[1])))
        except:
            print("Error executing function, parameter was malicious !")
    if(argv[0] == "ggt"):
        try:
            print(ggt(int(argv[1]), int(argv[2])))
        except:
            print("Error executing function, parameter was malicious !")
    if(argv[0] == "kgv"):
        try:
            print(kgv(int(argv[1]), int(argv[2])))
        except:
            print("Error executing function, parameter was malicious !")
    if(argv[0] == "primefactors"):
        try:
            print(primefactors(int(argv[1]), False))
        except:
            print("Error executing function, parameter was malicious !")
    if(argv[0] == "write_primefactors_to_file"):
        try:
            print(write_primefactors_to_file(int(argv[1]), argv[2]))
        except:
            print("Error executing function, parameter was malicious !")
    if(argv[0] == "crack_rsa"):
        try:
            print(crack_rsa(int(argv[1]), int(argv[2])))
        except:
            print("Error executing function, parameter was malicious !")