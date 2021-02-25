import os
import sys
from rsa import rsa_func
import hash


def hashh():
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


def enter():
    while True:
        crypto_tool = input("\n[@User] Choose method: \n [1] Hash\n [2] RSA\n [3] Exit\n")
        if crypto_tool == '1':
            hashh()
        elif crypto_tool == '2':
            rsa_func()
        elif crypto_tool == '3':
            print('[Exiting]')
            os.system('cls' if os.name=='nt' else 'clear')
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

