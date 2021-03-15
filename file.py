from cryptography.fernet import Fernet


def encrypt_file():
    path = input('[@User] Enter path of file: ')
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as file_key:
        file_key.write(key)
    with open('filekey.key', 'rb') as file_key:
        key = file_key.read()
        print("[Key] : ", key)
    fernet = Fernet(key)

    with open(path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    with open(path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print("[Encrypted file]")


# key must be the same for encryption and decryption
def decrypt_file():
    with open('filekey.key', 'rb') as file:
        key = file.read()
    fernet = Fernet(key)
    path = input('[@User] Enter path of file: ')
    with open(path, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)
    with open(path, 'wb') as dec_file:
        dec_file.write(decrypted)
    print("[Decrypted file]")

