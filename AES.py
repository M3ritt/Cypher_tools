import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# NEED TO FIX MORE THAN ONE PARATHESEES STUFF


def aes_ecc(data="", aad=""):
    try:
        if data == "":
            data = input("\n[@User] Enter message to encrypt: ")
        if aad == "":
            aad = input("[@User] Enter authenticated but unencrypted data:")
        key = AESGCM.generate_key(bit_length=128)
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        ct = aesgcm.encrypt(nonce, data.encode(), aad.encode())
        ad = aesgcm.decrypt(nonce, ct, aad.encode())
        # print("[Encrypted AES (ECC):",str(ct)[2:-1],"\nKey:",str(key)[2:-1],"\nNonce :",str(nonce)[2:-1])
        print("[Encrypted AES (ECC)]:", str(ct)[2:-1])

        print("\n[Decrypted AES (ECC)]:", str(ad)[2:-1])
    except:
        print("Wrong Value..!")


def aes_cbc(msg="", pwd=""):
    class AESCipher:
        def __init__(self, key):
            self.key = md5(key.encode('utf8')).digest()

        def encrypt(self, data):
            iv = get_random_bytes(AES.block_size)
            self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), AES.block_size)))

        def decrypt(self, data):
            raw = b64decode(data)
            self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
            return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)

    try:
        is_param_empty = True
        if msg == "":
            msg = input("[@User] Enter message to encrypt: ")
        else:
            is_param_empty = False

        if pwd == "":
            pwd = input("[@User] Enter key to encrypt: ")
            is_param_empty = True
        cte = AESCipher(pwd).encrypt(msg).decode('utf-8')
        print('[Ciphertext]:', cte)

        if is_param_empty:
            cte = input('\n[@User] Enter ciphertext for decryption: ')
            pwd = input('[@User] Enter key for decryption: ')
            print('\n[Decrypted AES (CBC)]:', AESCipher(pwd).decrypt(cte).decode('utf-8'))
        else:
            print('\n[Decrypted AES (CBC)]:', AESCipher(pwd).decrypt(cte).decode('utf-8'))
    except:
        print("\n[Error] Invalid cipher text or key")
