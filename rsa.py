def rsa_func():
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    import binascii

    message = input("[@User] Enter message to encode:")

    keyPair = RSA.generate(3072)
    pubKey = keyPair.publickey()

    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(message.encode("utf-8"))
    print("[Encrypted RSA]:", binascii.hexlify(encrypted))

    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\n[Decrypted RSA]:', decrypted)

