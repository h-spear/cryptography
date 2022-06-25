def powmod(C, n, mod):
    res = 1
    while n:
        if n & 1:
            res = res * C
        C = C * C % mod
        n >>= 1
    return res % mod


# prime number
p = 19

# primitive root
alpha = 3

# secret value of A
Xa = 2
# calc Ya
# A send 'Ya' to B
Ya = powmod(alpha, Xa, p)

# secret value of B
Xb = 3
# calc Yb
# B send 'Yb' to A
Yb = powmod(alpha, Xb, p)


# A
Ka = powmod(Yb, Xa, p)

# B
Kb = powmod(Ya, Xb, p)

print("prime number p:", p)
print("primitive root a:", alpha)
print()
print("Xa:", Xa)
print("Ya:", Ya)
print()
print("Xb:", Xb)
print("Yb:", Yb)
print()
print("calculate K from A:", Ka)
print("calculate K from B:", Kb)
print()
print("Key Exchange:", Ka == Kb)
