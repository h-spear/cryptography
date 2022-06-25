from tkinter.messagebox import NO


def powmod(C, n, mod):
    res = 1
    while n:
        if n & 1:
            res = res * C
        C = C * C % mod
        n >>= 1
    return res % mod


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def get_totient(p, q):
    return (p - 1) * (q - 1)


def get_public_key():
    e = 2
    while e < totient and gcd(e, totient) != 1:
        e += 1
    return e


def get_private_key():
    k = 1
    while (e * k) % totient != 1 or k == e:
        k += 1
    return k


def encrypt(ku, m):
    e, n = ku
    cipher_text = [chr(powmod(ord(char), e, n)) for char in m]
    return cipher_text


def decrypt(kr, c):
    d, n = kr
    plain_text = [chr(powmod(ord(char), d, n)) for char in c]
    return plain_text


p = int(input("select p: "))
q = int(input("select q: "))
m = list(input("input message: "))

n = p * q
totient = get_totient(p, q)
e = get_public_key()
d = get_private_key()

print("\np: {}, q: {}, n: {}, tot: {}, e: {}, d:{}\n".format(p, q, n, totient, e, d))


c = encrypt((e, n), m)

print("--- encrypt ---")
print("plain text:", m)
print("cipher text:", c)
print()

print("--- decrypt ---")
print("cipher text:", c)
print("plain text:", decrypt((d, n), c))
