def encrypt_image(path="", key=""):
    try:
        if path == "":
            path = input('[@User] Enter path of Image: ')
        if key == "":
            key = int(input('[@User] Enter Key for encryption of Image: '))
        else:
            key = int(key)
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)

        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('[Encryption complete]')
    except Exception:
        print("[Error] Try a different file path or key.")


# Note: Decryption key must be the same as the encryption key
def decrypt_image(path="", key=""):
    try:
        if path == "":
            path = input('Enter path of Image : ')
        if key == "":
            key = int(input('Enter Key for encryption of Image : '))
        else:
            key = int(key)
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)

        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('[Decryption complete]')
    except Exception:
        print("[Error] Try a different file path or key.")
