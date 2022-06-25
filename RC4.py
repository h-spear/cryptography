bits = 256


def key_schedling(key):
    key = key.encode()

    # initialize
    key_length = len(key)
    S = [i for i in range(bits)]
    T = [key[i % key_length] for i in range(bits)]

    # key scheduling
    j = 0
    for i in range(bits):
        j = (j + S[i] + T[i]) % bits
        S[i], S[j] = S[j], S[i]

    return S


def encrypt(message, key):
    i = 0
    j = 0
    S = key_schedling(key)
    stream_key = []
    message = message.encode()
    cipher_text = bytearray()

    for k in range(len(message)):
        i = (i + 1) % bits
        j = (j + S[i]) % bits
        S[i], S[j] = S[j], S[i]
        stream_key.append(S[(S[i] + S[j]) % bits])
        cipher_text.append(message[k] ^ stream_key[k])
    return cipher_text


def decrypt(message, key):
    i = 0
    j = 0
    S = key_schedling(key)
    stream_key = []
    plain_text = bytearray()

    for k in range(len(message)):
        i = (i + 1) % bits
        j = (j + S[i]) % bits
        S[i], S[j] = S[j], S[i]
        stream_key.append(S[(S[i] + S[j]) % bits])
        plain_text.append(message[k] ^ stream_key[k])
    return plain_text


# message = input("plaintext: ")
# key = input("key: ")
message = "HELLO WORLD! THIS IS STUDY"
key = "COMPUTER SCIENCE"

cipher_text = encrypt(message, key)
print("ciphertext:", cipher_text)

original_text = decrypt(cipher_text, key)
print("decrypted:", original_text)
