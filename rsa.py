from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def rsa_func(message="", bitsize=""):
    if message == "":
        message = input("\n[@User] Enter message to encode:")

    if bitsize == "":
        key_pair = RSA.generate(1024)
    else:
        print("[Bit size]:", int(bitsize))
        key_pair = RSA.generate(int(bitsize))

    public_key = key_pair.publickey()

    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(message.encode("utf-8"))
    print("[Encrypted RSA]:", binascii.hexlify(encrypted))

    decrypter = PKCS1_OAEP.new(key_pair)
    decrypted = decrypter.decrypt(encrypted)
    print('\n[Decrypted RSA]:', decrypted)
