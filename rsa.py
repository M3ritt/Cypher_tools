from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


def rsa_func():
    message = input("\n[@User] Enter message to encode:")
    key_pair = RSA.generate(3072)
    public_key = key_pair.publickey()

    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(message.encode("utf-8"))
    print("[Encrypted RSA]:", binascii.hexlify(encrypted))

    decrypter = PKCS1_OAEP.new(key_pair)
    decrypted = decrypter.decrypt(encrypted)
    print('\n[Decrypted RSA]:', decrypted)


def rsa_different_bit_size(bit_size):
    message = input("\n[@User] Enter message to encode:")
    print("[Bit size]:", bit_size)
    key_pair = RSA.generate(bit_size)
    public_key = key_pair.publickey()

    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(message.encode("utf-8"))
    print("[Encrypted RSA]:", binascii.hexlify(encrypted))

    decrypter = PKCS1_OAEP.new(key_pair)
    decrypted = decrypter.decrypt(encrypted)
    print('\n[Decrypted RSA]:', decrypted)
