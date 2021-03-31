import os
import sys
import re

import AES
import Diffie_helman
import hash
import rsa
import img
import file


def hash_func():
    hash_type = input("\n[@User] Choose hash type: \n [1] Base64\n [2] SHA1\n [3] SHA256\n [4] SHA512\n [5] MD5\n")
    if hash_type == '1':
        is_encode = input("\n[@User]:\n [1] Encryption \n [2] Decryption\n")
        if is_encode == '1':
            hash.encode_64()
        elif is_encode == '2':
            hash.decode_64()
        else:
            print('[Error] Invalid input')

    elif hash_type == '2':
        hash.encode_sha1()

    elif hash_type == '3':
        hash.encode_sha256()

    elif hash_type == '4':
        hash.encode_sha512()

    elif hash_type == '5':
        hash.encode_md5()

    else:
        print("[Error]: Invalid input")


def rsa_helper(input):
    user_input = input.split('-')
    num = user_input[1]
    try:
        bit_size = int(num)
        rsa.rsa_func("", bit_size)
    except ValueError:
        print("[Error] Invalid input. Changing bit size command is 2 -some_number")


def image_helper():
    is_encode = input("\n[@User]:\n [1] Encryption \n [2] Decryption\n")
    if is_encode == '1':
        img.encrypt_image()
    elif is_encode == '2':
        img.decrypt_image()
    else:
        print('[Error] Invalid input')


def file_helper():
    is_encode = input("\n[@User]:\n [1] Encryption \n [2] Decryption\n")
    if is_encode == '1':
        file.encrypt_file()
    elif is_encode == '2':
        file.decrypt_file()
    else:
        print('[Error] Invalid input')


def cmd_tool():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""                                
 ______     __  __     ______   __  __     ______     ______     ______    
/\  ___\   /\ \_\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \   /\  ___\   
\ \ \____  \ \____ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<   \ \___  \  
 \ \_____\  \/\_____\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
  \/_____/   \/_____/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/   \/_____/ 
                        Command line edition
                      --help for command list                                                                               
         """)
    while True:
        crypto_tool = input("\n[@User] Enter command: ")
        if "--help" in crypto_tool:
            print(""" 
[Commands] 
    - base64_encode(some_message_to_encrypt) 
    - base64_decode(some_message_to_decrypt)  
    - sha1_encode(some_message_to_encrypt)
    - sha256_encode(some_message_to_encrypt)
    - sha512_encode(some_message_to_encrypt)
    - md5_encode(some_message_to_encrypt)
    - rsa(some_message_to_encrypt, int_for_bit_size) 
    - AES_ECC(some_message_to_encrypt, some_authenticated_data)
    - AES_CBC(some_message_to_encrypt, some_key)   
    - DH(some_message_to_encrypt) 
    - image_encode(path_to_image, key_that_is_int)
    - image_decode(path_to_image, key_that_is_int)
    - file_encode(path_to_image)
    - file_decode(path_to_image)
    - no_parameters
    - exit
    """)
        elif crypto_tool == "exit":
            print('[Exiting]')
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        elif crypto_tool == "no_parameters":
            enter()
        else:
            try:
                # Getting information between the parentheses
                result = re.search(r'\((.*?)\)', crypto_tool).group(1)
                crypto_tool = crypto_tool.lower()
            except AttributeError:
                print('')
            if "base64_encode" in crypto_tool:
                hash.encode_64(result)

            elif "base64_decode" in crypto_tool:
                hash.decode_64(result)

            elif "sha1_encode" in crypto_tool:
                hash.encode_sha1(result)

            elif "sha256_encode" in crypto_tool:
                hash.encode_sha256(result)

            elif "sha512_encode" in crypto_tool:
                hash.encode_sha512(result)

            elif "md5_encode" in crypto_tool:
                hash.encode_md5(result)

            elif "rsa" in crypto_tool:
                try:
                    rsa.rsa_func(result.split(',')[0], result.split(',')[1])
                except IndexError:
                    rsa.rsa_func(result)

            elif "aes_ecc" in crypto_tool:
                try:
                    AES.aes_ecc(result.split(',')[0], result.split(',')[1])
                except IndexError:
                    print(" [Error] : Should be in the form of: "
                          "AES_ECC(some_message_to_encrypt, some_authenticated_data)")

            elif "aes_cbc" in crypto_tool:
                try:
                    AES.aes_cbc(result.split(',')[0], result.split(',')[1])
                except IndexError:
                    print(" [Error] : Should be in the form of: AES_CBC(some_message_to_encrypt, some_key) ")

            elif "dh" in crypto_tool:
                Diffie_helman.dff_func(result)

            elif "image_encode" in crypto_tool:
                try:
                    img.encrypt_image(result.split(',')[0], result.split(',')[1])
                except IndexError:
                    print(" [Error] : Should be in the form of: image_encode(path_to_image, key_that_is_int)")

            elif "image_decode" in crypto_tool:
                try:
                    img.decrypt_image(result.split(',')[0], result.split(',')[1])
                except IndexError:
                    print(" [Error] : Should be in the form of: image_decode(path_to_image, key_that_is_int)")

            elif "file_encode" in crypto_tool:
                file.encrypt_file(result)

            elif "file_decode" in crypto_tool:
                file.decrypt_file(result)

            else:
                print('[Error] ', crypto_tool , ' is an invalid input. --help for command options')


def enter():
    while True:
        crypto_tool = input("\n[@User] Choose method: \n [1] Hash\n [2] RSA\n [3] AES (ECC)\n [4] AES (CBC) \n "
                            "[5] Diffie Hellman \n [6] Image Encryption/Decryption \n "
                            "[7] File Encryption/Decryption \n [8] Help \n [9] CMD tool \n [-1] Exit\n")
        if crypto_tool == '1':
            hash_func()
        elif crypto_tool == '2':
            rsa.rsa_func()
        elif '2 -' in crypto_tool:
            rsa_helper(crypto_tool)
        elif crypto_tool == '3':
            AES.aes_ecc()
        elif crypto_tool == '4':
            AES.aes_cbc()
        elif crypto_tool == '5':
            Diffie_helman.dff_func()
        elif crypto_tool == '6':
            image_helper()
        elif crypto_tool == '7':
            file_helper()
        elif crypto_tool == '8':
            print(""" 
[HELP] 
    - [Hash] : 
        - Hash functions that can be encoded: Base64, SHA1, SHA256, SHA512, and MD5.
        - Hash functions that can be decoded: Base64.   
                
    - [RSA] : 
        - Enter message (String) to be encrypted and decrypted. 
        - Key pair is set to bit size of 3072.
             
     - [AES (ECC)] : 
        - Enter message (String) and authenticated but unencrypted data (String) to encrypt and decrypt. 
        - Key is generated on run time and is set to 128 bits. 
        
     - [AES (CBC)] : 
        - Message (String) to be encrypted and key (int) is needed and ciphertext is returned. 
        - Ciphertext (Must be what was returned) and key (int that is same key as before) is needed for decryption.
          
    - [Diffie Hellman] : 
        - Enter message (String) to be encrypted and decrypted.
        - Algorithm uses SHA256 and has PKCS7 padding.
        
    - [Images] : 
        - Enter path of Image and key (int that is same for both) for encryption and decryption.
        - Will edit file so don't mess on decryption.
        
    - [Files] : 
        - Enter path of File and key (int that is same for both) for encryption and decryption.
        - Will edit file so don't mess on decryption. 
        
    - [CMD Tool] : 
        - Method names and parameters are entered instead of being prompted. 
        - Ex. base64_encode(some_message_to_be_encrypted)        
                    """)
        elif crypto_tool == '9':
            cmd_tool()
        elif crypto_tool == '-1':
            print('[Exiting]')
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        else:
            print("[Error] Invalid input.")


if __name__ == '__main__':
    print("""                                
 ______     __  __     ______   __  __     ______     ______     ______    
/\  ___\   /\ \_\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \   /\  ___\   
\ \ \____  \ \____ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<   \ \___  \  
 \ \_____\  \/\_____\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
  \/_____/   \/_____/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/   \/_____/ 
  
                      Developed by: Josh Meritt                                                                                 
         """)
    enter()
