# Knapsack problem
#   a set of positive integers
#   a target sum
#   goal: finding a subset of integers that summed to the target
#   NP-complete problem

import random


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def get_w(n):
    w = 2
    while w < n and gcd(w, n) != 1:
        w += 1
    return w


# Zp에서 x의 inverse를 구하는 function
def get_inverse(p, x):
    r1 = p
    r2 = x
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r

        t = t1 - q * t2
        t1 = t2
        t2 = t

    if r1 == 1:
        return t1
    else:
        return None


def encrypt(P, ku):
    C = 0
    H = ku
    len_p = len(P)
    for i in range(len_p):
        C += H[i] * P[i]
    return C


def decrypt(C, kr):
    n, w, S = kr
    w_inverse = get_inverse(n, w)
    T = (w_inverse * C) % n
    len_s = len(S)
    P = []
    for i in range(len_s - 1, -1, -1):
        if T >= S[i]:
            T -= S[i]
            P.append(1)
        else:
            P.append(0)

    P.reverse()
    return P


# super increasing knapsack(private key)
S = [1, 2, 5, 9, 20, 43]
sum_s = sum(S)
len_s = len(S)

# GCD(n, w) = 1
n = random.randint(sum_s + 1, sum_s + 10)
w = get_w(n)

# compute H
H = []
for i in range(len_s):
    H.append((w * S[i]) % n)

# public key: H, private key: (n, w)
ku = H
kr = (n, w, S)

#
print("S:", S)
print("n: {}, w: {}".format(n, w))
print("H:", H)

P = [1, 0, 1, 0, 0, 1]
print("plain text:", P)
C = encrypt(P, ku)
print("cipher text:", C)

decrypted = decrypt(C, kr)
print("decrypted:", decrypted)
