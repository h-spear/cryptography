# Based DLP(Discrete logarithm problem)
from random import randint


def powmod(C, n, mod):
    res = 1
    while n:
        if n & 1:
            res = res * C
        C = C * C % mod
        n >>= 1
    return res % mod


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


def encrypt(plain_text, g, y, p):
    # generate random integer k
    k = randint(1, 10)
    print("generate random integer k:", k)
    a = powmod(g, k, p)
    b = (powmod(y, k, p) * plain_text) % p
    return (a, b)


# cipher text : (a, b)
def decrypt(cipher_text, x, p):
    a, b = cipher_text
    ax = powmod(a, x, p)
    plain_text = (b * get_inverse(p, ax)) % p
    return plain_text


# prime number p
p = 17

# generator of Zp
g = 6

# private key x (x < p)
x = 5

# public key y (y = g^x (mod p))
y = powmod(g, x, p)

# plain text
m = 13

print("p: {}, g: {}, x: {}, y: {}".format(p, g, x, y))
print("input message:", m)

print("\n--- encrypt ---")
cipher_text = encrypt(m, g, y, p)
print("plain text:", m)
print("cipher text:", cipher_text)

print("\n--- decrypt ---")
plain_text = decrypt(cipher_text, x, p)
print("cipher text:", cipher_text)
print("plain text:", plain_text)
