
key = "abcdefghijklmnopqrstuvwxyz!,'"

def encrypt(n, plaintext):
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 29
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 29
            result += key[i]
        except ValueError:
            result += l

    return result

def show_result(plaintext, n):
    encrypted = encrypt(n, plaintext)
    decrypted = decrypt(n, encrypted)

    print 'Rotation: %s' % n
    print 'Plaintext: %s' % plaintext
    print 'Encrypted: %s' % encrypted
    print 'Decrytped: %s' % decrypted


show_result("No, thank you! We don't want any more visitors, well wishers or distant relations", 5)

