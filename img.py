def encrypt_image():
    try:
        path = input('[@User] Enter path of Image: ')
        key = int(input('[@User] Enter Key for encryption of Image: '))
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
        print('Error caught : ', Exception.__name__)


# Note: Decryption key must be the same as the encryption key
def decrypt_image():
    try:
        path = input('Enter path of Image : ')
        key = int(input('Enter Key for encryption of Image : '))
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
        print('[Error]: ', Exception.__name__)