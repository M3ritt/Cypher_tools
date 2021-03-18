import base64
import binascii
import hashlib


def encode_64(message=""):
    if message == "":
        message = input("\n[@User] Enter message to encode:")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("[Encoded base64]: ", base64_message)


def decode_64(base64_message=""):
    if base64_message == "":
        base64_message = input("\n[@User] Enter hash to decode:")
    base64_bytes = base64_message.encode('ascii')
    try:
        message_bytes = base64.b64decode(base64_bytes)
        print("[Decoded base64]:", message_bytes.decode('ascii'))
    except binascii.Error:
        print("[Error] Invalid padding on message")


def encode_sha1(str2hash=""):
    if str2hash == "":
        str2hash = input("\n[@User] Enter message to encode:")
    result = hashlib.sha1(str2hash.encode())
    print("[Encoded SHA1]:", end="")
    print(result.hexdigest())


def encode_sha256(str2hash=""):
    if str2hash == "":
        str2hash = input("\n[@User] Enter message to encode:")
    result = hashlib.sha256(str2hash.encode())
    print("[Encoded SHA256]:", end="")
    print(result.hexdigest())


def encode_sha512(str2hash=""):
    if str2hash == "":
        str2hash = input("\n[@User] Enter message to encode:")
    result = hashlib.sha3_512(str2hash.encode())
    print("[Encoded SHA512]:", end="")
    print(result.hexdigest())


def encode_md5(str2hash=""):
    if str2hash == "":
        str2hash = input("\n[@User] Enter message to encode:")
    result = hashlib.md5(str2hash.encode())
    print("[Encoded MDH5]:", end="")
    print(result.hexdigest())
